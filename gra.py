import random

import pgzrun

from pgzero.keyboard import keyboard

from pgzhelper import *

WIDTH = 800
HEIGHT = 600
background_image = "background.png"
backgrounds = []
BACKG = Actor(background_image)
backgrounds.append(BACKG)
BACKG.scale = 1
BACKG.x = 400
BACKG.y = 300
BACKG = Actor(background_image)
BACKG.scale = 1
BACKG.x = -550
BACKG.y = 300
backgrounds.append(BACKG)

ship = Actor('ship.png')
ship.x = 100
ship.y = 300
ship.scale = 1.5

velocity_x = 0
velocity_y = 0
gravity = 0

obstacles = []
obstacles_timeout = 0

score = 0
game_over = False

def update():
    global velocity_y, velocity_x, obstacles_timeout, score, game_over

    if not game_over:

        obstacles_timeout += 1
        if obstacles_timeout > random.randint(15, 60):
            rocks = ['rock.png', 'rock2.png', 'rock3.png', 'rock4.png']
            meteors = Actor(rocks[random.randint(0, 3)])
            meteors.x = 850
            meteors.y = random.randint(0, 600)
            meteors.scale = 2
            obstacles.append(meteors)
            obstacles_timeout = 0

        for meteors in obstacles:
            meteors.x -= 8
            if meteors.x < -10:
                obstacles.remove(meteors)
                score += 1


        if keyboard.up:
            if velocity_y > -3.5:
                velocity_y -= 0.25
        if keyboard.down:
            if velocity_y < 3.5:
                velocity_y += 0.25
        if keyboard.left:
            if velocity_x > -3.5:
                velocity_x -= 0.25
        if keyboard.right:
            if velocity_x < 3.5:
                velocity_x += 0.25

        ship.y += velocity_y
        ship.x += velocity_x
        if velocity_y < 0:
            velocity_y += 0.05
        if velocity_y > 0:
            velocity_y -= 0.05
        if velocity_x < 0:
            velocity_x += 0.05
        if velocity_x > 0:
            velocity_x -= 0.05


        if ship.collidelist(obstacles) != -1:
            game_over = True

def draw():

    for BACKG in backgrounds:
        BACKG.draw()

    screen.draw.text('Made by: Mateusz Bandura', (15, 580), color=(255, 255, 255), fontsize=15)

    if game_over:
        screen.draw.text('You lost!!!', centerx=400, centery=250, color=(255, 255, 255), fontsize=65)
        screen.draw.text('Score: ' + str(score), centerx=400, centery=325, color=(255, 255, 255), fontsize=45)

    else:
        ship.draw()
        for meteors in obstacles:
            meteors.draw()
        screen.draw.text('Score: ' + str(score), (15, 10), color=(171, 186, 214), fontsize=35)


pgzrun.go()
