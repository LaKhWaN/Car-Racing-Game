import pygame
import time

pygame.init()

display_width = 1280
display_height = 720
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('LaKhWaN')
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

car_width = 73
car_height = 82

carImg = pygame.image.load('G:\My Drive\Python Projects! (1)\Python Game\PyGame\car.png')

def car(x,y):
    display.blit(carImg,(x,y))    
    
def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2,display_height/2))
    display.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed.')
    
def game_loop():
        
    x = (display_width*0.45)
    y = (display_height*0.8)

    dx = 0
    dy = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -5
                elif event.key  == pygame.K_RIGHT:
                    dx = 5
                elif event.key == pygame.K_UP:
                    dy = -5
                elif event.key == pygame.K_DOWN:
                    dy = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or pygame.K_LEFT or pygame.K_UP or pygame.K_DOWN:
                    dx = 0
                    dy = 0

        
        x+=dx
        y+=dy

        display.fill(white)
        car(x,y)
        
        if x > display_width - car_width or x < 0:
            crash()
        if y > display_height - car_height or y < 0:
            crash()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
