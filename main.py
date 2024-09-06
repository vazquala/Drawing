import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
PURPLE = (128, 0, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 128, 0)

display_surface.fill(WHITE)

TOP_LEFT_X = 200
TOP_LEFT_Y = 200
WIDTH = 200
HEIGHT = 200
rect = pygame.Rect(TOP_LEFT_X, TOP_LEFT_Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, BLUE, rect)

CENTER = (300, 300)
RADIUS = 100
pygame.draw.circle(display_surface, YELLOW, CENTER, RADIUS)

START = (200, 200)
END = (400, 400)
pygame.draw.line(display_surface, RED, START, END, 6)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
