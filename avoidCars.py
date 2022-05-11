import pgzrun
from random import *


WIDTH = 1400
HEIGHT = 800
#Impostare il comando per posizionare la finestra al centro#
import time
score = 0

game_over = False

sfondo = Actor("sfondo")
sfondo.pos = 0,0 

car = Actor("auto1")
car.pos = 700,675


def time_up():
    global game_over
    game_over = True


def draw():

    screen.clear()
    screen.fill("dimgray")
    car.draw()

    screen.draw.text("Score: " + str(score), color="white", topleft=(10,10), fontsize = 40)

    if game_over:
        screen.fill("pink")
        screen.draw.text("Punteggio finale: " + str(score), topleft=(10,10), fontsize = 60)



def update():

    global score


    if keyboard.left:
        car.x = car.x - 5
    elif keyboard.right:
        car.x = car.x + 5
    elif keyboard.up:
        car.y = car.y - 0
    elif keyboard.down:
        car.y = car.y + 0

clock.schedule(time_up,30.0)

pgzrun.go()