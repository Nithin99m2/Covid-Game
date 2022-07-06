import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("nithin")

bgimg = pygame.image.load("hk.jpg")

player = pygame.image.load("people.png")
x = 50
y = 370
x_change = 0
y_change = 0

enemy = pygame.image.load("alien.png")
enemy1 = pygame.image.load("alien2.png")
ex1 = 0
ey1 = 0
ex1_change = 3
ey1_change = 0
enemy2 = pygame.image.load("halloween.png")
ex2 = 0
ey2 = 0
ex2_change = 3
ey2_change = 0

enemy3 = pygame.image.load("chinese.png")
ex3 = 0
ey3 = 0
ex3_change = 3

enemy4 = pygame.image.load("fly.png")
ex4 = 0
ey4 = 0
ex4_change = 3

ex = random.randint(900, 1000)
ey = random.randint(350, 370)
ex_change = 3
ey_change = 0


def enemies(a, b):
    screen.blit(enemy, (a, b))


def enemies1(a, b):
    screen.blit(enemy1, (a, b))


def enemies2(a, b):
    screen.blit(enemy2, (a, b))


def enemies3(a, b):
    screen.blit(enemy3, (a, b))


def enemies4(a, b):
    screen.blit(enemy4, (a, b))


strip = pygame.image.load("j.png")

bull = pygame.image.load("weapons.png")
ix = 0
iy = 370
ix_change = 4
iy_change = 0
bullet_state = "Ready"


def injec(a, b):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bull, (a + 16, b - 1))


def play(a, b):
    screen.blit(player, (a, b))

distance1=math.sqrt(((ex - ix) ** 2) + ((ey - iy) ** 2))
distance2=math.sqrt(((ex1 - ix) ** 2) + ((ey1 - iy) ** 2))
distance3=math.sqrt(((ex2 - ix) ** 2) + ((ey2 - iy) ** 2))
distance4=math.sqrt(((ex3 - ix) ** 2) + ((ey3 - iy) ** 2))
distance5=math.sqrt(((ex4 - ix) ** 2) + ((ey4 - iy) ** 2))
playing = True

while playing:
    screen.fill((0, 0, 255))
    screen.blit(bgimg, (0, 0))
    screen.blit(strip, (-2, 400))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_change -= 3
            if event.key == pygame.K_RIGHT:
                x_change += 3
            if event.key == pygame.K_LEFT:
                x_change -= 3
            if event.key == pygame.K_s:

                if bullet_state == "Ready":
                    ix = x
                    iy = y
                    injec(ix, iy)
                    print("bulletrelessed")
        elif (event.type == pygame.KEYUP):
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x = x + x_change
    if x < 0:
        x = 0
    elif x > 756:
        x = 756

    y = y + y_change
    if y < 300:
        y_change = 3
    if y > 370:
        y = 370

    if ix >= 800:
        ix = x
        bullet_state = "Ready"
    if bullet_state == "Fire":
        injec(ix, iy)
        ix += ix_change

    ex = ex - ex_change
    enemies(ex, ey)
    if ex < 0:
        ex1 = random.randint(900, 1000)
        ey1 = random.randint(350, 370)
    enemies1(ex1, ey1)
    ex1 = ex1 - ex1_change
    if ex1 < 0:
        ex2 = random.randint(900, 1000)
        ey2 = random.randint(350, 370)
    enemies2(ex2, ey2)

    ex2 = ex2 - ex2_change
    if ex2 < 0:
        ex3 = random.randint(900, 1000)
        ey3 = random.randint(300, 310)
    enemies3(ex3, ey3)
    ex3 = ex3 - ex3_change
    if ex3 < 0:
        ex4 = random.randint(900, 1000)
        ey4 = random.randint(300, 310)
    enemies4(ex4, ey4)
    ex4 = ex4 - ex4_change

    if ex4 < 0:
        ex = random.randint(900, 1000)
        ey = random.randint(350, 370)
    enemies(ex, ey)

    if distance1<27:
        iy=480
        bullet_state="Ready"
        ex=random.randint(900,1000)
        ey=random.randint(350,370)
    enemies(ex,ey)

    play(x, y)

    pygame.display.update()
