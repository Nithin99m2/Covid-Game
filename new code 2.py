import pygame
from pygame import mixer

pygame.init()

screen=pygame.display.set_mode((800,600))

screen.fill((0,100,100))
witch=pygame.image.load("witch2.png")
x=200
y=150
x_change=0
y_change=0

mixer.music.load("bgmusic.mp3")
mixer.music.play(-1)


pygame.display.set_caption("WITCH game")
pic = pygame.image.load("witch.png")
pygame.display.set_icon(pic)

inject = pygame.image.load("meteor.png")
ix = 200
iy = 0
ix_change = 4
iy_change = 0
bullet_state = "Ready"

bgimg=pygame.image.load("xlconv.jpg")
bx=0
def player(a,b):
    screen.blit(witch,(a,b))

def injec(a, b):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(inject, (a + 16, b + 10))



playing=True
while playing:
    esc=bx%bgimg.get_rect().width
    
    screen.blit(bgimg,(esc-bgimg.get_rect().width,0))
    if esc<800:
        screen.blit(bgimg,(esc,0))
    
    bx-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= 2

            elif event.key == pygame.K_RIGHT:
                x_change += 2
            elif event.key == pygame.K_UP:
                y_change -= 2
            elif event.key == pygame.K_DOWN:
                y_change += 2
            elif event.key == pygame.K_SPACE:
                if bullet_state == "Ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    iy = y
                    ix = x
                    injec(ix, iy)
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                
                x_change=0
                y_change=0
    x=x+x_change
    y=y+y_change
    if x<0:
        x=0
    if x>756:
        x=756




    if ix >800:
        ix = 200
        bullet_state = "Ready"
    if bullet_state == "Fire":
        injec(ix, iy)
        ix += ix_change


    player(x,y)
    
    pygame.display.update()


