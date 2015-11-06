import pygame, sys, os, time, glob, random, noise
from pygame.locals import *

width  = 800
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))
fpsClock = pygame.time.Clock()

#colours    R    G    B
seaBlue = (050, 154, 255)

pygame.display.set_caption('Evolution')
characterright = pygame.image.load('images/sprites/rlevel0.png')
characterleft  = pygame.image.load('images/sprites/llevel0.png')
character = characterleft
cx = 50
cy = 50
speed = 4
direction = 'none'
healthbar = pygame.image.load('images/sprites/healthbar.png')
down = False
up = False
left = False
right = False

health = 20

fishlist = []
for fish in glob.glob('images/sprites/fish/*'):
    for i in range(int(fish[21])):
        fishlist.append(pygame.image.load(fish))

fishInSea = []

luckiestGuy = pygame.font.Font('fonts/LuckiestGuy.ttf', 100)

def spawn_fish():
    fish = fishlist[random.randint(0, len(fishlist) - 1)]
    fishInSea.append([fish, width + 100, random.randint(50, height-50), random.randint(2, 10), str(fish)[9:-8].split('x')])

def draw_fish():
    for fish in fishInSea:
        screen.blit(fish[0], (fish[1], fish[2]))

def draw_health_bar():
    pygame.draw.rect(screen, (147, 227, 18), (11, 11, (3.28*health), 35))

def move_fish():
    global health
    i = 0
    for fish in fishInSea:
        fish[1] -= fish[3]
        if fish[1] <= -100:
            fishInSea.pop(i)
            spawn_fish()
        characterdimensions = str(character)[9:-8].split('x')
        stop = False
        for x in range(cx, cx + int(characterdimensions[0])):
            if stop:
                break
            elif x in range(fish[1], fish[1] + int(fish[4][0])):
                for y in range(cy, cy + int(characterdimensions[1])):
                    if y in range(fish[2], fish[2] + int(fish[4][1])):
                        fishInSea.pop(i)
                        spawn_fish()
                        if fish[4] == ['142', '34']:
                            health -= 10
                        elif fish[4] == ['46', '34']:
                            health += 5
                        elif fish[4] == ['140', '88']:
                            health += 1
                        if health > 100:
                            health = 100
                        stop = True
                        break
        i += 1

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

def check_quit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

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
    draw_fish()
    move_fish()

for i in range(6):
    spawn_fish()

def timer(initialtime,timelimit):
    now = time.strftime('%H/%M/%s').split('/')
    value = True
    for i in range(3)
        if now[i] - initialtime[i] == timelimit[i]:
            value = False
        else:
            value = True
    return value


def game_over():
    screen.fill((43, 43, 43))
    text = luckiestGuy.render('GAME OVER!', False, (255, 255, 255))
    textPos = text.get_rect()
    textPos.center = (width/2, height/2)
    screen.blit(text, textPos)

startTime = time.strftime('%H/%M/%s').split('/')
while True:
    if timer(startTime, 3, 2):
        if health > 0:
            ocean()
            draw_health_bar()
            screen.blit(healthbar, (10, 10))
        else:
            game_over()
            check_quit()
    pygame.display.update()
    fpsClock.tick(30)
