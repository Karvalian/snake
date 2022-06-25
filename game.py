#!/usr/bin/env python3
import pygame
from pygame.locals import *
import random
import time
WIDTH = 900
HEIGHT = 640

pygame.init()
# DID SOME MINOR WORK OFF STREAM JUST TO FIX MOVEMENTS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
speed = 0.1
running = True
bruh = (255, 0, 255)
snake = pygame.image.load("test.png")
snake = pygame.transform.scale(snake, (25, 25))
rect = snake.get_rect()
rect.x = 900//2
rect.y = 640//2
food = pygame.image.load("test.png")
food = pygame.transform.scale(food, (25,25))
foodrect = food.get_rect()

foodrect.x = random.randint(0,900-25)
foodrect.y = random.randint(0,640-25)
score = 0
font = pygame.font.SysFont('droidsansmono', 32)
lastkey = 0
clock = pygame.time.Clock()
while running:
  dt = clock.tick(60)

  random.seed(time.time())
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
    if event.type == pygame.KEYDOWN:
      lastkey = event.key
  if(lastkey == K_d):
    rect.x += speed*dt
  if(lastkey == K_a):
    rect.x -= speed*dt
  if(lastkey == K_w):
    rect.y-=speed*dt
  if(lastkey == K_s):
    rect.y+=speed*dt
  rect.clamp_ip(screen.get_rect())
  if rect.colliderect(foodrect):
    foodrect.x = random.randint(0,900-25)
    foodrect.y = random.randint(0,640-25)
    speed+=0.1
    score+=1
    
  screen.fill(bruh)
  screen.blit(snake, (rect.x,rect.y))
  text = font.render(str("Score: " + str(score)).encode(), True, ((255,255,0)))
  screen.blit(text, (0, 0))
  if(foodrect.x!=-1):
    screen.blit(food, (foodrect.x, foodrect.y))
  pygame.display.flip()


