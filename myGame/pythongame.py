

#  Name : حماده السيد محمد سليم
#  ID   : 621224


# Create a game interface
from pickle import TRUE
from turtle import speed, width
import pygame # call the libraryه
from ob import Player # call the player
from ob import Road # call the street
from ob import Tree
from ob import Pr
import random


pygame.init() # library ready
SCREEN = WIDTH , HEIGHT = 288 ,  521 
win = pygame.display.set_mode(SCREEN) # creat display


clock = pygame.time.Clock()
FPS = 10


# --------------------------  coller ----------------------------------#

BLUE = (30,144,255)  # varabile constant


# -------------------------- call same image ---------------------------#

home_img = pygame.image.load('Assets/home.png') # background pictures   

bg =  pygame.image.load('Assets/bg.png') 

road = pygame.image.load('Assets/road.png') 

road = pygame.transform.scale(road,(WIDTH-60,HEIGHT))

p = Player (100,HEIGHT-120,0) #call player 
movo_left = False 
move_right = False

road = Road() # object call class road

speed = 1.2 # Street speed


# call Trees
tree_group = pygame.sprite.Group() 
Pr_group = pygame.sprite.Group()



# add some variable ----------> 

home_page = False

game_page = True

counter = 0




running = True  

while running : # loop of screen on
    
    win.fill(BLUE) 

    for event in pygame.event.get(): # add event --> حدث
       
        if event.type == pygame.QUIT: # tern off
       
            running = False  # off
        
        #  tern off by { q }

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:

                running = False
       
        # Mouse control
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if x< WIDTH //2:
                movo_left = TRUE
            else:
                move_right = True
      
        
        if event.type == pygame.MOUSEBUTTONUP:
            movo_left = False
            move_right = False




    #win.blit(home_img,(0,0)) # جلب صوره وضعها كخلفيه

    if home_page:

        win.blit(home_img,(0,0))

    if game_page:

        win.blit(bg,(0,0))
        road.updatd(speed)
        road.draw(win)
        



        counter += 1
        if counter %60 == 0 :
            tree = Tree(random.choice([-5, WIDTH-35]),-20)
            tree_group.add(tree)
            
        tree_group.update(speed)
        tree_group.draw(win)   
        if counter %90 == 0:
            obs = random.choices([1,2,3],weights=[6,2,2],k=1)[0] 
            obee = Pr(obs)
            Pr_group.add(obee)
            
        Pr_group.update(speed)
        Pr_group.draw(win)





    # add player -->
    p.draw(win) #  player on  screen
    
    p.update(movo_left,move_right) # add a movement



    pygame.display.update()

pygame.quit() # cloase game

