#importing pygame
import pygame
from sys import exit

#initializing pygame
pygame.init()

#Creating your screen and important variables
screen = pygame.display.set_mode((1000,750)) #widht,height #(()) its a tuple
pygame.display.set_caption('Backgrounds.png') #setting the name of the game
clock = pygame.time.Clock()
test_font = pygame.font.Font('pixeltype.ttf',30) #font type and font size
game_active = True

background_surface = pygame.image.load('backgrounds.png').convert_alpha() #converting an image to alpha facilitates pygame to read the code and make it lighter

title0_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title1_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title2_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title3_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title4_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title5_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title6_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title7_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title8_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()

game_over = pygame.image.load('gameover.png')

#score 
score_surface = test_font.render('Score:', False, 'White') #text you want to display, anti anliasing(False or True) , color
score_rect = score_surface.get_rect(topleft = (425,50 ))

#enemies
snake_surface = pygame.image.load('Snake\Cobra 1.png').convert_alpha()
snake_rect = snake_surface.get_rect(bottomright = (600,605))

#Player
player_surface = pygame.image.load('WalkSoldier\Soldado (1).png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (200,605)) #get the player surface and draws an rectangle around
#Gravity
player_gravity = 0

#defining the color of the background (display surface)
#test_surface = pygame.Surface((100,200))
#test_surface.fill('Red')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

#inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 605:
                player_gravity = -20
        
        # code to clik on the player to jump if necessary
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #if player_rect.collidepoint(event.pos):
                #player_gravity = -20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_active = True
                snake_rect.left = 800


    if game_active:
    #background
        screen.blit(background_surface,(0,0))
    #Ground
        screen.blit(title0_surface,(0,600))  #blit is used when you want to put a surface in another surface    
        screen.blit(title1_surface,(128,600))  #blit is used when you want to put a surface in another surface    
        screen.blit(title2_surface,(256,600))  #blit is used when you want to put a surface in another surface    
        screen.blit(title3_surface,(384,600))  #blit is used when you want to put a surface in another surface    
        screen.blit(title4_surface,(512,600))  #blit is used when you want to put a surface in another surface    
        screen.blit(title5_surface,(640,600))  #blit is used when you want to put a surface in another surface    
        screen.blit(title6_surface,(672,600))  #blit is used when you want to put a surface in another surface    
        screen.blit(title7_surface,(800,600))  #blit is used when you want to put a surface in another surface    
        screen.blit(title8_surface,(928,600))  #blit is used when you want to put a surface in another surface    
    #Score  
        pygame.draw.rect(screen,'Black',score_rect)
        screen.blit(score_surface,(425,50))
        
    #Snake   
        snake_rect.x -= 3
        if snake_rect.right <= 0:
            snake_rect.left = 1000
        pygame.draw.rect(screen,'Red',snake_rect)
        screen.blit(snake_surface,(snake_rect))

    #player
        player_gravity += 1
        player_rect.y += player_gravity
        
        #simulating the colision with the floor
        if player_rect.bottom >= 605:
            player_rect.bottom = 605