#!/usr/bin/env python
#Game redevelopment by Guy Mann (guydmann atsign gmail dot com) 
#Copyright (C) 2008  Guy Mann
#Game developed by Milad Rastian (miladmovie atsign gmail dot com) 
#http://home.gna.org/pyhearts/
#I wrote this Game for course Artificial Intelligent in Yazd Jahad University
#Thanks my teacher Mr Asghar Dehghani
#I in this project I know how much I Love Python !
#Copyright (C) 2007  Milad Rastian
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import os, pygame,math
class cardType:
    Hearts=1
    Spades=2
    Daimond=3
    Clubs=4

class biddingSuites:
    Hearts=1
    Spades=2
    Daimond=3
    Clubs=4
    NoTrump=5

class cardNumber:
    Ace=13
    num2=1
    num3=2
    num4=3
    num5=4
    num6=5
    num7=6
    num8=7
    num9=8
    num10=9
    jack=10
    queen=11
    king=12
    

    
def load_image(name, colorkey=None):
    fullname = os.path.join('data/img/', name)
    
    try:
        image=pygame.image.load(fullname)
        image=image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image, image.get_rect()
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message

class card:
    def __init__(self,name,type,priority,image,x=0,y=0):
        self.name=name
        self.type=type
        self.priority=priority
        self.use=False
        self.fimg,tmp=load_image(image)
        self.bimg,tmp=load_image("b.gif")
        self.img,self.rect = load_image("b.gif")
        #print self.rect
        #print self.rect.collidepoint(0, 0)
        self.isPlayed=False
        self.rect.x = x
        self.rect.y = y        
        self.side = 0
        self.index=0

    def moveCard(self,x,y):
        self.rect.x=x
        self.rect.y=y
    def getfrontImage(self):
        return self.fimg,self.rect
    def getImage(self):
        return self.img,self.rect
    def goUp(self,screen):
        background=self.fimg
        screen.blit(background, (self.rect))
    def getBackImage(self):
        return self.bimg,self.rect

screenPlayer1=[]

for i in range (60,265,15):
    screenPlayer1.append([10,i])

screenPlayer1.append([132,150])

screenPlayer2=[]
for i in range (120,326,15):
    screenPlayer2.append([i,5])
screenPlayer2.append([210,103])    

screenPlayer3=[]
for i in range (60,265,15):
    screenPlayer3.append([420,i])
screenPlayer3.append([290,150]) 
  
screenPlayer4=[]
for i in range (120,326,15):
    screenPlayer4.append([i,300])
screenPlayer4.append([210,200])
#for loc in screenPlayer1:
#    print loc[1]
