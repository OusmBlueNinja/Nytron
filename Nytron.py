from msilib import CAB
import os,time, pygame

pygame.init()

#color
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
sky_blue = (135, 206, 250)


font = pygame.font.Font(None, 25)

width = 1280
height = 720
cooldown = 0
jump = False

# Create the clock object
clock = pygame.time.Clock()
logo = pygame.image.load("assets/Nytron.png")
playerlgo = pygame.image.load("assets/Player.png")
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Nytron Alpha 000.000.003")
pygame.display.set_icon(logo)



class Player:
  def __init__(self) -> None:
    self.x = width/2
    self.y = height/2
    self.speedx = 0
    self.xvel = 1.5
    self.yvel = 3
    self.grav_vel = 0.5
    self.size = 64
    self.bottom = 656.5
  
  def gravity(self):
    if self.y <= height - player.size:
      self.y += self.grav_vel

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
            if player.y == player.bottom:
              movey = 1
              cooldown = 300
              jump = True
    
        if keys[pygame.K_LEFT]:
            movex = -1
        elif keys[pygame.K_RIGHT]:
            movex = 1
        else:
          movex = 0
        
        if player.x == -0.5:
          if keys[pygame.K_UP]:
            movey2 = 1
            can_jump = False
      
          
        
        
    
    if movex == 1 and player.x < width - player.size:
      player.x += player.xvel
    elif movex == -1 and player.x > 0:
      player.x -= player.xvel
    if movey == 1 and cooldown >= 200:
      player.y -= player.yvel
      can_jump = False
    if movey2 == 1:
      player.y -= player.yvel
    if player.y == player.bottom:
      jump = False
      movey = 0
      movey2 = 0
      

    
    
    
        
        
    
          
    if cooldown != 0:
      cooldown -= 1   

    win.blit(font.render("FPS: {}".format(framerate), True, white), (width-100, height-30))
    
    
    player.gravity()
    #pygame.draw.rect(win, blue, pygame.Rect(player.x, player.y, player.size, player.size))
    win.blit(playerIcon, (player.x, player.y))
    print('(', player.x, ',', player.y, ')', cooldown)
    pygame.display.update()

pygame.quit()