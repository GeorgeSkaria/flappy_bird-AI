import pygame
import neat
import time
import os
import random

WIN_WIDTH=600
WIN_HEIGHT=800

BIRD_IMGS=[pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird1.png")))
           ,pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird2.png"))),
           pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird3.png")))]

PIPE_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("images","pipe.png")))
BASE_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("images","base.png")))
BG_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("images","bg.png")))

class Bird:
  IMGS=BIRD_IMGS
  MAX_ROTATION=25
  ROT_VELOCITY=20
  ANIMATION_TIME=5

  def __init__(self,x,y):
    self.x=x
    self.y=y
    self.tilt=0
    self.tick_count=0 #How many times we have moved, since the last jump
    self.vel=0
    self.height=self.y
    self.img_count=0
    self.img=self.IMGS[0]

  def jump(self):
    self.vel=-10.5 #Origin of the screen is the top left corner
    self.tick_count=0
    self.height=self.y

  def move(self):
    self.tick_count+=1

while True:
  bird.move()


    


