import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))

screen.fill((0,100,100))
witch=pygame.image.load("witch2.png")
x=200
y=150
x_change=0
y_change=0

bgimg=pygame.image.load("xlconv.jpg")
bx=0
def player(a,b):
    screen.blit(witch,(a,b))

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
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                
                x_change=0
                y_change=0
    x=x+x_change
    y=y+y_change

    player(x,y)
    
    pygame.display.update()


