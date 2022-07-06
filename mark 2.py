import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
bgimage = pygame.image.load("markbimag.jpg")

mixer.music.load("bgm.mp3")
mixer.music.play(-1)


pygame.display.set_caption("FireBall")
pic = pygame.image.load("fireball.png")
pygame.display.set_icon(pic)


play = pygame.image.load("holidays.png")
x = 400
y = 430
x_change = 0
y_change = 0

enemy = []
cx = []
cy = []
cx_change = []
cy_change = []
for i in range(10):
    enemy.append(pygame.image.load("comet.png"))
    cx.append(random.randint(0, 760))
    cy.append(random.randint(0, 10))
    cx_change.append(0)
    cy_change.append(2)
    state = "ready"


def player(a, b):
    screen.blit(play, (a, b))


def fire(a, b, i):
    screen.blit(enemy[i], (a, b))
    state="ready"



def iscollison(cx, cy, x, y):
    distance = math.sqrt(((cx - x) ** 2) + ((cy - y) ** 2))
    if distance < 27:
        return True
    else:
        return False

font = pygame.font.Font("freesansbold.ttf", 32)
over_font = pygame.font.Font("freesansbold.ttf", 64)

score_gained=0
zx=10
zy=10

def points(a, b):
    score = font.render("SCORE:" + str(score_gained), True, (0, 255, 255))
    screen.blit(score, (a, b))

def game_over():
    over_text = font.render("GAME OVER" + "  Develeoped by NITHIL", True, (255, 0, 0))
    screen.blit(over_text, (150, 280))




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = x_change - 5
            elif event.key == pygame.K_RIGHT:
                x_change = y_change + 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                x_change = 0

    a = screen.fill((100, 100, 0))
    screen.blit(bgimage, (0, 0))
    x = x + x_change
    if x < 0:
        x = 0
    elif x > 750:
        x = 750
    for i in range(10 ):
        cy[i] = cy[i] + 3
        #assound=mixer.Sound("h.mp3")
        #assound.play()
        if cy[i] > 430:
            cx[i] = random.randint(0, 760)
            cy[i] = random.randint(0, 10)
            score_gained = score_gained + 1
        if (state=="ready"):
            fire(cx[i], cy[i], i)
        collision=iscollison(cx[i],cy[i],x,y)
        if collision:
            collision_sound = mixer.Sound("strike.wav")
            collision_sound.play()
            state="stop"
    if (state=="stop"):
        game_over()

    player(x, y)
    points(zx,zy)
    pygame.display.update()
