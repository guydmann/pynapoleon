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

import random
import os, pygame,math
from pygame.locals import *
from inits import *

        
       
class cards:
    
    def __init__(self): 

        self.cardItem = []
        #add Hearsts cards
        
        self.cardItem.append(card(cardNumber.Ace,cardType.Hearts,13,"ah.gif"))
        #self.cardItem[0]=card(cardNumber.Ace,cardType.Hearts,13,"ah.gif")
        
        self.cardItem.append(card(cardNumber.num2,cardType.Hearts,1,"2h.gif"))
        self.cardItem.append(card(cardNumber.num3,cardType.Hearts,2,"3h.gif"))
        self.cardItem.append(card(cardNumber.num4,cardType.Hearts,3,"4h.gif"))
        self.cardItem.append(card(cardNumber.num5,cardType.Hearts,4,"5h.gif"))
        self.cardItem.append(card(cardNumber.num6,cardType.Hearts,5,"6h.gif"))
        self.cardItem.append(card(cardNumber.num7,cardType.Hearts,6,"7h.gif"))
        self.cardItem.append(card(cardNumber.num8,cardType.Hearts,7,"8h.gif"))
        self.cardItem.append(card(cardNumber.num9,cardType.Hearts,8,"9h.gif"))
        self.cardItem.append(card(cardNumber.num10,cardType.Hearts,9,"th.gif"))
        self.cardItem.append(card(cardNumber.jack,cardType.Hearts,10,"jh.gif"))
        self.cardItem.append(card(cardNumber.queen,cardType.Hearts,11,"qh.gif"))
        self.cardItem.append(card(cardNumber.king,cardType.Hearts,12,"kh.gif"))
        
        #add Spades cards
        self.cardItem.append(card(cardNumber.Ace,cardType.Spades,13,"as.gif"))
        self.cardItem.append(card(cardNumber.num2,cardType.Spades,1,"2s.gif"))
        self.cardItem.append(card(cardNumber.num3,cardType.Spades,2,"3s.gif"))
        self.cardItem.append(card(cardNumber.num4,cardType.Spades,3,"4s.gif"))
        self.cardItem.append(card(cardNumber.num5,cardType.Spades,4,"5s.gif"))
        self.cardItem.append(card(cardNumber.num6,cardType.Spades,5,"6s.gif"))
        self.cardItem.append(card(cardNumber.num7,cardType.Spades,6,"7s.gif"))
        self.cardItem.append(card(cardNumber.num8,cardType.Spades,7,"8s.gif"))
        self.cardItem.append(card(cardNumber.num9,cardType.Spades,8,"9s.gif"))
        self.cardItem.append(card(cardNumber.num10,cardType.Spades,9,"ts.gif"))
        self.cardItem.append(card(cardNumber.jack,cardType.Spades,10,"js.gif"))
        self.cardItem.append(card(cardNumber.queen,cardType.Spades,11,"qs.gif"))
        self.cardItem.append(card(cardNumber.king,cardType.Spades,12,"ks.gif"))
        
        #add Daimond cards
        self.cardItem.append(card(cardNumber.Ace,cardType.Daimond,13,"ad.gif"))
        self.cardItem.append(card(cardNumber.num2,cardType.Daimond,1,"2d.gif"))
        self.cardItem.append(card(cardNumber.num3,cardType.Daimond,2,"3d.gif"))
        self.cardItem.append(card(cardNumber.num4,cardType.Daimond,3,"4d.gif"))
        self.cardItem.append(card(cardNumber.num5,cardType.Daimond,4,"5d.gif"))
        self.cardItem.append(card(cardNumber.num6,cardType.Daimond,5,"6d.gif"))
        self.cardItem.append(card(cardNumber.num7,cardType.Daimond,6,"7d.gif"))
        self.cardItem.append(card(cardNumber.num8,cardType.Daimond,7,"8d.gif"))
        self.cardItem.append(card(cardNumber.num9,cardType.Daimond,8,"9d.gif"))
        self.cardItem.append(card(cardNumber.num10,cardType.Daimond,9,"td.gif"))
        self.cardItem.append(card(cardNumber.jack,cardType.Daimond,10,"jd.gif"))
        self.cardItem.append(card(cardNumber.queen,cardType.Daimond,11,"qd.gif"))
        self.cardItem.append(card(cardNumber.king,cardType.Daimond,12,"kd.gif"))      
        
        #add Clubs cards
        self.cardItem.append(card(cardNumber.Ace,cardType.Clubs,13,"ac.gif"))
        self.cardItem.append(card(cardNumber.num2,cardType.Clubs,1,"2c.gif"))
        self.cardItem.append(card(cardNumber.num3,cardType.Clubs,2,"3c.gif"))
        self.cardItem.append(card(cardNumber.num4,cardType.Clubs,3,"4c.gif"))
        self.cardItem.append(card(cardNumber.num5,cardType.Clubs,4,"5c.gif"))
        self.cardItem.append(card(cardNumber.num6,cardType.Clubs,5,"6c.gif"))
        self.cardItem.append(card(cardNumber.num7,cardType.Clubs,6,"7c.gif"))
        self.cardItem.append(card(cardNumber.num8,cardType.Clubs,7,"8c.gif"))
        self.cardItem.append(card(cardNumber.num9,cardType.Clubs,8,"9c.gif"))
        self.cardItem.append(card(cardNumber.num10,cardType.Clubs,9,"tc.gif"))
        self.cardItem.append(card(cardNumber.jack,cardType.Clubs,10,"jc.gif"))
        self.cardItem.append(card(cardNumber.queen,cardType.Clubs,11,"qc.gif"))
        self.cardItem.append(card(cardNumber.king,cardType.Clubs,12,"kc.gif"))  
        
        
        #shuffle cards
        self.shuffle()
        
    def shuffle(self):
        for i in range(0,1000) :
            random.shuffle(self.cardItem)
            random.shuffle(self.cardItem)
            random.shuffle(self.cardItem)
    
              
    def deck(self,player1,player2,player3,player4,pot):
        #for i in range(0,52,4):
        #    player1.addHand(self.cardItem[i])
        #    player2.addHand(self.cardItem[i+1])
        #    player3.addHand(self.cardItem[i+2])
        #    player4.addHand(self.cardItem[i+3])
        #return
        for i in range(0,12):
            player1.addHand(self.cardItem[i])
        for i in range(12,24):
            player2.addHand(self.cardItem[i])
        for i in range(24,36):
            player3.addHand(self.cardItem[i])
        for i in range(36,48):
            player4.addHand(self.cardItem[i])
        for i in range(36,48):
            player4.addHand(self.cardItem[i])
        for i in range(48,52):
            pot.addHand(self.cardItem[i])        
        


        #return player1,player2,player3,player4
    
 
pygame.init()

My_Window = pygame.display.set_mode((640, 480))
 
s=cards()   



 