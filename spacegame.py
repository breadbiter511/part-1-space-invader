import pygame
import os

pygame.init()
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space invaders game")
velocity = 5
fps = 60
bullet_velcoity = 5

bg = pygame.transform.scale(pygame.image.load(os.path.join("space invader/bg.png")),(WIDTH,HEIGHT))
ship_y = pygame.image.load(os.path.join("space invader/yellowship.png"))
yellow_ship = pygame.transform.rotate(pygame.transform.scale(ship_y,(60,40)),90)
ship_r = pygame.image.load(os.path.join("space invader/redship.png"))
red_ship = pygame.transform.rotate(pygame.transform.scale(ship_r,(60,40)),270)

def draw_window(yellow,red,yellow_bullet,red_bullet):
    screen.blit(bg,(0,0))
    screen.blit(yellow_ship,(yellow.x,yellow.y))
    screen.blit(red_ship,(red.x,red.y))
    for i in red_bullet:
       pygame.draw.rect(screen,"red",i)
    for i in yellow_bullet:
       pygame.draw.rect(screen,"yellow",i)
    pygame.display.update()


def red_ship_move (keypress,red):
    if keypress [pygame.K_LEFT]:
      red.x -= 1
    if keypress [pygame.K_RIGHT]:
      red.x += 1
    if keypress [pygame.K_UP]:
      red.y -= 1
    if keypress [pygame.K_DOWN]:
      red.y += 1

def yellow_ship_move (keypress,yellow):
    if keypress [pygame.K_a]:
      yellow.x -= 1
    if keypress [pygame.K_d]:
      yellow.x += 1
    if keypress [pygame.K_w]:
      yellow.y -= 1
    if keypress [pygame.K_s]:
      yellow.y += 1


def main():
  yellow = pygame.Rect(100,300,60,60)
  red = pygame.Rect(900,300,60,60)
  red_bullet = []
  yellow_bullet = []
  while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    keypress = pygame.key.get_pressed()
    red_ship_move(keypress,red)
    yellow_ship_move(keypress,yellow)
    draw_window(yellow,red,yellow_bullet,red_bullet)     
main()



    
    
   
       


if __name__ == "__main__":
    main()




                                                           
                                                           