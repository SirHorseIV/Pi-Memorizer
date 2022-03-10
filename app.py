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
playing=True

# Game Loop
running=True
while running:
    # Get Input
    inp.getInput()
    if inp.quit:
        pygame.quit()
        running=False
    if playing:
        cam.update((textRect.move(-WINDOW_SIZE[0]*2/5,-10).midright))
        # Draw
        screen.fill((40,43,48))
        screen.blit(text,textRect.move(cam.smoothScroll).topleft)
        screen.blit(smallText,(20,0))
        # Handle Input
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
            else:
                wrong=True
                playing=False
    elif wrong:
        cam.update(textRect.move(WINDOW_SIZE[0]*1/4,-10).midright)
        # Draw
        screen.fill((202,52,51))
        text=font.render(digits[:index],True,(255,255,255))
        textRect=text.get_rect(center=(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2))
        screen.blit(text,textRect.move(cam.smoothScroll).topleft)
        nextText=font.render(digits[index:index+10],True,(245,113,139))
        nextTextRect=nextText.get_rect(midleft=textRect.midright)
        screen.blit(nextText,nextTextRect.move(cam.smoothScroll).topleft)
        smallText=smallFont.render("Press R to reset",True,(255,255,255))
        screen.blit(smallText,(20,0))
        # Handle Input
        inp.getStringInput()
        character=inp.character
        if character=="r":
            index=0
            digitNum=0
            text=font.render(digits[:index],True,(255,255,255))
            smallText=smallFont.render(str(digitNum),True,(255,255,255))
            playing=True
            wrong=False

    # Update Display
    pygame.display.update()
    clock.tick(FPS)
