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
enemy2 = pygame.image.load("halloween.png")
enemy3 = pygame.image.load("chinese.png")
enemy4 = pygame.image.load("fly.png")
l=[enemy,enemy1,enemy2,enemy3,enemy4]


em=[]
ex=[]
ey=[]
ex_change=[]
ey_chnage=[]

for i in range(len(l)):
    em.append(l[i])
    ex.append(random.randint(900,1000))
    ey.append(random.randint(350,370))
    ex_change.append(1)

print(em)
print(ex)
print(ey)
print(ex_change)


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
def villains(a,b,i):
    screen.blit(em[i],(a,b))


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
    distance1=math.sqrt(((ix - ex[0]) ** 2) + ((iy - ey[0]) ** 2))
    l=[enemy,enemy1,enemy2,enemy3,enemy4]
    for i in range(0,len(l)):
        em.append(l[i])
        if i==0:
            ex[i]-=ex_change[i]
            if ex[i]<0 :
                ex[i]=random.randint(900,1000)
                ey[i]=random.randint(350,370)



            villains(ex[i],ey[i],i)
            i=i+1
        if i==1:
            ex[i]-=ex_change[i]
            if ex[i]<0:
                ex[i]=random.randint(900,1000)
                ey[i]=random.randint(350,370)
                villains(ex[i],ey[i],i)
            i=i+1
        if i==2:
            ex[i]-=ex_change[i]
            if ex[i]<0:
                ex[i]=random.randint(900,1000)
                ey[i]=random.randint(350,370)
            villains(ex[i],ey[i],i)
            i=i+1
        if i==3:
            ex[i] -= ex_change[i]
            if ex[i] < 0:
                ex[i] = random.randint(900, 1000)
                ey[i] = random.randint(350, 370)
            villains(ex[i], ey[i], i)
            i = i + 1
        if i==4:
            ex[i] -= ex_change[i]
            if ex[i] < 0:
                ex[i] = random.randint(900, 1000)
                ey[i] = random.randint(350, 370)
        --=villains(ex[i], ey[i], i)
        if distance1 < 27:
            iy = 370
            bullet_state = "Ready"

            ex[0] = random.randint(900, 1000)
            ey[0] = random.randint(350, 370)
        villains(ex[0],ey[0],0)
        ex[0]=ex[0]-ex_change[0]








    play(x, y)
    pygame.display.update()