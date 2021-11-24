# Import pygame and time modules
import pygame
# Initialize pygame
pygame.init() 

screen = pygame.display.set_mode((550, 400))
pygame.display.set_caption("City Runner Game")

# Create image loading function here
def image_load(location, length, width):
    img = pygame.image.load(location).convert_alpha()
    img_scaled = pygame.transform.smoothscale(img,(length,width))
    return img_scaled

# Create a function to display coins here
def coin_display():
    x = 0
    for i in coins:
        screen.blit(i,(70*(x+1),210))
        x += 1
 
bgImg = image_load("background.png",800,400)
char = image_load("character.png",40,90)
coin = image_load("coin.png",50,50)
coins = [coin for i in range(6)]

# All variables required to track background, character and coin positions are defined here
bgx = 0
charx = 10
chary = 210
x = 0

# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            carryOn = False  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                charx += 10
                bgx -= 1
        # If character goes beyond 500 coordinate along x-axis reset position of character and background
        if charx >= 500:
            charx = 10
            bgx = 0
    

    # Display the background, character and coins here
    screen.blit(bgImg,(bgx,0))
    screen.blit(char,(charx,chary))
    coin_display()
    
    pygame.display.flip()
pygame.quit()