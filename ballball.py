import pygame
import random
import time
pygame.init()
HEIGHT = 600
WIDTH = 800
FPS = 60
WHITE =(255,255,255)
BLACK =(0,0,0)
RED =(255,0,0)
GREEN =(0,255,0)
BLUE =(0,0,255)
LIGHTBLUE =(115,215,255)
BROWN =(123, 63, 0)
YELLOW =(255,255,0)
GRASGREEN =(34,139,34)
DARKRED =(63,0,0)
sc = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("example")
clock = pygame.time.Clock()
heights = [100, HEIGHT // 2, HEIGHT - 100]
gate = -1
x = 0
y = random.choice(heights)
v = 5
score = 1
level = 1
def draw():
    gatecolors = [GREEN, GREEN, GREEN]
    sc.fill(LIGHTBLUE)
    if gate != -1:
        gatecolors[gate] = GRASGREEN
    pygame.draw.rect(sc, gatecolors[0], (WIDTH - 50, heights[0], 30, 80))
    pygame.draw.rect(sc, gatecolors[1], (WIDTH - 50, heights[1], 30, 80))
    pygame.draw.rect(sc, gatecolors[2], (WIDTH - 50, heights[2], 30, 80))
    pygame.draw.circle(sc, RED, (x, y +40), 20)
    pygame.display.flip()

def gettext(message, color, x, y):
    font = pygame.font.SysFont("Calibri", 36)
    text = font.render(message, True, color)
    place = text.get_rect(center = (x, y))
    sc.blit(text, place)
    pygame.display.flip()


trigger = True

play = True
while play:
    clock.tick(FPS)
    if x > WIDTH - 50:
        v = 0
        if gate == -1 or y != heights[gate]:
            gettext("You lost!", WHITE, WIDTH // 2, HEIGHT // 2)
            gettext("Press 'Enter' to restart the game", WHITE, WIDTH // 2, (HEIGHT // 2) + 50)
            level = 0
        else:
            gettext(f"You passed level {level}!", WHITE, WIDTH // 2, HEIGHT // 2)
            gettext("Press 'Enter' to continue the game", WHITE, WIDTH // 2, (HEIGHT // 2) + 50)
        trigger = False
        time.sleep(0.2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if x < WIDTH - 50:
                if event.key == pygame.K_1:
                    gate = 0
                if event.key == pygame.K_2:
                    gate = 1
                if event.key == pygame.K_3:
                    gate = 2
            if not trigger and event.key == pygame.K_RETURN:
                x = 0
                y = random.choice(heights)
                gate = -1
                trigger = True
                level += 1
                v = level * 5

    draw()


    x += v
pygame.quit()