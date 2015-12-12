# -*- coding: utf-8 -*-
# 1 - Import library
import pygame
from pygame.locals import *
import random

# 2 - Initialize the game
pygame.init()
# 2.1 - show the picture
width,height = 640,640
screen = pygame.display.set_mode((width, height))
# 2.2 - record the keys to be touched
#playerpos = [[10,6],[10,9],[10,12]]
keys = [False, False, False, False]
# 2.3 -



# 2. - gameover
gameover = False  
score = 0


#direction control
turnRight = 0
turnLeft = 0
turnUp = 0
turnDown = 0
lastTurnRight = 0
lastTurnLeft = 0
lastTurnUp = 0
lastTurnDown = 0
running = 1



# 3 - Load images
playerimg1 = pygame.image.load("hi/lan.png")
playerimg = playerimg1
apple1 = pygame.image.load("hi/kai.png")
apple2 = pygame.image.load("hi/qiang.png")
apple3 = pygame.image.load("hi/xian.png")
apples = [apple1, apple2, apple3]
appleloc = [120,120]
appleimg = 1
grass = pygame.image.load("hi/grass.png")
heiyi1 = pygame.image.load("hi/heiyi1.png")
heiyi2 = pygame.image.load("hi/heiyi2.png")
tong1 = pygame.image.load("hi/tong1.png")
tong2 = pygame.image.load("hi/tong2.png")
gameover = pygame.image.load("hi/gameover.png")
players = [[10+3*playerimg.get_height(),320],[10+2*playerimg.get_height(),320],[10+playerimg.get_height(),320],[10,320]]
#BALLBALL
heiyi1s = [[230,100], [250,100], [270,100], [290,100], [310,100], [330,100]]
heiyi2s = [[490,240], [490,290], [459,340], [428,340], [397,340], [366,340], [335,340]]
tong2s = [[150,340], [150,395], [150,450], [150, 505]]
tong1s = [[360, 560], [360, 535], [360, 505], [342, 505], [324, 505], [378, 505], [396, 505], [414, 505]]
#BALLBALLBALLBaLLBALLBALLBALLBALLBALL

# 3.1 - Load audio
eat = pygame.mixer.Sound('hey/perfect.wav')
pygame.mixer.music.load('hey/run.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.15)
eat.set_volume(0.55)

# 4 - keep looping through

while running:
	# 5 - clear the screen before drawing it again
    screen.fill(0)
    # # 6 - draw the screen elements
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*grass.get_width(),y*grass.get_height()))
    #if randomapple == 1:
        #screen.blit(apple1,(120,120))
    #elif randomapple == 2:
        #screen.blit(apple2,(120,120))
    #elif randomapple == 3:
        #screen.blit(apple3,(120,120))
    
    # screen.blit(heiyi1,(230,100))
    # screen.blit(heiyi1,(250,100))
    # screen.blit(heiyi1,(270,100))
    # screen.blit(heiyi1,(290,100))
    # screen.blit(heiyi1,(310,100))
    # screen.blit(heiyi1,(330,100))
    # screen.blit(heiyi2,(490,240))
    # screen.blit(heiyi2,(490,290))
    # screen.blit(heiyi2,(490,340))
    # screen.blit(heiyi2,(459,340))
    # screen.blit(heiyi2,(428,340))
    # screen.blit(heiyi2,(397,340))
    # screen.blit(heiyi2,(366,340))
    # screen.blit(heiyi2,(335,340))
    # screen.blit(tong2,(150,340))
    # screen.blit(tong2,(150,395))
    # screen.blit(tong2,(150,450))
    # screen.blit(tong2,(150,505))
    # screen.blit(tong1,(360,560))
    # screen.blit(tong1,(360,535))
    # screen.blit(tong1,(360,505))
    # screen.blit(tong1,(342,505))
    # screen.blit(tong1,(324,505))
    # screen.blit(tong1,(378,505))
    # screen.blit(tong1,(396,505))
    # screen.blit(tong1,(414,505))


    #BALLBALL: A better way to display barriers, and a easier way to check collision
    for h1 in heiyi1s:
        screen.blit(heiyi1, (h1[0], h1[1]))
    for h2 in heiyi2s:
        screen.blit(heiyi2, (h2[0], h2[1]))
    for t1 in tong1s:
        screen.blit(tong1, (t1[0], t1[1]))
    for t2 in tong2s:
        screen.blit(tong2, (t2[0], t2[1]))

    if appleimg == 1:
        screen.blit(apple1, appleloc)
    elif appleimg == 2:
        screen.blit(apple2, appleloc)
    else:
        screen.blit(apple3, appleloc)

    #BALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALL


    #snake run


    # 6.1 - draw player
    for player in players:
        if player[0]<1 or player[0]>640 or player[1]<1 or player[1]>640:
            running = 0
            #screen.blit(gameover, (0,0))
        # 6.1.1 turn around
            

    for player in players:
        screen.blit(playerimg,(player[0], player[1]))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==K_RIGHT:
                copy = players[:]
                for i in range(len(players)-1,0,-1):
                    players[i] = copy[i-1]
                players[0] = [23+players[0][0], players[0][1]]
                        
            
            elif event.key==K_LEFT:
                copy = players[:]
                for i in range(len(players)-1,0,-1):
                    players[i] = copy[i-1]
                players[0] = [players[0][0]-23, players[0][1]]


            elif event.key==K_UP:
                copy = players[:]
                for i in range(len(players)-1,0,-1):
                    players[i] = copy[i-1]
                players[0] = [players[0][0], players[0][1]-25]


            elif event.key==K_DOWN:
                copy = players[:]
                for i in range(len(players)-1,0,-1):
                    players[i] = copy[i-1]
                players[0] = [players[0][0], 25+players[0][1]]

    #draw the apple
    #appletime -= 100

    playrect = pygame.Rect(playerimg.get_rect())
    playrect.top = players[0][1]
    playrect.left = players[0][0]
    #BALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALL
    # playrect.right = players[0][0] + 23
    # playrect.bottom = players[0][1] + 25 
    #BALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALL

    applerect = pygame.Rect(apple1.get_rect())
    applerect.top = appleloc[1]
    applerect.left = appleloc[0]
    if applerect.colliderect(playrect):
        players.append([appleloc[0], appleloc[1]])
        appleloc = [random.randint(0,640-apple1.get_width()), random.randint(0,640-apple2.get_height())]
        appleimg = random.randint(0, len(apples))
        score += 1
        eat.play()


    #BALLBALL: collide barriers:
    for t1 in tong1s:
        tongrect = pygame.Rect(tong1.get_rect())
        tongrect.top = t1[1]
        tongrect.left = t1[0]+5
        if tongrect.colliderect(playrect):
            print 1
            running = 0

    for t2 in tong2s:
        tongrect = pygame.Rect(tong2.get_rect())
        tongrect.top = t2[1]
        tongrect.left = t2[0]+5
        if tongrect.colliderect(playrect):
            print 2
            running = 0

    for h1 in heiyi1s:
        heiyirect = pygame.Rect(heiyi1.get_rect())
        heiyirect.top = h1[1]
        heiyirect.left = h1[0]
        if heiyirect.colliderect(playrect):
            print 3
            running = 0

    for h2 in heiyi2s:
        heiyirect = pygame.Rect(heiyi2.get_rect())
        heiyirect.top = h2[1]
        heiyirect.left = h2[0]
        if heiyirect.colliderect(playrect):
            print 4
            running = 0
    #BALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALLBALL

 #draw score
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str(score),True,(0,0,255))
    textRect = survivedtext.get_rect()
    textRect.topright=[600,50]
    screen.blit(survivedtext, textRect)

    
    # #print len(apple)
    # index = 0
    # for ap in apple:
    #     if applesimg[index] == [1]:
    #         screen.blit(apple1, (ap[0], ap[1]))
    #     elif applesimg[index] == [2]:
    #         screen.blit(apple2, (ap[0], ap[1]))
    #     elif applesimg[index] == [3]:
    #         screen.blit(apple3, (ap[0], ap[1]))
    #     applerect = pygame.Rect(apple1.get_rect())
    #     applerect.top = ap[0]
    #     applerect.left = ap[1]
    #     if playrect.colliderect(applerect):
    #         apple.pop(index)
    #         apple.append([random.randint(0,640-apple1.get_width()), random.randint(0,640-apple2.get_height())])
    #         applesimg.append([random.randint(0,len(apples))])
    #     else:
    #         index += 1
            
        

    
##    class Food(object):  
##        def __init__(self, Grid):  
##            self.grid = Grid  
##            self.color = "#23D978"          
##            self.set_pos()  
##        def set_pos(self):  
##            x = randint(0,self.grid.grid_x - 1)  
##            y = randint(0,self.grid.grid_y - 1)  
##            self.pos =  (x, y)      
##        def display(self):  
##            self.grid.draw(self.pos,self.color)
   # """
    #I don't think you've thoroughly understood this chunk of code. I don't recommend copy and paste codes that you are not sure
    #what they are doing. If you stop trying to make your code look like other people's, you would probably come up with a better
    #implementation sooner. Just a piece of advice. You didn't even copy it correctly......
    #"""
##    
##    #6.2 - check for collisions
##    playrect = pygame.Rect(playerimg.get_rect())
##    playrect.top = playrect[1]
##    playrect.left = playrect[0]
##    playrect.right = playrect[0] + 23
##    playrect.bottom = playrect[1] + 25 
##    index = 0
##    applesrect = pygame.Rect(randomapple.get_rect())
##    applesrect.top = applesrect[1]
##    applesrect.left = applesrect[0]
##    applesrect.right = applesrect[0] +23
##    applesrect.bottom = applesrect[1] +25
##    if playrect.colliderect(applesrect):
##        randomapples.pop(index)
##            


    # 7 - update the screen
    pygame.display.flip()

    # 8 - loop through the events
    for event in pygame.event.get():
        # 8.1 check if the event is the X button
        if event.type==pygame.QUIT:
            # 8.1.1 if it is quit the game
            pygame.quit()
            exit(0)
        # 8.2 turn around
##        head = self.playerpos[0]  """For example, if I ask you what does 'self' mean, can you explain it? If not, don't use it. """
##        if self.direction == 'Up':  
##            new = (head[0], head[1]-1)  
##        elif self.direction == 'Down':  
##            new = (head[0], head[1]+1)  
##        elif self.direction == 'Left':  
##            new = (head[0]-1,head[1])  
##        else:  
##            new = (head[0]+1,head[1])  
##        if not self.randomapple.pos == head:           
##            pop = self.body.pop()  
##            self.grid.draw(pop,self.grid.bg)  
##        else:  
##            self.display_food()  
##            self.score += 1  
##        self.body.insert(0,new)        
##        if not new in self.available_grid():  
##            self.status.reverse()              
##            self.gameover = True  
##        else:  
##            self.grid.draw(new,color=self.color)
##    
##                
if running == 0:
    screen.blit(gameover, (0,0))
    pygame.display.flip()

while 1:
    for event in pygame.event.get():
    # 8.1 check if the event is the X button
        if event.type==pygame.QUIT:
            # 8.1.1 if it is quit the game
            pygame.quit()
            exit(0)



        #if event.type == pygame.KEYDOWN:
         #   print "down"
