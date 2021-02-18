import pygame
import time
import random
import math
from pygame import mixer
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

# title and loon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('background-img.jpg')

# Background Sound 
mixer.music.load('background.mp3')
mixer.music.play(-1)
# Player 
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy-1
enemy_1_Img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6
for i in range(num_of_enemies):
        
    enemy_1_Img.append(pygame.image.load("enemy_1.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(0,150))
    enemyX_change.append(0.3)
    enemyY_change.append(-0.01)

# bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bullet_Img = pygame.image.load("bigbang.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

# Score 

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10
def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))


def enemy_1(x, y, i):
    screen.blit(enemy_1_Img[i],(x,y))
    

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bullet_Img, (x + 24 ,y + 25))



def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) +(math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:

    screen.fill((28,85,80))
    # backgraound image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left

        # right and left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound("bullet.wav")
                    bullet_Sound.play()
                    
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX 
                    fire_bullet(bulletX, bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        # up and down 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0
    # Cheacking for boundaries of spaceship so it doesn't ho out of bounds
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # Enemy movement x-axis
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        
        if enemyX[i] <= 0:
            enemyX[i] = 0
            if enemyX[i] == 0:
                enemyX_change[i] = 0.4
        elif enemyX[i] >= 736:
            enemyX[i] = 736
            if enemyX[i] == 736:
                enemyX_change[i] = -0.4
    # Enemy movement y-axis
        
        enemyY[i] += enemyY_change[i]

        if enemyY[i] <= 0:
            enemyY[i] = 0
            if enemyY[i] == 0:
                enemyY_change[i] = 0.5
        elif enemyY[i] >= 520:
            enemyY[i] = 520
            if enemyY[i] == 520:
                enemyY_change[i] = -0.5
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"


            crash_Sound = mixer.Sound("crashing.wav")
            crash_Sound.play()
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(0,150)
            score_value += 1
            print(score_value) 
        enemy_1(enemyX[i], enemyY[i], i)
        
    # Bullet Movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state in "Fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
       

    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
