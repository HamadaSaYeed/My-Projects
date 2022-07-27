
from email.mime import image
import pygame 
import random


SCREEN = WIDTH , HEIGHT = 288 ,  521

lan_pos = [50,95,142,90]

class Player:
    def __init__(self,x,y,type):
        
        self.image = pygame.image.load(f'Assets/cars/{type+8}.png')
        self.image = pygame.transform.scale(self.image,(55,85)) # size player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #  move player

    def update (self,left,right):
        if left:
            self.rect.x -=1
            if self.rect.x <=45:
                self.rect.x = 45
        if right:
            self.rect.x +=1
            if self.rect.right >=250:
                self.rect.right = 250
    # Add  player to  interface
    def draw(self,win):
        win.blit(self.image,self.rect)            


class Road:
    def __init__(self):
        #  cal image
        self.image = pygame.image.load('Assets/road.png')     
        self.image = pygame.transform.scale(self.image,(WIDTH-60,HEIGHT))
        # add mov variable 
        self.move = True
        self.reset() 
    
    def reset(self):
        self.x=30
        self.y1=0
        self.y2= -HEIGHT
    def updatd(self,speed):
        if self.move:
            self.y1 += speed
            self.y2 += speed
        if self.y1 >= HEIGHT:
            self.y1 = -HEIGHT
        if self.y2 >= HEIGHT:
            self.y2 = -HEIGHT    
    # add image to screen
    def draw (self,win):
        win.blit(self.image,(self.x,self.y1))        
        win.blit(self.image,(self.x,self.y2))   


# add tree to game

class Tree(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super(Tree,self).__init__()
        type = random.randint(1,4)# random  
        #add images for tree          
        self.image = pygame.image.load(f'Assets/trees/{type}.png')
        # x , y  ابعاد الصوره
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, speed):
    
        self.rect.y += speed   # remove tree
        if self.rect.y >= HEIGHT:
            self.kill()

    # add tree to screen
    def draw (self,win):
        win.blit(self.image,self.rect) 



class Pr(pygame.sprite.Sprite):
    def __init__(self, type):
        super(Pr,self).__init__()
        dx = 0  
        # add varible   
        self.type = type
      
        if type == 1:
            ctype=random.randint(2,8)
           
            self.image = pygame.image.load(f'Assets/cars/{ctype}.png')
            self.image = pygame.transform.flip(self.image,False,True)
            self.image = pygame.transform.scale(self.image,(48,82))
        if type == 2:
            self.image = pygame.image.load('Assets/barrel.png')
            self.image = pygame.transform.scale(self.image,(24,36))
            dx = 10
        if type == 3:
            self.image = pygame.image.load('Assets/roadblock.png')
            self.image = pygame.transform.scale(self.image,(50,25))  
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(lan_pos)+ dx
        self.rect.y = -100
    def update(self, speed):
        self.rect.y += speed
        self.mask = pygame.mask.from_surface(self.image)
    def draw(self,win):
        win.blit(self.image,self.rect)    
