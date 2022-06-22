from msilib import CAB
import os
import time
import pygame
from map import *

pygame.init()

# color
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
sky_blue = (135, 206, 250)
light_blue = (155, 155, 255)


font = pygame.font.Font(None, 25)
MsmllArial = pygame.font.SysFont('Arial', 30)
smllArial = pygame.font.SysFont('Arial', 20)
Arial = pygame.font.SysFont('Arial', 35)

width = map.width
height = map.height
cooldown = 0
jump = False
colide = False
colide1, colide2, colide3, colide_end = False, False, False, False

# Create the clock object
clock = pygame.time.Clock()
logo = pygame.image.load("assets/Nytron.png")
playerlgo = pygame.image.load("assets/Player.png")
win = pygame.display.set_mode((width, height))
screen = win
pygame.display.set_caption("Nytron Alpha", map.version)
pygame.display.set_icon(logo)


class Player:
    def __init__(self) -> None:
        self.x = width/2
        self.y = height/2
        self.speedx = 0
        self.xvel = 1.5
        self.yvel = 5
        self.grav_vel = 0.5
        self.size = 64
        self.bottom = 656.5
        self.level = 1
        self.completed = False

    def gravity(self):
        global colide
        if self.y <= height - player.size and colide == False:
            self.y += self.grav_vel
        else:
            colide = True


player = Player()


playerIcon = pygame.transform.scale(playerlgo, (player.size, player.size))

run = True
movey = 0
movex = 0
movey2 = 0
while run:
    win.fill(sky_blue)
    framerate = round(clock.get_fps(), 1)
    # un-limit framerate
    if framerate <= 120:
        clock.tick(120)
    else:
        clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if cooldown == 0:
                if player.y == player.bottom or colide == True:
                    movey = 1
                    cooldown = 100

        if keys[pygame.K_LEFT]:
            movex = -1
        elif keys[pygame.K_RIGHT]:
            movex = 1
        else:
            movex = 0

    if movex == 1 and player.x < width - player.size:
        player.x += player.xvel
    elif movex == -1 and player.x > 0:
        player.x -= player.xvel
    if movey == 1 and cooldown >= 50:
        player.y -= player.yvel
    if player.y == player.bottom:

        movey = 0
        movey2 = 0

    if player.y <= -3000:
        player.y = player.bottom
        movey = 0
        movey2 = 0

    def button(self, x, y, szey, szex, Color, text, hover_color, name):
        player.completed = True
        color = Color
        mouse_pos = pygame.mouse.get_pos()

        # print(mouse_pos)
        mousex = mouse_pos[0]
        mousey = mouse_pos[1]
        if mousex >= x and mousex <= (x + szex):
            if mousey >= y and mousey <= (y + szey):
                color = hover_color

                if pygame.mouse.get_pressed() == (True, False, False):
                    color = (255, 255, 255)
                    player.completed = False
                    player.level += 1

        rect = pygame.draw.rect(screen, color, (x, y, szex, szey))
        pygame.draw.rect(screen, color, rect)
        words = MsmllArial.render(str(text), True, black)
        screen.blit(words, (x+17, y+7.2))
        return player.completed
        

    def tile(self, x, y, szey, szex, color):
        global colide1
        # print(mouse_pos)
        mousex = player.x + player.size/2
        mousey = player.y + player.size
        if mousex >= x and mousex <= (x + szex):
            if mousey >= y and mousey <= (y + szey):
                colide1 = True
            else:
                colide1 = False
        else:
            colid1e = False
        pygame.draw.rect(screen, color, pygame.draw.rect(
            screen, color, (x, y, szex, szey)))

    def tile2(self, x, y, szey, szex, color):
        global colide2
        # print(mouse_pos)
        mousex = player.x + player.size/2
        mousey = player.y + player.size
        if mousex >= x and mousex <= (x + szex):
            if mousey >= y and mousey <= (y + szey):
                colide2 = True
            else:
                colide2 = False
        else:
            colide2 = False
        pygame.draw.rect(screen, color, pygame.draw.rect(
            screen, color, (x, y, szex, szey)))

    def tile3(self, x, y, szey, szex, color):
        global colide3
        # print(mouse_pos)
        mousex = player.x + player.size/2
        mousey = player.y + player.size
        if mousex >= x and mousex <= (x + szex):
            if mousey >= y and mousey <= (y + szey):
                colide3 = True
            else:
                colide3 = False
        else:
            colide3 = False
        pygame.draw.rect(screen, color, pygame.draw.rect(
            screen, color, (x, y, szex, szey)))

    def end(self, x, y, szey, szex, color):
        global colide_end
        # print(mouse_pos)
        mousex = player.x + player.size/2
        mousey = player.y + player.size
        if mousex >= x and mousex <= (x + szex):
            if mousey >= y and mousey <= (y + szey):
                colide_end = True
            else:
                colide_end = False
        else:
            colide_end = False
        pygame.draw.rect(screen, color, pygame.draw.rect(
            screen, color, (x, y, szex, szey)))

    if colide1 or colide2 or colide3 or colide_end:
        colide = True
    else:
        colide = False

    tile(win, 200, height - 200 - 10, 30, 30*3, red)
    tile2(win, 450, height - 200 - 10, 30, 30*3, red)
    tile3(win, 900, height - 200 - 10, 30, 30*3, red)
    end(win, width - 30*3 - 10, height - 300 - 10, 30, 30*3, green)

    if colide_end or player.completed:
        win.blit(font.render("Level Complete", True, white),
                 (width/2 - 100, height/2))
        player.completed = True
        button(win, width/2 - 100, height/2 + 50, 200,
               50, green, "Next Level", green, "next")

    if cooldown != 0:
        cooldown -= 1

    elif colide == True:
        cooldown = 0

    win.blit(font.render("FPS: {}".format(framerate),
             True, white), (width-100, height-30))

    player.gravity()
    #pygame.draw.rect(win, blue, pygame.Rect(player.x, player.y, player.size, player.size))
    win.blit(playerIcon, (player.x, player.y))
    print('(', player.x, ',', player.y, ')', cooldown, colide, player.level)

    if colide_end or player.completed:
        win.fill(black)
        win.blit(font.render("Level Complete", True, white),(width/2 - 100, height/2))
        player.completed = button(win, width/2 - 100, height/2 + 50, 50, 175, green, "Next Level", (25,255,75), "next")

    win.blit(font.render("FPS: {}".format(framerate),True, white), (width-100, height-30))
    pygame.display.update()

pygame.quit()
