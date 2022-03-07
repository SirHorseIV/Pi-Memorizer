import pygame
from inputHandler import inputHandler
from cameraController import camera

pygame.init()
clock=pygame.time.Clock()
FPS=60
WINDOW_SIZE=[800,200]
screen=pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pi Memorizer")
inp=inputHandler()
with open("pi.txt","r") as file:
    digits=file.read()
index=0
digitNum=0
font=pygame.font.Font("Shippori.ttf",150)
smallFont=pygame.font.Font("Shippori.ttf",30)
text=font.render(digits[:index],True,(255,255,255))
textRect=text.get_rect(center=(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2))
smallText=smallFont.render(str(digitNum),True,(255,255,255))
cam=camera(textRect.midright,10,WINDOW_SIZE)

# Game Loop
running=True
while running:
    cam.update(textRect.midright)
    # Draw
    screen.fill((40,43,48))
    screen.blit(text,textRect.move(cam.smoothScroll).move(WINDOW_SIZE[0]*2/5,10).topleft)
    screen.blit(smallText,(20,0))
    # Update Display
    pygame.display.update()
    clock.tick(FPS)
    # Get Input
    inp.getInput()
    # Handle Input
    if inp.quit:
        pygame.quit()
        running=False
    inp.getStringInput()
    character=inp.character
    if character!="":
        if character==digits[index]:
            index+=1
            if digits[index-1]!=".":
                digitNum+=1
            text=font.render(digits[:index],True,(255,255,255))
            textRect=text.get_rect(center=(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2))
            smallText=smallFont.render(str(digitNum),True,(255,255,255))
