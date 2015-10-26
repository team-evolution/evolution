import pygame, sys, os, time, glob
from pygame.locals import *

width  = 800
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))

#colours    R    G    B
seaBlue = (050, 154, 255)

pygame.display.set_caption('Evolution')
characterright = pygame.image.load('images/sprites/rlevel0.png')
characterleft  = pygame.image.load('images/sprites/llevel0.png')
character = characterleft
cx = 50
cy = 50
speed = 2
direction = 'none'
healthbar = pygame.image.load('images/sprites/healthbar.png')
down = False
up = False
left = False
right = False

fishlist = {}
for fish in glob.glob('images/sprites/fish/*'):
    fishlist[fish[20:-4]] = pygame.image.load(fish)
print fishlist

#def spawnfish():


def move_left():
    global cx, character
    cx -= speed
    character = characterleft

def move_right():
    global cx, character
    cx += speed
    character = characterright

def move_up():
    global cy
    cy -= speed

def move_down():
    global cy
    cy += speed

def check_all_events():
    global up, down, left, right, cy, cx, character
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_DOWN:
                down = False
            if event.key == K_UP:
                up = False
            if event.key == K_LEFT:
                left = False
            if event.key == K_RIGHT:
                right = False
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                down = True
            if event.key == K_UP:
                up = True
            if event.key == K_LEFT:
                left = True
            if event.key == K_RIGHT:
                right = True

def ocean():
    global up, down, left, right, cy, cx, character
    screen.fill(seaBlue)
    check_all_events()
    if down:
        move_down()
    if up:
        move_up()
    if left:
        move_left()
    if right:
        move_right()
    screen.blit(character, (cx, cy))


while True:
    ocean()
    screen.blit(healthbar, (10, 10))
    pygame.display.update()

hungerbar = pygame.image.load('images/sprites/healthbar.png')
while True:
    ocean()
    screen.blit(hungerbar, (5, 5))
    pygame.display.update()
