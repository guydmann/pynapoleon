#!/usr/bin/env python
#Game redevelopment by Guy Mann (guydmann atsign gmail dot com) 
#Copyright (C) 2008  Guy Mann
#I am taking the existing framework of this hearts program and will program my own napoleon game
#Napoleons play style is a great deal like hearts, where hands are won and pos are obtained for specific cards.
#I am doing this project to familiarize myself with python.
#While i'm changing things i will try and put more comments in so that anyone else can try the same sort of thing with their own rules.
#
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

import os, pygame,math, random
from pygame.locals import *
from Player import *
from inits import  *
from  Card import *

class background:
	def __init__(self):
		self.blink=0 #it will contorl blink text until 

		pygame.init()
		
		icon,tmp=load_image("icon.png")
		pygame.display.set_icon(icon)        
		self.screen = pygame.display.set_mode((500,450),1)
		self.ShowScoreBoardDialog =False
		self.playedCards=[]
		self.tmpPlayedCard=[]
		self.scoreBoard=[]
		#self.NapoleonsANDBids=[]
		self.errorMsg=""
		self.numberofplayers=0
		self.isPlayHeart=False
		pygame.display.set_caption('PyNapoleon')
		self.tmpGeneralCardNumber=None
		self.tmpGeneralCardSuite=None

#the intro
#wait for user input to start the game
#gotta have this cause very few people know what napoleon is
		self.screen.fill((0x00, 0xb0, 0x00))
		pygame.display.flip() 
		self.ready=0
		
		while self.ready==0:
			self.introDialog()
			pygame.display.flip()  
			pygame.time.delay(20)
			for event in pygame.event.get():
				if event.type == QUIT:
					return     
				if event.type==KEYDOWN:
					if event.key==13:
						self.ready = 1
						break
					if event.key==271:			
						self.ready = 1
						break
				if event.type==MOUSEBUTTONDOWN:
					self.ready = 1
					break					
			continue

	
	
	
	
#	if self.numberofplayers==4:
		self.player1=None
		self.player2=None
		self.player3=None
		self.player4=None
		self.playerName=[]
		self.playerName.append("Lord_Nelson")
		self.playerName.append("darksider")
		self.playerName.append("NapoBot")
		self.playerName.append("User")
#	else:
#		self.player1=None
#		self.player2=None
#		self.player3=None
#		self.player4=None
#		self.playerName=[]
#		self.playerName.append("Lord_Nelson")
#		self.playerName.append("darksider")
#		self.playerName.append("NapoBot")
#		self.playerName.append("User")       
       
       


	
		#self.scoreBoard.append([0,0,0,0])
		#self.scoreBoard.append([20,16,8,9])
		
		#self.scoreBoard.append([ 100 , 50 , 9 , 9 ])
		#reset hands
		self.playAgain()
		self.emptyGround=False


		self.screen.fill((0x00, 0xb0, 0x00))
		#self.drawCardsInHand()
		#bac,rc=load_image("j.gif")
		#self.screen.blit(bac,(290,150))
		self.screen.fill((0x00, 0xb0, 0x00))
		pygame.display.flip() 
		
		self.numOfDeckPlay=0         
		self.players=[]
		self.players.append(self.player1)
		self.players.append(self.player2)
		self.players.append(self.player3)
		self.players.append(self.player4)


		self.bidnumber=None
		self.bidsuite=None
		#self.currentbidnumber=None
		#self.currentbidsuite=None
		indD=0
		while 1:  
			#change status of self.blink
			if self.blink==11 : self.blink=0
			else : self.blink+=1
			

	#check if score board Dialog is open dont let players to play
			if self.ShowScoreBoardDialog==True:
				self.scoreBoardDialog()

				pygame.display.flip()  
				pygame.time.delay(20)
				for event in pygame.event.get():
					if event.type == QUIT:
						return                     
					#if event.type==MOUSEBUTTONDOWN:
					#	self.backToGame()
					if event.type==KEYDOWN  :
						if event.key==13:
							self.backToGame()
						if event.key==27:
							return 
				continue
	#check if one player get all cards give point to others
			if self.numOfDeckPlay==13:
				print ""
				print ""
				print ""
				print self.player1.name," get ",self.player1.result," point"
				print self.player2.name," get ",self.player2.result," point"
				print self.player3.name," get ",self.player3.result," point"
				print self.player4.name," get ",self.player4.result," point"
				
				
				if self.Napoleon==1:
					self.result =self.player1.result
				if self.Napoleon==2:
					self.result =self.player2.result
				if self.Napoleon==3:
					self.result =self.player3.result					
				if self.Napoleon==4:
					self.result =self.player4.result

				if self.General==1:
					self.result =self.result +self.player1.result
				if self.General==2:
					self.result =self.result +self.player2.result
				if self.General==3:
					self.result =self.result +self.player3.result					
				if self.General==4:
					self.result =self.result +self.player4.result
					
				if self.Napoleon==1:
					if self.bidnumber <=self.result:
						print "%s is successful in their bid of %d and wins the game" % (self.player1.name, self.bidnumber,)
					else:
						print "%s failed in their bid of %d and loses the game" % (self.player1.name, self.bidnumber,)
				if self.Napoleon==2:
					if self.bidnumber <=self.result:
						print "%s is successful in their bid of %d and wins the game" % (self.player2.name, self.bidnumber,)
					else:
						print "%s failed in their bid of %d and loses the game" % (self.player2.name, self.bidnumber,)
				if self.Napoleon==3:
					if self.bidnumber <=self.result:
						print "%s is successful in their bid of %d and wins the game" % (self.player3.name, self.bidnumber,)
					else:
						print "%s failed in their bid of %d and loses the game" % (self.player3.name, self.bidnumber,)
				if self.Napoleon==4:
					if self.bidnumber <=self.result:
						print "You are successful in your bid of %d and wins the game" % (self.bidnumber,)
					else:
						print "You have failed in your bid of %d and lose the game" % ( self.bidnumber,)
						
					if self.bidnumber <=self.result:
						print "%s is successful in their bid of %d and wins the game" % (self.player1.name, self.bidnumber,)
					else:
						print "%s failed in their bid of %d and loses the game" % (self.player1.name, self.bidnumber,)						
				print ""
				print ""
				print ""
				
				#add last scores to scoreBoard
				self.scoreBoard.append([self.player1.result,self.player2.result,self.player3.result,self.player4.result,self.bidnumber,self.Napoleon,self.General])
				#self.NapoleonsANDBids.append([)
				self.ShowScoreBoardDialog=True
				self.scoreBoardDialog()
				
				self.player1.result=0
				self.player2.result=0
				self.player3.result=0
				self.player4.result=0

				#if one player score is bigger than 100 then game is end and restart games object
				if self.player1.result>=100 or self.player2.result>=100 or self.player3.result>=100 or self.player4.result>=100 :
					self.playedCards=[]
					self.tmpPlayedCard=[]
					self.numOfDeckPlay=0 
					self.players=[]
					self.players.append(self.player1)
					self.players.append(self.player2)
					self.players.append(self.player3)
					self.players.append(self.player4)
					self.emptyGround=False          
					self.errorMsg=""
					self.isPlayHeart=False                                    
				else:
					self.playAgain()
				continue
			#this is for bidding
			if self.playerspassedbid==3:
				self.bidnumber=self.currentbidnumber
				self.bidsuite=self.currentbidsuite
				self.Napoleon=self.currentbidwinner
				#this will need to be commented out once we implement the pot and the general
				self.turnPlay=self.currentbidwinner	
				self.playerspassedbid=0
			if self.bidnumber==None  and self.bidsuite==None:
				if self.currentbidnumber==None and self.currentbidsuite==None:
					self.screen.fill((0x00, 0xb0, 0x00))	
				#the player needs to see their cards to bid
				self.drawCardsInHand()
				self.showNames()				
				pygame.display.flip()  
				#pygame.time.delay(20)

				if self.turnBid==1:
					self.bid=self.player1.bid(self.currentbidnumber,self.currentbidsuite,self.players)
					if self.bid!=0:
						self.currentbidnumber = self.bid
						self.currentbidsuite = self.player1.currentbidsuite
						self.currentbidwinner=1
						self.playerspassedbid = 0
						print "%s bid %d, %d" % (self.player1.name, self.currentbidnumber, self.currentbidsuite,)
					else:
						self.player1.currentbidsuite=0
						self.player1.currentbidnumber=0
						self.playerspassedbid = self.playerspassedbid +1
						print "%s passed" % (self.player1.name,)
					self.bid=None
				elif self.turnBid==2:
					self.bid=self.player2.bid(self.currentbidnumber,self.currentbidsuite,self.players)
					if self.bid!=0:
						self.currentbidnumber = self.bid
						self.currentbidsuite = self.player2.currentbidsuite
						self.currentbidwinner=2
						self.playerspassedbid = 0
						print "%s bid %d, %d" % (self.player2.name, self.currentbidnumber, self.currentbidsuite,)
					else:
						self.player2.currentbidsuite=0
						self.player2.currentbidnumber=0
						self.playerspassedbid = self.playerspassedbid +1
						print "%s passed" % (self.player2.name,)
					self.bid=None
				elif self.turnBid==3:
					self.bid=self.player3.bid(self.currentbidnumber,self.currentbidsuite,self.players)
					if self.bid!=0:
						self.currentbidnumber = self.bid
						self.currentbidsuite = self.player3.currentbidsuite
						self.currentbidwinner=3
						self.playerspassedbid = 0
						print "%s bid %d, %d" % (self.player3.name, self.currentbidnumber, self.currentbidsuite,)
					else:
						self.player3.currentbidsuite=0
						self.player3.currentbidnumber=0
						self.playerspassedbid = self.playerspassedbid +1
						print "%s passed" % (self.player3.name,)
					self.bid=None
				#elif self.turnBid==4  and self.player4.currentbidnumber==None and self.player4.currentbidsuite==None:
				elif self.turnBid==4:
					self.bid=None
					self.drawCardsInHand()
					self.showNames()		
					self.showMessage("bidding: +/- on numpad and 1-5 for suite, enter to bid, space to pass")	
					pygame.display.flip()  	
					if self.player4.currentbidnumber==None:
						self.player4.currentbidnumber=0
					while self.bid==None:
						for event in pygame.event.get():
							if event.type == QUIT:
								return                     
							#if event.type==MOUSEBUTTONDOWN:
							#	print "something"
							if event.type==KEYDOWN :
								#print event.key
								if event.key==13:
									if self.player4.currentbidnumber>self.currentbidnumber and self.player4.currentbidsuite!=None:
										self.currentbidnumber = self.player4.currentbidnumber
										self.currentbidsuite = self.player4.currentbidsuite
										self.bid=self.currentbidnumber
										self.currentbidwinner=4
										self.playerspassedbid = 0
									else:
										if self.player4.currentbidnumber<=self.currentbidnumber:
											self.screen.fill((0x00, 0xb0, 0x00))	
											#the player needs to see their cards to bid
											self.drawCardsInHand()
											self.showNames()			
											self.showMessage("Bid not high enough")										
											pygame.display.flip()  										
											pygame.time.delay(1000)
										else:
											self.screen.fill((0x00, 0xb0, 0x00))	
											#the player needs to see their cards to bid
											self.drawCardsInHand()
											self.showNames()		
											self.showMessage("Select a suite")										
											pygame.display.flip()  										
											pygame.time.delay(1000)

								if event.key==49:
									self.player4.currentbidsuite=1							
								if event.key==50:
									self.player4.currentbidsuite=2								
								if event.key==51:
									self.player4.currentbidsuite=3
								if event.key==52:
									self.player4.currentbidsuite=4
								if event.key==53:
									self.player4.currentbidsuite=5
								if event.key==270:
									if self.player4.currentbidnumber<20:
										self.player4.currentbidnumber=self.player4.currentbidnumber+1
									else:
										self.screen.fill((0x00, 0xb0, 0x00))	
										#the player needs to see their cards to bid
										self.drawCardsInHand()
										self.showNames()		
										self.showMessage("20 is the maximum bid")										
										pygame.display.flip()  										
										pygame.time.delay(1000)									
								if event.key==269:
									if self.player4.currentbidnumber>1:
										self.player4.currentbidnumber=self.player4.currentbidnumber-1
									else:
										self.screen.fill((0x00, 0xb0, 0x00))	
										#the player needs to see their cards to bid
										self.drawCardsInHand()
										self.showNames()
										self.showMessage("1 is the minimum bid")										
										pygame.display.flip()  										
										pygame.time.delay(1000)													
								if event.key==32:
									self.player4.currentbidsuite=0
									self.player4.currentbidnumber=0
									print "%s passed" % (self.player4.name,)
									self.playerspassedbid = self.playerspassedbid +1
									self.bid=0
								self.screen.fill((0x00, 0xb0, 0x00))	
								#the player needs to see their cards to bid
								self.drawCardsInHand()
								self.showNames()	
								self.showMessage("bidding: +/- on numpad and 1-5 for suite, enter to bid, spacebar to pass")
								pygame.display.flip()  
					self.bid=None
				if self.turnBid==1:
					self.turnBid=2
				elif self.turnBid==2:
					self.turnBid=3
				elif self.turnBid==3:
					self.turnBid=4
				#if self.turnBid==4 and self.player4.currentbidnumber!=None:
				elif self.turnBid==4:
					self.turnBid=1
			if self.bidnumber!=None  and self.bidsuite!=None and self.GeneralCardNumber==None and self.GeneralCardSuite==None:
				self.selectedGeneralCard=[]
				self.player1.analayzHand(self.bidsuite)
				self.player2.analayzHand(self.bidsuite)
				self.player3.analayzHand(self.bidsuite)
				if self.Napoleon==1 :
					self.selectedGeneralCard=self.player1.selectGeneralCard()
					self.GeneralCardNumber=self.selectedGeneralCard[0]
					self.GeneralCardSuite=self.selectedGeneralCard[1]
				if self.Napoleon==2 :
					self.selectedGeneralCard=self.player2.selectGeneralCard()
					self.GeneralCardNumber=self.selectedGeneralCard[0]
					self.GeneralCardSuite=self.selectedGeneralCard[1]
				if self.Napoleon==3:
					self.selectedGeneralCard=self.player3.selectGeneralCard()
					self.GeneralCardNumber=self.selectedGeneralCard[0]
					self.GeneralCardSuite=self.selectedGeneralCard[1]
				if self.Napoleon==4:
					self.tmpGeneralCardNumber=13
					self.tmpGeneralCardSuite=2					
					self.drawCardsInHand()
					self.showNames()
					self.showbids()				
					self.showgeneral()
					self.showMessage("General Selection: +/- on numpad and 1-5 for suite, enter to select")	
					pygame.display.flip()  	

					while self.GeneralCardNumber ==None:
						for event in pygame.event.get():
							if event.type == QUIT:
								return                     
							#if event.type==MOUSEBUTTONDOWN:
							#	print "something"
							if event.type==KEYDOWN :
								#print event.key
								if event.key==13:
									if self.tmpGeneralCardNumber!=None and self.tmpGeneralCardSuite!=None:
										self.GeneralCardNumber = self.tmpGeneralCardNumber
										self.GeneralCardSuite = self.tmpGeneralCardSuite
										#self.bid=self.currentbidnumber
										#self.currentbidwinner=4
										#self.playerspassedbid = 0
									else:
										if  self.tmpGeneralCardNumber==None:
											self.screen.fill((0x00, 0xb0, 0x00))	
											#the player needs to see their cards to bid
											self.drawCardsInHand()
											self.showNames()
											self.showMessage("Select a General Card Type")										
											pygame.display.flip()  										
											pygame.time.delay(1000)
										else:
											self.screen.fill((0x00, 0xb0, 0x00))	
											#the player needs to see their cards to bid
											self.drawCardsInHand()
											self.showNames()											
											self.showMessage("Select a General Card Type")										
											pygame.display.flip()  										
											pygame.time.delay(1000)

								if event.key==49:
									self.tmpGeneralCardSuite=1							
								if event.key==50:
									self.tmpGeneralCardSuite=2								
								if event.key==51:
									self.tmpGeneralCardSuite=3
								if event.key==52:
									self.tmpGeneralCardSuite=4
								if event.key==270:
									if self.tmpGeneralCardNumber<13:
										self.tmpGeneralCardNumber=self.tmpGeneralCardNumber+1
									else:
										self.screen.fill((0x00, 0xb0, 0x00))	
										#the player needs to see their cards to bid
										self.drawCardsInHand()
										self.showNames()
										self.showMessage("Ace is the highest card")										
										pygame.display.flip()  										
										pygame.time.delay(1000)									
								if event.key==269:
									if self.tmpGeneralCardNumber>1:
										self.tmpGeneralCardNumber=self.tmpGeneralCardNumber-1
									else:
										self.screen.fill((0x00, 0xb0, 0x00))	
										#the player needs to see their cards to bid
										self.drawCardsInHand()
										self.showNames()
										self.showMessage("1 is the minimum bid")										
										pygame.display.flip()  										
										pygame.time.delay(1000)													
								self.screen.fill((0x00, 0xb0, 0x00))	
								#the player needs to see their cards to bid
								self.drawCardsInHand()
								self.showNames()							
								self.showMessage("General Selection: +/- on numpad and 1-5 for suite, enter to select")
								pygame.display.flip()  
					#self.tmpGeneralCardNumber=None
					#self.tmpGeneralCardSuite=None
				print "the general card is %d of %d" % (self.GeneralCardNumber, self.GeneralCardSuite,)
				self.player1.analayzHand(self.bidsuite,self.GeneralCardNumber, self.GeneralCardSuite)
				self.player2.analayzHand(self.bidsuite,self.GeneralCardNumber, self.GeneralCardSuite)
				self.player3.analayzHand(self.bidsuite,self.GeneralCardNumber, self.GeneralCardSuite)
				
			indD+=1
			if self.turnPlay==1 and self.player1.currentPlay==None:
				#print "1"
				self.selectedCard=self.player1.play(self.tmpPlayedCard,self.playedCards,self.numOfDeckPlay,self.players,self.bidnumber,self.bidsuite,self.Napoleon,self.General)
				self.player1.currentPlay=self.selectedCard
				#move card to ground
				self.moveCardSlowly(self.selectedCard,screenPlayer1[14])
				self.tmpPlayedCard.append([self.selectedCard,1])
				print "Player 1 plays ",self.selectedCard.name, " of ", self.selectedCard.type
				self.selectedCard=None
			elif self.turnPlay==2 and self.player2.currentPlay==None:
				#print "2"
				self.selectedCard=self.player2.play(self.tmpPlayedCard,self.playedCards,self.numOfDeckPlay,self.players,self.bidnumber,self.bidsuite,self.Napoleon,self.General)
				self.player2.currentPlay=self.selectedCard
				self.moveCardSlowly(self.selectedCard,screenPlayer2[14])
				self.tmpPlayedCard.append([self.selectedCard,2])
				print "Player 2 plays ",self.selectedCard.name, " of ", self.selectedCard.type
				self.selectedCard=None

			elif self.turnPlay==3 and self.player3.currentPlay==None:
				#print "3"
				self.selectedCard=self.player3.play(self.tmpPlayedCard,self.playedCards,self.numOfDeckPlay,self.players,self.bidnumber,self.bidsuite,self.Napoleon,self.General)
				
				self.player3.currentPlay=self.selectedCard
				self.moveCardSlowly(self.selectedCard,screenPlayer3[14])
				self.tmpPlayedCard.append([self.selectedCard,3])
				print "Player 3 plays ",self.selectedCard.name, " of ", self.selectedCard.type
				self.selectedCard=None
				#pygame.time.delay(500)


			for event in pygame.event.get():
				if event.type == QUIT:
				    return  
				if event.type==KEYDOWN:
					#if press ESC go to score board
					if event.key==27:
						self.ShowScoreBoardDialog=True
				
				if event.type==MOUSEBUTTONDOWN:
					if event.button==1:
						#check if turn is player4 and click mouse button ...
						if self.player4.currentPlay==None and self.turnPlay==4:
							self.selectedCard=self.selectedCard=self.getCard(event.pos[0],event.pos[1])
							if self.selectedCard:
								#check if selected card is true to play
								if self.checkPlayCard(self.selectedCard,self.player4)==False:
									self.selectedCard=None
									break
								self.moveCardSlowly(self.selectedCard,screenPlayer4[14])
								self.player4.currentPlay=self.selectedCard
								self.tmpPlayedCard.append([self.selectedCard,4])
								self.selectedCard=None

					elif  event.button==3:
						self.selectedCard=self.selectedCard=self.getCard(event.pos[0],event.pos[1]) 
						#try to show pop selected Card
						if self.selectedCard:
							self.selectedCard.goUp(self.screen)
							pygame.display.flip() 
							pygame.time.delay(500)
							pass
				if   event.type==MOUSEBUTTONUP:
					if event.button==3:
						if self.selectedCard:
							if self.selectedCard.isPlayed==False:
								#try do put hands of Player4 again
								for i in range(0,13):
									if self.player4.cardsInHand[i].isPlayed==False:
										self.player4.moveCard(i,screenPlayer4[i][0], screenPlayer4[i][1])

			    
		#now if not turn to any player to play do ...
			if self.player1.currentPlay!=None   and self.player2.currentPlay!=None   and self.player3.currentPlay!=None   and self.player4.currentPlay!=None  :
				#palyed on deck so we put ground in  PlayedCards
				self.player1.currentPlay.isPlayed=True
				self.player2.currentPlay.isPlayed=True
				self.player3.currentPlay.isPlayed=True
				self.player4.currentPlay.isPlayed=True
				self.addPlayedCards(self.player1.currentPlay, self.player2.currentPlay, self.player3.currentPlay, self.player4.currentPlay)
				self.turnPlay=self.howTurnNow(self.player1.currentPlay, self.player2.currentPlay, self.player3.currentPlay, self.player4.currentPlay)
				
				#self.GeneralCardNumber), self.textsuite(self.GeneralCardSuite
				#if someone plays the general card everyone should know
				if self.player1.currentPlay.type==self.GeneralCardSuite and self.player1.currentPlay.name==self.GeneralCardNumber:
					self.General=1
				if self.player2.currentPlay.type==self.GeneralCardSuite and self.player2.currentPlay.name==self.GeneralCardNumber:
					self.General=2
				if self.player3.currentPlay.type==self.GeneralCardSuite and self.player3.currentPlay.name==self.GeneralCardNumber:
					self.General=3
				if self.player4.currentPlay.type==self.GeneralCardSuite and self.player4.currentPlay.name==self.GeneralCardNumber:
					self.General=4					
					
				#check result on this deck
				typeToPlayed=self.tmpPlayedCard[0][0].type
				numOfMaxPlayed=self.tmpPlayedCard[0][0].name
				cardBelongToPlayer=None
#				for i in range(0,4):
#					if self.tmpPlayedCard[i][0].type==typeToPlayed and  self.tmpPlayedCard[i][0].name>=numOfMaxPlayed:
#						numOfMaxPlayed=self.tmpPlayedCard[i][0].name
				if self.turnPlay ==1:
				    cardBelongToPlayer=self.player1
				elif self.turnPlay==2:
				    cardBelongToPlayer=self.player2
				elif self.turnPlay==3:    
				    cardBelongToPlayer=self.player3
				elif self.turnPlay==4:
				    cardBelongToPlayer=self.player4
				    
				if cardBelongToPlayer:
					result=0
					for card in self.tmpPlayedCard:
						if card[0].name>=9:
						    result+=1
						    
						#if card[0].type==cardType.Spades and card[0].name==cardNumber.queen:
						    #result+=13
					cardBelongToPlayer.result+=result
					cardBelongToPlayer.tmpResult+=result
					print cardBelongToPlayer.name," get ",result," point"
					cardBelongToPlayer=None

				else:
					print "Error ! report me now ! thanks"
				
				#now set None to play next deck
				self.player1.currentPlay=None
				self.player2.currentPlay=None
				self.player3.currentPlay=None
				#send out card location !
				#I don't exactly why ! but some times played card come over new card which is on ground
				#so that I send out card form screen !!!
				self.moveOut(self.player4.currentPlay)
				self.player4.currentPlay=None
				
				self.numOfDeckPlay+=1
				self.tmpPlayedCard=[]
				
				
				
			else:
				if self.turnPlay==1 and self.player1.currentPlay!=None:
					self.turnPlay=2
				if self.turnPlay==2 and self.player2.currentPlay!=None:
					self.turnPlay=3
				if self.turnPlay==3 and self.player3.currentPlay!=None:
					self.turnPlay=4
				if self.turnPlay==4 and self.player4.currentPlay!=None:
					self.turnPlay=1


			    #if   event.type!=MOUSEBUTTONDOWN and event.button == 3 :
			    
			self.screen.fill((0x00, 0xb0, 0x00))
			    
			self.drawCardsInHand()

			if self.turnPlay==1:
				self.showMessage("Waiting for "+ self.player1.name +" to play")
			if self.turnPlay==2:
				self.showMessage("Waiting for "+ self.player2.name +" to play")
			if self.turnPlay==3:
				self.showMessage("Waiting for "+ self.player3.name +" to play")
			if self.turnPlay==4:
				if self.errorMsg :
					self.showMessage(self.errorMsg)
				else :
					self.showMessage("Waiting for you to play! Come on "+ self.player4.name +" harryup")
				pass

			self.showNames()            
			pygame.display.flip()  
					   
			pygame.time.delay(50)
			# DRAWING             

	#check how is turn now
	def howTurnNow(self,card1,card2,card3,card4):
		print "trump is %d" % ( self.bidsuite, )
		print "c1:%d,%d" % (card1.type, card1.name)
		print "c2:%d,%d" % (card2.type, card2.name)
		print "c3:%d,%d" % (card3.type, card3.name)
		print "c4:%d,%d" % (card4.type, card4.name)
		
		getMaxCardOfDeckPlay=self.tmpPlayedCard[0][0]
		turn=1
		#check for the snoopy flying ace of spades
		
		if (card1.type==2 and card1.name==cardNumber.Ace):
			return 1
		if (card2.type==2 and card2.name==cardNumber.Ace):
			return 2
		if (card3.type==2 and card3.name==cardNumber.Ace):
			return 3
		if (card4.type==2 and card4.name==cardNumber.Ace):
			return 4
		#self.bidsuite=1
		#self.bidsuitealt=1
		#check for the jack of trump
		#print "Jtr"
		if (card1.type==self.bidsuite and card1.name==cardNumber.jack):
			return 1
		if (card2.type==self.bidsuite and card2.name==cardNumber.jack):
			return 2
		if (card3.type==self.bidsuite and card3.name==cardNumber.jack):
			return 3
		if (card4.type==self.bidsuite and card4.name==cardNumber.jack):
			return 4
		#self.bidsuitealt=1
		#check for the jack of same color as trump
		#print "Jctr"
		if (self.bidsuite==1):
			coloralt = 3
		if (self.bidsuite==2):
			coloralt = 4			
		if (self.bidsuite==3):
			coloralt = 1			
		if (self.bidsuite==4):
			coloralt = 2
		if (self.bidsuite==5):
			coloralt = 5			
		if (card1.type==coloralt and card1.name==cardNumber.jack):
			return 1
		if (card2.type==coloralt and card2.name==cardNumber.jack):
			return 2
		if (card3.type==coloralt and card3.name==cardNumber.jack):
			return 3
		if (card4.type==coloralt and card4.name==cardNumber.jack):
			return 4
		
		#check if everyone followed suite
		if (card1.type==getMaxCardOfDeckPlay.type and card2.type==getMaxCardOfDeckPlay.type and card3.type==getMaxCardOfDeckPlay.type and card4.type==getMaxCardOfDeckPlay.type):
			#if everyone followed suite check for a 2
			#print "followed suite"
			if (self.numOfDeckPlay!=0):
				if(card1.name==1):
					return 1
				if(card2.name==1):
					return 2
				if(card3.name==1):
					return 3
				if(card4.name==1):
					return 4
			if(card1.name>=getMaxCardOfDeckPlay.name):
				turn=1
				getMaxCardOfDeckPlay=card1
			if(card2.name>=getMaxCardOfDeckPlay.name):
				turn=2
				getMaxCardOfDeckPlay=card2
			if(card3.name>=getMaxCardOfDeckPlay.name):
				turn=3
				getMaxCardOfDeckPlay=card3
			if(card4.name>=getMaxCardOfDeckPlay.name):
				turn=4
				getMaxCardOfDeckPlay=card4
		else:
			#check for the highest card in suite
			#print "didn't follow suite"
			#print "trump is"
			#print self.bidsuite
			if (card1.type==getMaxCardOfDeckPlay.type):
				if(card1.name>=getMaxCardOfDeckPlay.name):
					turn=1
					getMaxCardOfDeckPlay=card1
			if (card2.type==getMaxCardOfDeckPlay.type):
				if(card2.name>=getMaxCardOfDeckPlay.name):
					turn=2
					getMaxCardOfDeckPlay=card2
			if (card3.type==getMaxCardOfDeckPlay.type):
				if(card3.name>=getMaxCardOfDeckPlay.name):
					turn=3
					getMaxCardOfDeckPlay=card3
			if (card4.type==getMaxCardOfDeckPlay.type):
				if(card4.name>=getMaxCardOfDeckPlay.name):
					turn=4
					getMaxCardOfDeckPlay=card4
			#print "current winner %d: %d,%d" % (turn,getMaxCardOfDeckPlay.type,getMaxCardOfDeckPlay.name,)
			#check for the highest trump card
			#print "checking trumps"
			if (card1.type==self.bidsuite):
				if(card1.name>=getMaxCardOfDeckPlay.name or getMaxCardOfDeckPlay.type!=self.bidsuite):
					turn=1
					getMaxCardOfDeckPlay=card1
			if (card2.type==self.bidsuite):
				if(card2.name>=getMaxCardOfDeckPlay.name or getMaxCardOfDeckPlay.type!=self.bidsuite):
					turn=2
					getMaxCardOfDeckPlay=card2
			if (card3.type==self.bidsuite):
				if(card3.name>=getMaxCardOfDeckPlay.name or getMaxCardOfDeckPlay.type!=self.bidsuite):
					turn=3
					getMaxCardOfDeckPlay=card3
			if (card4.type==self.bidsuite):
				if(card4.name>=getMaxCardOfDeckPlay.name or getMaxCardOfDeckPlay.type!=self.bidsuite):
					turn=4
					getMaxCardOfDeckPlay=card4
			#print "current winner %d: %d,%d" % (turn,getMaxCardOfDeckPlay.type,getMaxCardOfDeckPlay.name,)
		return turn



	def checkIsPlayHeart(self):
		for i in range(0,len(self.playedCards)):
			for j in range(0,4):
				if self.playedCards[i][j].type==cardType.Hearts:
					self.isPlayHeart=True
					return            

	    #check Players Play Correct Card
	def checkPlayCard(self,cardToPlay,player):
#		if(self.isPlayHeart==False):
#		    self.checkIsPlayHeart()
#		if(self.numOfDeckPlay==0):
#			if len(self.tmpPlayedCard)==0:
#				if cardToPlay.type==cardType.Clubs:
#					if cardToPlay.name==cardNumber.num2 :
#						return True
#				self.errorMsg="You Must Start Game with 2 Clubs, Come on Don't Be Stupid !"
#				return False
#			if(cardToPlay.type==cardType.Hearts):
#				self.errorMsg="In First Deck You Can not Play With Hearts, Do You Know How To Play?"
#				return False
#			if(cardToPlay.type==cardType.Spades and cardToPlay.name==cardNumber.queen):
#				self.errorMsg="In First Deck You Can Not Play With Queen Of Spades , Do You Know How To Play? "
#				return False
		if len(self.tmpPlayedCard)!=0:
#			if(self.isPlayHeart==False  and cardToPlay.type==cardType.Hearts):
#				self.errorMsg="You Can Not Play Hearts Now ! Take Another Card"
#				return False

			if cardToPlay.type!=self.tmpPlayedCard[0][0].type:
				if player.hastThisType(self.tmpPlayedCard[0][0].type):
				    self.errorMsg="Check Your Card To Play,You Should Play Card As Type First Deck"
				    return False
#		if(cardToPlay.type==cardType.Hearts) :     
#		    self.isPlayHeart=True


		self.errorMsg=None
		return True
		
	def moveCardSlowly(self,moveCard,toLocation):
		#it will in to do list !
		#now just move straitly
		self.screen.fill((0x00, 0xb0, 0x00))
		moveCard.moveCard(toLocation[0],toLocation[1])
		self.drawCardsInHand()              
		self.showNames()             
		pygame.display.flip()
		pygame.time.delay(500)
		
	def drawCardsInHand(self):
		#draw cards of player1    
		self.player1.refreshHand(self.screen)
		#draw cards of player2
		self.player2.refreshHand(self.screen)
		#draw cards of player3
		self.player3.refreshHand(self.screen)        
		#draw cards of player4
		self.player4.refreshHand(self.screen) 

	def showNames(self):
		"""print players name"""
		font = pygame.font.Font(None, 20)
		textPlayer1 = font.render(self.player1.name, 1, (10, 10, 10))
		
		textPlayer2 = font.render(self.player2.name, 1, (10, 10, 10))
		
		textPlayer3 = font.render(self.player3.name, 1, (10, 10, 10))
		
		textPlayer4 = font.render(self.player4.name, 1, (10, 10, 10))
		
		textScoreBoard = font.render("Esc to go score board", 1, (10, 10, 10))
		
		self.screen.blit(textScoreBoard, (5,430))
		
		self.screen.blit(textPlayer1, (10,43))
		self.screen.blit(textPlayer2, (375,10))
		self.screen.blit(textPlayer3, (420,340))
		self.screen.blit(textPlayer4, (40,360))
		self.showbids()
		self.showgeneral()
		

	def textcardnumber(self,cardnum):
		if cardnum==1:
			return "2"
		if cardnum==2:
			return "3"
		if cardnum==3:
			return "4"
		if cardnum==4:
			return "5"
		if cardnum==5:
			return "6"
		if cardnum==6:
			return "7"
		if cardnum==7:
			return "8"
		if cardnum==8:
			return "9"
		if cardnum==9:
			return "10"
		if cardnum==10:
			return "Jack"
		if cardnum==11:
			return "Queen"
		if cardnum==12:
			return "King"
		if cardnum==13:
			return "Ace"			

	def textsuite(self,suite):
		if suite==1:
			return "Hearts"
		if suite==2:
			return "Spades"
		if suite==3:
			return "Diamonds"
		if suite==4:
			return "Clubs"
		if suite==5:
			return "No Trump"			

	def showbids(self):
		"""print bids during the bidding phase name"""
		font = pygame.font.Font(None, 20)
		fontColorPlayer1=(0, 0, 0)
		fontColorPlayer2=(0, 0, 0)
		fontColorPlayer3=(0, 0, 0)
		fontColorPlayer4=(0, 0, 0)

		if self.player1.currentbidnumber ==0:
			textPlayer1 = font.render("pass", 1, fontColorPlayer1)
		elif self.player1.currentbidnumber==None:
			textPlayer1 = font.render("has not bid", 1,fontColorPlayer1)
		else:
			#textPlayer1 = font.render("%d %s" % (self.player1.currentbidnumber, self.textsuite(self.player1.currentbidsuite), ), 1, (10, 10, 10))
			bid = "%d %s" % (self.player1.currentbidnumber, self.textsuite(self.player1.currentbidsuite), )
			textPlayer1 = font.render(bid, 1, fontColorPlayer1)

		if self.player2.currentbidnumber ==0:
			textPlayer2 = font.render("pass", 1, fontColorPlayer2)
		elif self.player2.currentbidnumber==None:
			textPlayer2 = font.render("has not bid", 1, fontColorPlayer2)
		else:
			bid = "%d %s" % (self.player2.currentbidnumber, self.textsuite(self.player2.currentbidsuite), )
			textPlayer2 = font.render(bid, 1, fontColorPlayer2)

		if self.player3.currentbidnumber ==0:
			textPlayer3 = font.render("pass", 1, fontColorPlayer3)
		elif self.player3.currentbidnumber==None:
			textPlayer3 = font.render("has not bid", 1, fontColorPlayer3)			
		else:
			#textPlayer3 = font.render("%d %s" % (self.player3.currentbidnumber, self.textsuite(self.player3.currentbidsuite), ), 1, (10, 10, 10))
			bid = "%d %s" % (self.player3.currentbidnumber, self.textsuite(self.player3.currentbidsuite), )
			textPlayer3 = font.render(bid, 1, fontColorPlayer3)
			
		if self.player4.currentbidnumber ==0:
			textPlayer4 = font.render("pass", 1, fontColorPlayer4)
		elif self.player4.currentbidnumber==None:
			textPlayer4 = font.render("has not bid", 1, fontColorPlayer4)			
		else:
			#textPlayer4 = font.render("%d %s" % (self.player4.currentbidnumber, self.textsuite(self.player4.currentbidsuite), ), 1, (10, 10, 10))
			bid = "%d %s" % (self.player4.currentbidnumber, self.textsuite(self.player4.currentbidsuite), )
			textPlayer4 = font.render(bid, 1, fontColorPlayer4)
			#self.screen.blit(textPlayer1, (10,43))
		#if self.Napoleon!=None:
		#	if self.Napoleon==1:
		#		self.screen.blit(textPlayer1, (10,28))
		#	if self.Napoleon==2:
		#		self.screen.blit(textPlayer2, (375,23))
		#	if self.Napoleon==3:
		#		self.screen.blit(textPlayer3, (420,353))
		#	if self.Napoleon==4:
		#		self.screen.blit(textPlayer4, (40,375))	
		#else:
		self.screen.blit(textPlayer1, (10,28))
		self.screen.blit(textPlayer2, (375,23))
		self.screen.blit(textPlayer3, (420,353))
		self.screen.blit(textPlayer4, (40,375))
		
	def showgeneral(self):
		"""print general card for the napoleon"""
		font = pygame.font.Font(None, 20)

		fontColor=(0, 0, 0)
		if self.Napoleon==1:
			if self.GeneralCardNumber!=None:
				general = "%s of %s" % (self.textcardnumber(self.GeneralCardNumber), self.textsuite(self.GeneralCardSuite), )
				textPlayer = font.render(general,1 , fontColor)
				self.screen.blit(textPlayer, (10,13))
		if self.Napoleon==2:
			if self.GeneralCardNumber!=None:
				general = "%s of %s" % (self.textcardnumber(self.GeneralCardNumber), self.textsuite(self.GeneralCardSuite), )
				textPlayer = font.render(general,1 , fontColor)
				self.screen.blit(textPlayer, (375,38))
		if self.Napoleon==3:
			if self.GeneralCardNumber!=None:
				general = "%s of" % (self.textcardnumber(self.GeneralCardNumber), )
				textPlayer = font.render(general,1 , fontColor)
				self.screen.blit(textPlayer, (420,365))
				general = "%s" % (self.textsuite(self.GeneralCardSuite), )
				textPlayer = font.render(general,1 , fontColor)
				self.screen.blit(textPlayer, (420,375))				
		if self.Napoleon==4:
			if self.GeneralCardNumber!=None or self.GeneralCardSuite!=None:
				if self.GeneralCardNumber==None:
					general = "%s of %s" % (self.GeneralCardNumber, self.textsuite(self.GeneralCardSuite), )
				elif self.GeneralCardSuite==None:
					general = "%s of %s" % (self.textcardnumber(self.GeneralCardNumber), self.GeneralCardSuite, )
				else:
					general = "%s of %s" % (self.textcardnumber(self.GeneralCardNumber),self.textsuite(self.GeneralCardSuite), )
				textPlayer = font.render(general,1 , fontColor)
				self.screen.blit(textPlayer, (40,390))
			elif self.tmpGeneralCardNumber!=None or self.tmpGeneralCardSuite!=None:
				if self.tmpGeneralCardNumber==None:
					general = "%s of %s" % (self.tmpGeneralCardNumber, self.textsuite(self.tmpGeneralCardSuite), )
				elif self.tmpGeneralCardSuite==None:
					general = "%s of %s" % (self.textcardnumber(self.tmpGeneralCardNumber), self.tmpGeneralCardSuite, )
				else:
					general = "%s of %s" % (self.textcardnumber(self.tmpGeneralCardNumber),self.textsuite(self.tmpGeneralCardSuite), )
				textPlayer = font.render(general,1 , fontColor)
				self.screen.blit(textPlayer, (40,390))
				
				

	def showMessage(self,message,error=False):
		font = pygame.font.Font(None, 20)
		text = font.render(message, 1, (10, 10, 10))
		textpos = text.get_rect()
		textpos.centerx = self.screen.get_rect().centerx
		if error==False:
		    self.screen.blit(text, (30,410))
		elif error==True:
		    self.screen.blit(text, (40,450))

	def addPlayedCards(self,cardP1,cardP2,cardP3,cardP4):
		self.playedCards.append([cardP1,cardP2,cardP3,cardP4])
		
	def playAgain(self):
		self.playedCards=[]
		self.tmpPlayedCard=[]
		cc=cards()
		self.numOfDeckPlay=0
		
		#save players result
		resultPlayer1=0
		resultPlayer2=0
		resultPlayer3=0
		resultPlayer4=0

		#check if this is first Play scape
		if self.player1!=None:
			resultPlayer1=self.player1.result
			resultPlayer2=self.player2.result
			resultPlayer3=self.player3.result
			resultPlayer4=self.player4.result
		
		self.player1=Player(self.playerName[0],0);
		self.player2=Player(self.playerName[1],1);
		self.player3=Player(self.playerName[2],2);
		self.player4=Player(self.playerName[3],3,True)
		
		#set Last players Result
		self.player1.result=resultPlayer1
		self.player2.result=resultPlayer2
		self.player3.result=resultPlayer3
		self.player4.result=resultPlayer4
		
		cc.deck(self.player1, self.player2, self.player3, self.player4)
		self.putGround(self.player1,self.player2,self.player3,self.player4)   
		
		
		self.Napoleon=None
		self.General=None
		self.bidnumber=None
		self.bidsuite=None
		self.GeneralCardNumber=None
		self.GeneralCardSuite=None
		self.tmpGeneralCardNumber=None
		self.tmpGeneralCardSuite=None

		self.currentbidwinner=None
		self.currentbidnumber=None
		self.currentbidsuite=None
		
		self.playerspassedbid=0
		self.turnBid=0
		
		#randomly select the first person to bid
		random.seed()
		self.turnBid = random.randint(1, 4)
		print "player %d starts the bidding" % (self.turnBid, )
		
		self.turnPlay=0
		#check how has card 2 Clubs to first play
		#if self.player1.has2Clubs==True:
		#	self.turnPlay=1
		#if self.player2.has2Clubs==True:
		#	self.turnPlay=2
		#if self.player3.has2Clubs==True:
		#	self.turnPlay=3
		#if self.player4.has2Clubs==True:
		#	self.turnPlay=4

	def putGround(self,player1,player2,player3,player4):
		
		#sort hands of player1
		#player1.sortHande()
		#put cards of player1
		for i in range(0,13):  
			#background=player1.getCardImg(i) 
			player1.moveAndShowCard(i,screenPlayer1[i][0],screenPlayer1[i][1],self.screen)
			 #self.screen.blit(background, (screenPlayer1[i][0], screenPlayer1[i][1]))

		#sort hands of player2
		#player2.sortHande()                 
		#put cards of player2
		for i in range(0,13):        
			player2.moveAndShowCard(i,screenPlayer2[i][0], screenPlayer2[i][1],self.screen)

		
		#sort hands of player3
		#player3.sortHande()
		#put cards of player3
		for i in range(0,13):        
			player3.moveAndShowCard(i,screenPlayer3[i][0], screenPlayer3[i][1],self.screen)

		#sort hands of player4
		player4.sortHande()
		#put cards of player4
		for i in range(0,13):
			player4.moveAndShowCard(i,screenPlayer4[i][0], screenPlayer4[i][1],self.screen)
		

	def moveOut(self,card):
		card.moveCard(600, 600)
		
	def getCard(self,x,y):
		for i in range(len(self.player4.cardsInHand)-1,-1,-1)  :
			if self.player4.cardsInHand[i].rect.collidepoint(x, y):
				fc = self.player4.cardsInHand[i]
				return fc
		return None

	    
	def scoreBoardDialog(self):    
		"""show Board Dialog"""
		bimg,tmp=load_image("background.png")
		font = pygame.font.Font(None, 20)
		self.screen.blit(bimg, (0,0))
		textPlayer1 = font.render(self.player1.name, 1, (10, 10, 10))
		self.screen.blit(textPlayer1, (5,45))       
		
		textPlayer2 = font.render(self.player2.name, 1, (10, 10, 10))
		self.screen.blit(textPlayer2, (95,45))       

		textPlayer3 = font.render(self.player3.name, 1, (10, 10, 10))
		self.screen.blit(textPlayer3, (172,45))       

		textPlayer4 = font.render(self.player4.name, 1, (10, 10, 10))
		self.screen.blit(textPlayer4, (270,45)) 
		if self.blink>=0 and self.blink<=5:
		    textBackGame = font.render("Press Enter to Return to the Game ...", 1, (0, 0, 0))
		    self.screen.blit(textBackGame, (5,10)) 
		
		self.showcredits ()
		xLocation=75
		#self.NapoleonsANDBids.append([self.bidnumber,self.Napoleon])
		#show players score 
		for scores in self.scoreBoard:
			fontColorPlayer1=(0, 0, 0)
			fontColorPlayer2=(0, 0, 0)
			fontColorPlayer3=(0, 0, 0)
			fontColorPlayer4=(0, 0, 0)
			minScore=scores[0]
			self.result=0
			
			if scores[5]  == 1:
				self.result=scores[0]
			if scores[5]  == 2:
				self.result=scores[1]
			if scores[5]  == 3:
				self.result=scores[2]
			if scores[5]  == 4:
				self.result=scores[3]
				
			if scores[6]  == 1 and scores[5]  != 1:
				self.result=self.result+scores[0]
			if scores[6]  == 2 and scores[5]  != 2:
				self.result=self.result+scores[1]
			if scores[6]  == 3 and scores[5]  != 3:
				self.result=self.result+scores[2]
			if scores[6]  == 4 and scores[5]  != 4:
				self.result=self.result+scores[3]
				
				
			#if scores[0]>=scores[1] and scores[0]>=scores[2] and scores[0]>=scores[3]:
			if scores[5]  == 1 or scores[6]  == 1:
				if self.result >= scores[4]:
					fontColorPlayer1=(35, 20, 234)
				else:
					fontColorPlayer1=(234, 20, 35)
				if scores[5]  == 1:
					textScoresPlayer1 = font.render("%d [%d]" % (scores[0], scores[4] ), 1, fontColorPlayer1)
				else:
					textScoresPlayer1 = font.render(scores[0].__str__(), 1, fontColorPlayer1)
			else:
				textScoresPlayer1 = font.render(scores[0].__str__(), 1, fontColorPlayer1)

			#if scores[1]>=scores[0] and scores[1]>=scores[2] and scores[1]>=scores[3]:
			if scores[5] == 2 or  scores[6] == 2 :
				if self.result>=scores[4]:
					fontColorPlayer2=(35, 20, 234)
				else:
					fontColorPlayer2=(234, 20, 35)
				if scores[5]  == 2:
					textScoresPlayer2 = font.render("%d [%d]" % (scores[1], scores[4] ), 1, fontColorPlayer2)
				else:
					textScoresPlayer2 = font.render(scores[1].__str__(), 1, fontColorPlayer2)
			else:
				textScoresPlayer2 = font.render(scores[1].__str__(), 1, fontColorPlayer2)

			if scores[5] == 3 or  scores[6] == 3 :
				if self.result>=scores[4]:
					fontColorPlayer3=(35, 20, 234)
				else:
					fontColorPlayer3=(234, 20, 35)
				if scores[5]  == 3:
					textScoresPlayer3 = font.render("%d [%d]" % (scores[2], scores[4] ), 1, fontColorPlayer3)
				else:
					textScoresPlayer3 = font.render(scores[2].__str__(), 1, fontColorPlayer3)
			else:
				textScoresPlayer3 = font.render(scores[2].__str__(), 1, fontColorPlayer3)

			if scores[5] == 4 or scores[6] == 4:
				if self.result>=scores[4]  :
					fontColorPlayer4=(35, 20, 234)
				else:
					fontColorPlayer4=(234, 20, 35)
				if scores[5]  == 4:
					textScoresPlayer4 = font.render("%d [%d]" % (scores[3], scores[4] ), 1, fontColorPlayer4)
				else:
					textScoresPlayer4 = font.render(scores[3].__str__(), 1, fontColorPlayer4)
			else:
				textScoresPlayer4 = font.render(scores[3].__str__(), 1, fontColorPlayer4)
				
			
			self.screen.blit(textScoresPlayer1, (30,xLocation))       

			#textScoresPlayer2 = font.render(scores[1].__str__(), 1, fontColorPlayer2)
			self.screen.blit(textScoresPlayer2, (115,xLocation))       

			#textScoresPlayer3 = font.render(scores[2].__str__(), 1, fontColorPlayer3)
			self.screen.blit(textScoresPlayer3, (200,xLocation))       

			#textScoresPlayer4 = font.render(scores[3].__str__(), 1, fontColorPlayer4)
			self.screen.blit(textScoresPlayer4, (285,xLocation))  
			xLocation+=20

		if self.player1.result>=100 or self.player2.result>=100 or self.player3.result>=100 or self.player4.result>=100 :
			if self.blink>=0 and self.blink<=5:
				textEndGame = font.render("End of game Esc to play again ", 1, (255, 0, 0))
				self.screen.blit(textEndGame, (10,430)) 


	def playerchoiceDialog(self):
		"""show starting player number dialog Dialog"""
		bimg,tmp=load_image("background2.png")
		font = pygame.font.Font(None, 20)
		self.screen.blit(bimg, (0,0))
		
		textAbout = font.render("Select the number of players, press 4 or 5 ...", 1, (0, 0, 0))
		self.screen.blit(textAbout, (50,10)) 


	def introDialog(self):
		"""show rule and title Dialog"""
		bimg,tmp=load_image("background2.png")
		font = pygame.font.Font(None, 20)
		self.screen.blit(bimg, (0,0))
		self.showcredits()
		textAbout = font.render("The Rules / Dev Notes:", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,10)) 
		textAbout = font.render("1.The Point is to get Points", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,25)) 
		textAbout = font.render("2.Bidding and General Cards have been introduced", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,40)) 
		textAbout = font.render("3.The cards go A(sp), J(hr), J(di),", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,55)) 
		textAbout = font.render("   2(if all follow suite), Highest Trump(hr),", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,70)) 
		textAbout = font.render("   highest card", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,85)) 
		textAbout = font.render("4.scoreboard resets ever 10 games", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,100)) 
		textAbout = font.render("5.Computer players still think they are playing hearts", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,115)) 
		textAbout = font.render("6.This project has been incredibly informative", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,130)) 
		textAbout = font.render("7.Many thanks to python, pyGames, pyHearts", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,145)) 
		textAbout = font.render(" and Milad Rastianwithout which/whom this might", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,160)) 
		textAbout = font.render(" never have been created", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,175)) 
		textAbout = font.render("as well as the NNHS crew, you know who you are", 1, (0, 0, 0))
		self.screen.blit(textAbout, (10,190)) 
		
	def showcredits(self):
		font = pygame.font.Font(None, 20)

		textAbout = font.render("PyNapoleon", 1, (14, 58, 17))
		self.screen.blit(textAbout, (280,265)) 

		textAbout = font.render("Developer: Guy Mann", 1, (14, 58, 17))
		self.screen.blit(textAbout, (280,280)) 
		
		textAbout = font.render("guydmann@gmail.com", 1, (14, 58, 17))
		self.screen.blit(textAbout, (280,295))        
		
		textAbout = font.render("based on code from pyHearts", 1, (14, 58, 17))
		self.screen.blit(textAbout, (280,310)) 
		
		textAbout = font.render("by Milad Rastian", 1, (14, 58, 17))
		self.screen.blit(textAbout, (280,325)) 
		
		textAbout = font.render("Version : 2.0.0", 1, (14, 58, 17))
		self.screen.blit(textAbout, (320,340))

		textAbout = font.render("License : GPL", 1, (14, 58, 17))
		self.screen.blit(textAbout, (320,355))        
		
		
	def backToGame(self):
		"""back to game"""
		self.ShowScoreBoardDialog=False
		#self.bidnumber=0
		#self.bidsuite=0
		if self.player1.result>=100 or self.player2.result>=100 or self.player3.result>=100 or self.player4.result>=100 :
			self.scoreBoard=[]
			self.player1.result=0
			self.player2.result=0
			self.player3.result=0
			self.player4.result=0
			self.playAgain()

def main():
	g = background()

	 
	      
