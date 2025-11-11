import pygame as pg
import random as r
import time as t

pg.init()

pg.display.set_caption("Hiru - Flappy Bird")
screen = pg.display.set_mode((800,800))

clock = pg.time.Clock()
score = 0

green = (0, 255, 0)
light_blue = (0, 200, 207)
black = (0,0,0)
blue = (0,0,255)
red = (168, 13, 13)
dark_red = (99, 7, 7)
end_red = (255, 0, 0)
green = (0,255,0)
brown = (133, 82, 0)
white = (255, 255, 255)
yellow = (250, 210, 35)
font=pg.font.Font(None,75)
endfont=pg.font.SysFont("Calibri",100)

endscreen = pg.image.load("Hiru - Endscreen.png")
birdimg = pg.image.load("bird.png")
titlescreen = pg.image.load("titleScreen.png")

bird = pg.Rect(100,300,175,100)
top_pipe = pg.Rect(600,0,100,200)
bot_pipe = pg.Rect(600,600,100,800)

state = 0
clear_endscreen = pg.image.load("clearEnd.png")

# mouse character
mouse = pg.Rect(0,0,10,10)

def play_game():
    global state
    global score

    bird[0] = 100
    bird[1] = 300
    top_pipe[0] = 600
    bot_pipe[0] = 600
    top_pipe[1] = 0
    bot_pipe[1] = 600
    top_pipe[2] = 100
    bot_pipe[2] = 100
    top_pipe[3] = 200
    bot_pipe[3] = 800
    score = 0

    while state == 1:
        pg.event.pump()

        L,M,R = pg.mouse.get_pressed()
        screen.fill(light_blue)

        top_pipe_height = r.randint(10, 500)
        bot_pipe_height = (top_pipe_height + 300)

        pg.draw.ellipse(screen, light_blue, bird)
        pg.draw.rect(screen, green, top_pipe)
        pg.draw.rect(screen, green, bot_pipe)

        # move pipes
        top_pipe[0] -= 10
        bot_pipe[0] -= 10

        # always move bird down
        bird[1] += 5

        # when clicked, move bird up
        if L == True:
            bird[1] -= 20

        # spawn new pipes once pipes have passed
        if top_pipe[0] and bot_pipe[0] <= -100:
            top_pipe[0] = 800
            bot_pipe[0] = 800

            top_pipe[3] = top_pipe_height
            bot_pipe[1] = bot_pipe_height

            pg.draw.rect(screen, green, top_pipe)
            pg.draw.rect(screen, green, bot_pipe)

            score += 1

        # collision
        if bird.colliderect(top_pipe) or bird.colliderect(bot_pipe) or bird[1] >= 800 or bird[1] <= 0:
            state = 2

        screen.blit(birdimg, (bird[0] - 50, bird[1] - 10))

        scoretext = font.render("Score: " + str(score), True, white)
        screen.blit(scoretext, (0, 0))
        pg.display.flip()
        clock.tick(60)

def start_screen():
    global state
    while state == 0:
        pg.event.pump()

        L,M,R = pg.mouse.get_pressed()
        if L == 1:
            state = 1

        screen.fill(white)
        screen.blit(titlescreen, (0,0))
        startText = font.render("Click To Start", True, black)

        screen.blit(startText, (200, 500))
        pg.display.flip()
        clock.tick(60)

def end_screen():
    global score
    global state
    while state == 2:
        pg.event.pump()

        L,M,R = pg.mouse.get_pressed()
        endscoretext = endfont.render(str(score), True, end_red)

        screen.fill(black)
        screen.blit(endscreen, (0,0))
        screen.blit(endscoretext, (500, 325))

        if L == 1:
            state = 1

        if R == 1:
            state = 0

        pg.display.flip()
        clock.tick(60)

while True:
    if state == 0:
        start_screen()

    if state == 1:
        play_game()

    if state == 2:
        end_screen()
