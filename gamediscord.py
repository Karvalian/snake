# put the webhooks link in the url column

#!/usr/bin/env python3
import pygame
from pygame.locals import *
import random
import time
import requests
WIDTH = 900
HEIGHT = 640

username = input("Enter your username: ")
speed = float(input("Enter the speed: "))
URL = 'put it here'
pygame.init()


# DID SOME MINOR WORK OFF STREAM JUST TO FIX MOVEMENTS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#speed = float(input("Enter speed: "))
running = True
bruh = (0,0,0)
snake = pygame.image.load("snake.png")
snake = pygame.transform.scale(snake, (35, 35))
rect = snake.get_rect()
rect.x = 900//2
rect.y = 640//2
food = pygame.image.load("food.png")
food = pygame.transform.scale(food, (35, 35))
foodrect = food.get_rect()

foodrect.x = random.randint(0,900-35)
foodrect.y = random.randint(0,640-35)
score = 0
font = pygame.font.SysFont('sfmono', 32)
lastkey = 0
clock = pygame.time.Clock()

while running:
  dt = clock.tick(60)
  random.seed(time.time())
  keys = [K_d, K_a, K_w, K_s]
  pause = font.render(str("Paused"), True, ((255, 255,0)))
  over = font.render(str("Game Over"), True, ((255, 255,0)))
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
    if event.type == pygame.KEYDOWN:
      lastkey = event.key

  screenrect = screen.get_rect()
  if(lastkey == K_d):
    rect.x += speed*dt
  elif(lastkey == K_a):
    rect.x -= speed*dt
  elif(lastkey == K_w):
    rect.y-= speed*dt
  elif(lastkey == K_s):
    rect.y+= speed*dt
  if not screenrect.contains(rect):
    lastkey = K_l
    data = {
        'content': f'Game Over, Username : {username}, MaxSpeed : {speed}  Score : {score} ',
    }
    rect.x = WIDTH//2
    rect.y = HEIGHT//2
    if(score>0):
      requests.post(url=URL, data=data)
    score = 0
    rect.clamp_ip(screen.get_rect())
  if rect.colliderect(foodrect):
    foodrect.x = random.randint(0,900-35)
    foodrect.y = random.randint(0,640-35)
    speed+=0.0001
    score+=1
  screen.fill(bruh)
  screen.blit(snake, (rect.x,rect.y))
  text = font.render(str("Score: " + str(score)).encode(), True, ((255,255,0)))
  text2 = font.render(str("Made by Karvalian"), True, ((255,255,0)))
  if(lastkey==K_q):
    running = False
  elif((lastkey not in keys) & (lastkey!=K_l)):
    screen.blit(pause, (300, 0))
  elif(lastkey==K_l):
    screen.blit(over, (300, 0))

  screen.blit(text, (0, 0))
  screen.blit(text2, (550, 0))
  if(foodrect.x!=-1):
    screen.blit(food, (foodrect.x, foodrect.y))
  pygame.display.flip()
