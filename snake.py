import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))
bgimage = pygame.image.load("resized.jpg")

mixer.music.load("bgmusic.wav")
mixer.music.play(-1)

pygame.display.set_caption("Coronagame")
pic = pygame.image.load("virus.png")
pygame.display.set_icon(pic)

player = pygame.image.load("medi.png")
x = 400
y = 480
x_change = 0

enemy = []
cx = []
cy = []
cx_change = []
cy_change = []

for i in range(6):
    enemy.append(pygame.image.load("coro.png"))
    cx.append(random.randint(0, 800))
    cy.append(random.randint(50, 150))
    cx_change.append(3)
    cy_change.append(20)
print(enemy)

inject = pygame.image.load("security.png")
ix = 0
iy = 480
ix_change = 0
iy_change = 4
bullet_state = "Ready"


def play(a, b):
    screen.blit(player, (a, b))


def corona(a, b, i):
    screen.blit(enemy[i], (a, b))


def injec(a, b):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(inject, (a + 16, b + 10))


def iscollision(cx, cy, ix, iy):
    distance = math.sqrt(((cx - ix) ** 2) + ((cy - iy) ** 2))
    if distance < 27:
        return True
    else:
        return False


score_gained = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scX = 10
scY = 10

over_font=pygame.font.Font("freesansbold.ttf",64)




def points(a, b):
    score = font.render("SCORE:" + str(score_gained), True, (0, 0, 255))
    screen.blit(score, (a, b))

def game_over():
    over_text = font.render("GAME OVER" + "  madeby NITHIL", True, (255, 0, 0))
    screen.blit(over_text, (200,250))


running = True
while running:

    screen.fill((0, 0, 255))
    screen.blit(bgimage, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= 5

            elif event.key == pygame.K_RIGHT:
                x_change += 5

            elif event.key == pygame.K_SPACE:
                if bullet_state == "Ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    ix = x
                    injec(ix, iy)
        elif (event.type == pygame.KEYUP):
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                x_change = 0

    x += x_change
    if x < 0:
        x = 0
    elif x > 756:
        x = 756

    for i in range(6):
        if cy[i] > 440:
            for j in range(6):
                cy[j] = 2000
            game_over()
            break

        cx[i] += cx_change[i]
        if cx[i] < 0:
            cx_change[i] = 3
            cy[i] += cy_change[i]
        elif cx[i] > 756:
            cy[i] += cy_change[i]
            cx_change[i] = -2
        collision = iscollision(cx[i], cy[i], ix, iy)
        if collision:
            collision_sound = mixer.Sound("strike.wav")
            collision_sound.play()
            iy = 480
            bullet_state = "Ready"
            score_gained = score_gained + 1
            cx[i] = random.randint(0, 800)
            cy[i] = random.randint(50, 150)
        corona(cx[i], cy[i], i)

    if iy <= 0:
        iy = 480
        bullet_state = "Ready"
    if bullet_state == "Fire":
        injec(ix, iy)
        iy -= iy_change

    play(x, y)
    points(scX, scY)
    pygame.display.update()
