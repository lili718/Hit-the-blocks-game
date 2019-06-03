#Lia Johnson
#Lej42
#CS 172 HW3
#5/17/19
# This file contains the main script


import pygame
from ball import ball
from block import block
from text import text

#define intersection
def intersect(rect1, rect2) :
 if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y) :
     return True
 return False

#initialize pygame
pygame.init()

#set up screen
size = [600,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('CS 172 HW3: Block Game')

#ball
b = ball(50,385, True)

#blocks
blks =[]
#add blocks to list
for i in range(0,9):
    blks.append(block(0,0,True))

#set x and y for each block
blks[0].set_x(400)
blks[0].set_y(340)

blks[1].set_x(420)
blks[1].set_y(340)

blks[2].set_x(440)
blks[2].set_y(340)

blks[3].set_x(400)
blks[3].set_y(360)

blks[4].set_x(420)
blks[4].set_y(360)

blks[5].set_x(440)
blks[5].set_y(360)

blks[6].set_x(400)
blks[6].set_y(380)

blks[7].set_x(420)
blks[7].set_y(380)

blks[8].set_x(440)
blks[8].set_y(380)

#score
rScore = 0
score = text(10, 10, True, "Score: " + str(rScore))

#reset message
message = text(10, 450, True, "Press \"R\" to reset the ball")

#physics variables
xv = 0
yv = 0
dt = 0.1
g = 6.67
R = 0.7
eta = 0.5          

#while loop
running = True
while running:
    for event in pygame.event.get():
        #exit
        if event.type == pygame.QUIT:
            exit()
        
        #reset ball position if r is hit
        if event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_r:
            xv = 0
            yv = 0
            b.set_x(50)
            b.set_y(385)
        
        #get final position of mouse after it has been released
        if event.type == pygame.MOUSEBUTTONDOWN:
            mFinalx, mFinaly = pygame.mouse.get_pos()
    
        #get initial position of mouse when it is clicked. Set initial x and y velocities
        if event.type == pygame.MOUSEBUTTONUP:
            mInitx, mInity = pygame.mouse.get_pos()
            xv = mFinalx - mInitx
            yv = -1*(mFinaly - mInity)
    
    #set screen color
    screen.fill((255,255,255))
    
    # draw objects to screen
    pygame.draw.line(screen, (0,0,0), (0,400), (600,400), 3)
    b.draw(screen)
    score.draw(screen)
    message.draw(screen)
    for blk in blks:
        #if visible is true draw block to screen
        if blk.get_vis():
            blk.draw(screen)
        
        #if ball hits block, set visible to false, remove from list and add pts to score
        if intersect(b.get_rect(),blk.get_rect()):
            blk.set_vis(False)
            blks.remove(blk)
            rScore += 1
            score = text(10, 10, True, "Score: " + str(rScore))
            #print("hello")
    
    #increase x-coord, decrease y-coord
    b.set_x(b.get_x()+xv*dt)
    b.set_y(b.get_y()-yv*dt)
    
    #if ball hits ground reverse y-velocity and reduce x-velocity
    if b.get_y() > 400:
        yv = -R * yv
        xv = eta * xv
    
    #regular y velocity
    else:
        yv = yv - g * dt
    
    #update screen
    pygame.display.update()
    
