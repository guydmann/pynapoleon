#!/usr/bin/env python
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

from inits import  *

class Player:

	def __init__(self,name="",location=0,isHuman=False):
		self.isHuman=isHuman
		self.cardsInHand=[]
		self.currentPlay=None
		self.isGeneral=False
		self.isNapoleon=False
		self.hasAceSpades=False
		self.hasJackOfTrump=False
		self.hasJackOfColor=False
		self.has2Clubs=False
		self.hasQueenSpades=False
		self.isPlayHeart=False
		self.isQueenSpadesPlayed=False
		self.result=0
		self.allDeckResult=0
		self.name=name
		self.locationInPlayedCard=location
		self.tryDontPlayHearts=False
		self.tryDontPlaySpades=False
		self.tryDontPlayDaimond=False
		self.tryDontPlayClubs=False
		self.tryGetHearts=False
		self.result=0
		self.tmpResult=0
		self.currentbidnumber=None
		self.currentbidsuite=None
		


	def addHand(self,card):
		self.cardsInHand.append(card)
		card.index=len(self.cardsInHand)-1
		if card.name==cardNumber.Ace and card.type==cardType.Spades:
			self.hasAceSpades=True
		#if card.name==cardNumber.queen and card.type==cardType.Spades:
		#	self.hasQueenSpades=True
			
	def analayzLastDeck(self,playedCard):

		#there is not any thing to analayz, dont waste my players time :P ;)
		if self.tryDontPlayHearts==True and self.tryDontPlayClubs==True and self.tryDontPlayDaimond==True and self.tryDontPlaySpades==True:
		    return 
		for cards in playedCard:

			#check if in the last paly analayz dont do that again
			if cards[self.locationInPlayedCard].type==cardType.Hearts and self.tryDontPlayHearts==True:
				break
			if cards[self.locationInPlayedCard].type==cardType.Clubs and self.tryDontPlayClubs==True:
				break
			if cards[self.locationInPlayedCard].type==cardType.Daimond and self.tryDontPlayDaimond==True:
				break                
			if cards[self.locationInPlayedCard].type==cardType.Spades and self.tryDontPlaySpades==True:
				break    

			#checks for anyone who has broken suite
			#if someone broke suite it sets the tryDontPlay variable for that suite to attempt to not give that person a change to trump
			#this might be improved by checking if that they are out if is trump in which case you might change your strategy
			for card in cards:
				tryDontPlayType=False
				
				#check if know it players card dont check it            
				if card.type==cards[self.locationInPlayedCard].type and card.name==cards[self.locationInPlayedCard].name :
					continue
				if card.type!=cards[self.locationInPlayedCard].type:
					tryDontPlayType=True
				else:
					tryDontPlayType=False
			if tryDontPlayType==True:
				if cards[self.locationInPlayedCard].type==cardType.Hearts:
					self.tryDontPlayHearts=True
				elif cards[self.locationInPlayedCard].type==cardType.Clubs:
					self.tryDontPlayClubs=True
				elif cards[self.locationInPlayedCard].type==cardType.Daimond:
					self.tryDontPlayDaimond=True
				elif cards[self.locationInPlayedCard].type==cardType.Spades:
					self.tryDontPlaySpades=True
			pass
	def analayzPlayer(self,playedCard):
		for cards in playedCard:
			pass

	def analayzHand(self,trump,GeneralCardNumber=None, GeneralCardSuite=None):
		#used after the trump suite has been decided
		#self.hasJackOfTrump=False
		#self.hasJackOfColor=False
		if (trump==1):
			coloralt = 3
		if (trump==2):
			coloralt = 4			
		if (trump==3):
			coloralt = 1			
		if (trump==4):
			coloralt = 2
		if (trump==5):
			coloralt = 5
		for card in self.cardsInHand:
			if card.type==trump and card.name==10:
				self.hasJackOfTrump=True
			if card.type==coloralt and card.name==10:
				self.hasJackOfColor=True
			#the check for the Ace of space really isn't needed here, but once the pot is implemented it will be 
			#because you could pick up the Ace, or you could throw it away.. though you wouldn't
			if card.name==cardNumber.Ace and card.type==cardType.Spades:
				self.hasAceSpades=True
			if GeneralCardNumber!=None and GeneralCardSuite!=None:	
				if card.name==GeneralCardNumber and card.type==GeneralCardSuite:	
					self.isGeneral=True


	def selectGeneralCard(self):
		self.selectedGeneralCard=[]
		if self.hasAceSpades==False:
			self.selectedGeneralCard=[13,2]
		elif self.hasJackOfTrump==False:
			self.selectedGeneralCard=[10,self.currentbidsuite]
		elif self.hasJackOfColor==False:
			if (self.currentbidsuite==1):
				coloralt = 3
			if (self.currentbidsuite==2):
				coloralt = 4			
			if (self.currentbidsuite==3):
				coloralt = 1			
			if (self.currentbidsuite==4):
				coloralt = 2
			if (self.currentbidsuite==5):
				coloralt = 5
			self.selectedGeneralCard=[10,coloralt]	
		else:
			for i in range (13,2):
				hasCard=False
				for card in self.cardsInHand:
					if card.type==self.currentbidsuite and card.name==i:
						hasCard=True
						break
				if hasCard==False:
					self.selectedGeneralCard=[i,self.currentbidsuite]	
					break
			if len(self.selectedGeneralCard)==0:
				for i in range (13,2):
					hasCard=False
					inSuite=None
					for j in range (1,4):
						for card in self.cardsInHand:
							if card.type==j and card.name==i:
								hasCard=True
								inSuite=j
								break
						if hasCard==False:
							self.selectedGeneralCard=[i,j]	
							break
		return self.selectedGeneralCard
	
	
	
	def bid(self,currentbidnumber,currentbidsuite,Players):
		self.maxbid=0
		self.maxbidsuite=0
		self.suitevalues = [0, 0, 0,0]
		for i in range(1,4):
			if (i==1):
				coloralt = 3
			if (i==2):
				coloralt = 4			
			if (i==3):
				coloralt = 1			
			if (i==4):
				coloralt = 2
			if (i==5):
				coloralt = 5
			j=i-1
			for card in self.cardsInHand:
				if card.type==cardType.Spades and card.name==cardNumber.Ace:
					#self.suitevalue = self.suitevalue + 1
					self.suitevalues[0] = self.suitevalues[0] +1
					self.suitevalues[1] = self.suitevalues[1] +1
					self.suitevalues[2] = self.suitevalues[2] +1
					self.suitevalues[3] = self.suitevalues[3] +1
				if card.name==2:
					self.suitevalues[0] = self.suitevalues[0] +1
					self.suitevalues[1] = self.suitevalues[1] +1
					self.suitevalues[2] = self.suitevalues[2] +1
					self.suitevalues[3] = self.suitevalues[3] +1
				if card.type==coloralt and card.name==cardNumber.jack:
					self.suitevalues[j] = self.suitevalues[j] + 1
				if card.type==i:
					if card.name<9:
						self.suitevalues[j] = self.suitevalues[j] + 1
					if card.name>=9:
						self.suitevalues[j] = self.suitevalues[j] + 1
					if card.name==cardNumber.jack:
						self.suitevalues[j] = self.suitevalues[j] + 1
				else:
					if card.name>=9:
						self.suitevalues[j] = self.suitevalues[j] + .5
			#print "%d" % (self.suitevalues[j] ,)
			if self.suitevalues[j]>self.maxbid:
				self.maxbid=self.suitevalues[j]
				self.maxbidsuite=i
		if self.maxbid>currentbidnumber:
			#self.currentbidnumber=self.maxbid
			#self.currentbidsuite=self.maxbidsuite
			self.currentbidnumber=round(self.maxbid,0)
			self.currentbidsuite=self.maxbidsuite
		else:
			self.currentbidnumber=0
			self.currentbidsuite=0
		return self.currentbidnumber
		
		
	
		
	def WillIWin(self,cardInGround,testcard, trump):
		#cardInGround: list of the cards already played
		#testcard: the card which we are thinking of playing
		#Returns True if the card passed as testcard will beat all cards already played
		#Returns False if the card won't win
		
		#if you play the ace of spades you win the hand, easy short circuit
		if (testcard.type==2 and testcard.name==cardNumber.Ace):
			return True
		
		startingsuit=cardInGround[0][0].type
		if (trump==1):
			coloralt = 3
		if (trump==2):
			coloralt = 4			
		if (trump==3):
			coloralt = 1			
		if (trump==4):
			coloralt = 2
		if (trump==5):
			coloralt = 5		
		for card in cardInGround:
			#if someone plays the ace of spades they win the hand
			if (card.type==2 and card.name==cardNumber.Ace):
				return False
			#test for the jack of trump
			if (card.type==trump and card.name==cardNumber.jack):
				#if you're not playing the Ace of Spades then you lose
				if (testcard.type!=2 and testcard.name!=cardNumber.Ace):
					return False
			#test for the jack of color
			if (card.type==coloralt and card.name==cardNumber.jack):
				#if you're not playing the Ace of spades or the jack of trump then you lose
				if (testcard.type!=2 and testcard.name!=cardNumber.Ace) or (card.type!=trump and card.name!=cardNumber.jack):
					return False
			#if a trump is played and you are not playing trump thenyou will lose
			if (card.type==trump and testcard.type!=trump):
				#if you're not playing the Ace of spades or the jack of trump, or the jack of color  then you lose
				if (testcard.type!=2 and testcard.name!=cardNumber.Ace) or (card.type!=trump and card.name!=cardNumber.jack) or (testcard.type!=coloralt and testcard.name!=cardNumber.jack):
					return False
			if (card.type==trump and testcard.type==trump and card.name>testcard.name):
				#if you're not playing the Ace of spades or the jack of trump, or the jack of color  then you lose
				if (testcard.type!=2 and testcard.name!=cardNumber.Ace) or (card.type!=trump and card.name!=cardNumber.jack) or (testcard.type!=coloralt and testcard.name!=cardNumber.jack):
					return False
			if (card.type==startingsuit and testcard.type==startingsuit and card.name>testcard.name):
				if (testcard.type!=2 and testcard.name!=cardNumber.Ace) or (card.type!=trump and card.name!=cardNumber.jack) or (testcard.type!=coloralt and testcard.name!=cardNumber.jack):
					return False
#NEED TO ADD TEST FOR 2s					
		return True
		
	def WhoWillWin(self,cardInGround,testcard, trump):
		#cardInGround: list of the cards already played
		#testcard: the card which we are thinking of playing
		#Returns the player number of the person who will currently win the hand
		
		#if you play the ace of spades you win the hand, easy short circuit
		
		#self.locationInPlayedCard	
		
		if (testcard.type==2 and testcard.name==cardNumber.Ace):
			return self.locationInPlayedCard
			
		#number of cards played - players location modulous 4 tells us who started
		playerwhostarted=(len(cardInGround)-self.locationInPlayedCard)%4		
		startingsuit=cardInGround[0][0].type
		
		if (trump==1):
			coloralt = 3
		if (trump==2):
			coloralt = 4			
		if (trump==3):
			coloralt = 1			
		if (trump==4):
			coloralt = 2
		if (trump==5):
			coloralt = 5		
		cardnum=0
		currentwinner = playerwhostarted
		for card in cardInGround:
			
			#if someone plays the ace of spades they win the hand
			if (card.type==2 and card.name==cardNumber.Ace):
				currentwinner = cardnum + playerwhostarted
				return currentwinner
				#have to stop.. can't concentrate anymore
			#test for the jack of trump
			if (card.type==trump and card.name==cardNumber.jack):
				#if you're not playing the Ace of Spades then you lose
				if (testcard.type!=2 and testcard.name!=cardNumber.Ace):
					return cardnum + playerwhostarted
			#test for the jack of color
			if (card.type==coloralt and card.name==cardNumber.jack):
				#if you're not playing the Ace of spades or the jack of trump then you lose
				if (testcard.type!=2 and testcard.name!=cardNumber.Ace) or (card.type!=trump and card.name!=cardNumber.jack):
					return False
			#if a trump is played and you are not playing trump thenyou will lose
			if (card.type==trump and testcard.type!=trump):
				#if you're not playing the Ace of spades or the jack of trump, or the jack of color  then you lose
				if (testcard.type!=2 and testcard.name!=cardNumber.Ace) or (card.type!=trump and card.name!=cardNumber.jack) or (testcard.type!=coloralt and testcard.name!=cardNumber.jack):
					return False
			if (card.type==trump and testcard.type==trump and card.name>testcard.name):
				#if you're not playing the Ace of spades or the jack of trump, or the jack of color  then you lose
				if (testcard.type!=2 and testcard.name!=cardNumber.Ace) or (card.type!=trump and card.name!=cardNumber.jack) or (testcard.type!=coloralt and testcard.name!=cardNumber.jack):
					return False
			if (card.type==startingsuit and testcard.type==startingsuit and card.name>testcard.name):
				if (testcard.type!=2 and testcard.name!=cardNumber.Ace) or (card.type!=trump and card.name!=cardNumber.jack) or (testcard.type!=coloralt and testcard.name!=cardNumber.jack):
					return False
#NEED TO ADD TEST FOR 2s					
			cardnum = cardnum+1
		return cardnum-1
		
	def PointsPlayed(self,cardInGround):
	#returns the number of points played in this hand so far
	#does this by looping through what each player has played
		pointsplayed=0
		for j in range(0,len(cardInGround)):
			if cardInGround[j][0].name>=9:
				pointsplayed=pointsplayed+1
		print "points played: %d\n" % (pointsplayed ,)
		return pointsplayed
		
	def play(self,cardInGround,playedCard,numOfDeckPlay,Players,Bid,Trump, Napoleon, General):
		return self.playStratN1(cardInGround,playedCard,numOfDeckPlay,Players,Bid,Trump, Napoleon, General)

	

	def playStratN1(self,cardInGround,playedCard,numOfDeckPlay,Players,Bid,Trump, Napoleon, General):
		retcard=None
		self.analayzLastDeck(playedCard)
		pointsplayed=0
		
		if self.isNapoleon==True:
			#player is his own general
			#this code won't be used until there is a pot because the computer user will currently never pick one of their cards as general
			if self.isGeneral==True:
				#if there are cards already played
				if len(cardInGround)!=0:
					if self.hastThisType(cardInGround[0][0].type)==True:
						#now try to play bigger One
						maxCardToPlay=0
						for card in self.cardsInHand:
							if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
								maxCardToPlay=card.name
								retcard=card
						if retcard:
							if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
								return self.setAsPlay(retcard)
							else:
								retcard=None
					else:
						#now has not this type try to play small card but no play hearts
						minCardToPlay=15
						for card in self.cardsInHand:
							if card.type==cardType.Hearts:
							       continue
							if card.name<minCardToPlay and card.isPlayed==False:
							       minCardToPlay=card.name
							       retcard=card
						if retcard:
							if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							       return self.setAsPlay(retcard)
							else:
							       retcard=None
				else:
					#here we will need to determine how far along the game is and then figure out what we can let go of
					#for now however it is being dumb and going to play a high card.  this will need to be changed. but i want to get it up and running
					maxCardToPlay=0
					for card in self.cardsInHand:
						if card.isPlayed==False and card.name>maxCardToPlay :
							maxCardToPlay=card.name
							retcard=card
					if retcard:
						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							return self.setAsPlay(retcard)
						else:
							retcard=None
					
		
			#player is napoleon and the general is known
			elif General!=None:
				if len(cardInGround)!=0:
					pointsplayed=self.PointsPlayed(cardInGround)
					#tests to see if the player has the suite of the first card
					#does the player have to follow suite
					if self.hastThisType(cardInGround[0][0].type)==True:
						if pointsplayed>0 or len(cardInGround)<2:
							#if there are points played then we try and play higher
							maxCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									maxCardToPlay=card.name
									retcard=card
						else:
							minCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									maxCardToPlay=card.name
									retcard=card
					else:
					#player does not have the starting suite thus doesn't have to follow suite
						#now has not this type try to play small card but no play hearts
						minCardToPlay=15
						for card in self.cardsInHand:
							if card.type==cardType.Hearts:
							       continue
							if card.name<minCardToPlay and card.isPlayed==False:
							       minCardToPlay=card.name
							       retcard=card
						if retcard:
							if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							       return self.setAsPlay(retcard)
							else:
							       retcard=None
				else:
					#here we will need to determine how far along the game is and then figure out what we can let go of
					#for now however it is being dumb and going to play a high card.  this will need to be changed. but i want to get it up and running
					maxCardToPlay=0
					for card in self.cardsInHand:
						if card.isPlayed==False and card.name>maxCardToPlay :
							maxCardToPlay=card.name
							retcard=card
					if retcard:
						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							return self.setAsPlay(retcard)
						else:
							retcard=None
				
			#player is napoleon and the general is unknown
			else:
				if len(cardInGround)!=0:
					pointsplayed=self.PointsPlayed(cardInGround)
					#tests to see if the player has the suite of the first card
					#does the player have to follow suite
					if self.hastThisType(cardInGround[0][0].type)==True:
						if pointsplayed>0 or len(cardInGround)<2:
							#if there are points played then we try and play higher
							maxCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									maxCardToPlay=card.name
									retcard=card
						else:
							minCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									maxCardToPlay=card.name
									retcard=card
					else:
					#player does not have the starting suite thus doesn't have to follow suite
						#now has not this type try to play small card but no play hearts
						minCardToPlay=15
						for card in self.cardsInHand:
							if card.type==cardType.Hearts:
							       continue
							if card.name<minCardToPlay and card.isPlayed==False:
							       minCardToPlay=card.name
							       retcard=card
						if retcard:
							if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							       return self.setAsPlay(retcard)
							else:
							       retcard=None
				else:
					#here we will need to determine how far along the game is and then figure out what we can let go of
					#for now however it is being dumb and going to play a high card.  this will need to be changed. but i want to get it up and running
					maxCardToPlay=0
					for card in self.cardsInHand:
						if card.isPlayed==False and card.name>maxCardToPlay :
							maxCardToPlay=card.name
							retcard=card
					if retcard:
						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							return self.setAsPlay(retcard)
						else:
							retcard=None

		else:
			#player is general not napoleon
			#this code won't be used until there is a pot because the computer user will currently never pick one of their cards as general
			if self.isGeneral==True:
				if len(cardInGround)!=0:
					pointsplayed=self.PointsPlayed(cardInGround)
					#tests to see if the player has the suite of the first card
					#does the player have to follow suite
					if self.hastThisType(cardInGround[0][0].type)==True:
						if pointsplayed>0 or len(cardInGround)<2:
							#if there are points played then we try and play higher
							maxCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									maxCardToPlay=card.name
									retcard=card
						else:
							minCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									maxCardToPlay=card.name
									retcard=card
					else:
					#player does not have the starting suite thus doesn't have to follow suite
						#now has not this type try to play small card but no play hearts
						minCardToPlay=15
						for card in self.cardsInHand:
							if card.type==cardType.Hearts:
							       continue
							if card.name<minCardToPlay and card.isPlayed==False:
							       minCardToPlay=card.name
							       retcard=card
						if retcard:
							if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							       return self.setAsPlay(retcard)
							else:
							       retcard=None
				else:
					#here we will need to determine how far along the game is and then figure out what we can let go of
					#for now however it is being dumb and going to play a high card.  this will need to be changed. but i want to get it up and running
					maxCardToPlay=0
					for card in self.cardsInHand:
						if card.isPlayed==False and card.name>maxCardToPlay :
							maxCardToPlay=card.name
							retcard=card
					if retcard:
						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							return self.setAsPlay(retcard)
						else:
							retcard=None
		
			#player not napoleon or general and the general is known
			elif General!=None:
				if len(cardInGround)!=0:
					pointsplayed=self.PointsPlayed(cardInGround)
					#tests to see if the player has the suite of the first card
					#does the player have to follow suite
					if self.hastThisType(cardInGround[0][0].type)==True:
						if self.pointsplayed>0 or len(cardInGround)<2:
							#if there are points played then we try and play higher
							maxCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									maxCardToPlay=card.name
									retcard=card
						else:
							minCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									maxCardToPlay=card.name
									retcard=card
					else:
					#player does not have the starting suite thus doesn't have to follow suite
						#now has not this type try to play small card but no play hearts
						minCardToPlay=15
						for card in self.cardsInHand:
							if card.type==cardType.Hearts:
							       continue
							if card.name<minCardToPlay and card.isPlayed==False:
							       minCardToPlay=card.name
							       retcard=card
						if retcard:
							if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							       return self.setAsPlay(retcard)
							else:
							       retcard=None
				else:
					#here we will need to determine how far along the game is and then figure out what we can let go of
					#for now however it is being dumb and going to play a high card.  this will need to be changed. but i want to get it up and running
					maxCardToPlay=0
					for card in self.cardsInHand:
						if card.isPlayed==False and card.name>maxCardToPlay :
							maxCardToPlay=card.name
							retcard=card
					if retcard:
						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							return self.setAsPlay(retcard)
						else:
							retcard=None		
			#player is not napoleon and the general is unknown
			else:
				if len(cardInGround)!=0:
					pointsplayed=self.PointsPlayed(cardInGround)
					#tests to see if the player has the suite of the first card
					#does the player have to follow suite
					if self.hastThisType(cardInGround[0][0].type)==True:
						if pointsplayed>0 or len(cardInGround)<2:
							#if there are points played then we try and play higher
							maxCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									maxCardToPlay=card.name
									retcard=card
						else:
							minCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									maxCardToPlay=card.name
									retcard=card
					else:
					#player does not have the starting suite thus doesn't have to follow suite
						#now has not this type try to play small card but no play hearts
						minCardToPlay=15
						for card in self.cardsInHand:
							if card.type==cardType.Hearts:
							       continue
							if card.name<minCardToPlay and card.isPlayed==False:
							       minCardToPlay=card.name
							       retcard=card
						if retcard:
							if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							       return self.setAsPlay(retcard)
							else:
							       retcard=None
				else:
					#here we will need to determine how far along the game is and then figure out what we can let go of
					#for now however it is being dumb and going to play a high card.  this will need to be changed. but i want to get it up and running
					maxCardToPlay=0
					for card in self.cardsInHand:
						if card.isPlayed==False and card.name>maxCardToPlay :
							maxCardToPlay=card.name
							retcard=card
					if retcard:
						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							return self.setAsPlay(retcard)
						else:
							retcard=None
		if retcard==None:
		#Ok stupid ! play every thinh you want ! I dont know how much must learn you Hearts Game :P
			for i in range(0,13):
				if self.cardsInHand[i].isPlayed==False:
					if self.checkPlayCard(self.cardsInHand[i], cardInGround, numOfDeckPlay):
						retcard=self.cardsInHand[i]
		return retcard

		#this is the start of testing if we shoudl use the 2
		#if numOfDeckPlay!=0:

		#play4 try get all card do some thing!
#		if Players[3].result==18:
#			if Players[0].result==0 and Players[1].result==0 and Players[2].result==0 :
#				#play with Hearts
#				if len(cardInGround)==0:
#					MaxCardToPlay=0
#					for card in self.cardsInHand:
#						if card.isPlayed==False and card.name>MaxCardToPlay :
#							MaxCardToPlay=card.name
#							retcard=card
#					if retcard:
#						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
#							return self.setAsPlay(retcard)
#						else:
#							retcard=None
#					MaxHeartNum=0
#					for card in self.cardsInHand:
#						if card.isPlayed==False and card.name>MaxHeartNum and card.type==cardType.Hearts:
#							MaxHeartNum=card.name
#							retcard=card
#					if retcard:
#						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
#							return self.setAsPlay(retcard)
#						else:
#							retcard=None
#
#			
#			#play with bigger one or do not play with hearts
#			if len(cardInGround)!=0:
#				if self.hastThisType(cardInGround[0][0].type)==True:
#					#now try to play bigger One
#					maxCardToPlay=0
#					for card in self.cardsInHand:
#						if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
#							maxCardToPlay=card.name
#							retcard=card
#					if retcard:
#						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
#							return self.setAsPlay(retcard)
#						else:
#							retcard=None
#				else:
#					#now has not this type try to play small card but no play hearts
#					minCardToPlay=15
#					for card in self.cardsInHand:
#						if card.type==cardType.Hearts:
#						       continue
#						if card.name<minCardToPlay and card.isPlayed==False:
#						       minCardToPlay=card.name
#						       retcard=card
#					if retcard:
#						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
#						       return self.setAsPlay(retcard)
#						else:
#						       retcard=None                                              
					
					
		#check is heart or Queen of Spades play yet ?
#		self.checkIsPlayHeart(playedCard)
		#self.analayzLastDeck(playedCard)
#		self.analayzPlayer(playedCard)
		#check if game played by hearts try play by less than cards in ground


	#check card and cards in Played card on type Hearts If didnt play larger than card number palying is safe
	def checkCanPlayHearts(self,card,playedCard):
		maxHeartsPlayedCard=0
		#find max hearts play in played card
		for cards in playedCard:
			if cards[0].type==cardType.Hearts:
				if cards[0].name>maxHeartsPlayedCard:
					maxHeartsPlayedCard=cards[0].name
			if cards[1].type==cardType.Hearts:
				if cards[1].name>maxHeartsPlayedCard:
					maxHeartsPlayedCard=cards[1].name
			if cards[2].type==cardType.Hearts:
				if cards[2].name>maxHeartsPlayedCard:
					maxHeartsPlayedCard=cards[2].name
			if cards[3].type==cardType.Hearts:
				if cards[2].name>maxHeartsPlayedCard:
					maxHeartsPlayedCard=cards[3].name
		#find max hearts in his hand
		for tmpCard in self.cardsInHand:
			if tmpCard.type==cardType.Hearts:
				if tmpCard>maxHeartsPlayedCard:
					maxHeartsPlayedCard=tmpCard
		if card.name<maxHeartsPlayedCard:
			return True
		return False
			
		pass

	def setAsPlay(self,card):
		card.isPlayed=True
		if card.name==cardNumber.queen and cardType.Spades==card.type:
			self.hasQueenSpades=False
		return card

	def checkIsPlayedQueen(self,playedCard):
		for i in range(0,len(playedCard)):
			for j in range(0,4):
				if playedCard[i][j].type==cardType.Spades and playedCard[i][j].name==cardNumber.queen:
					return True
		return False    

	def removeCards(self):
		self.cardsInHand

	def sortHande(self):
		for i in range(0,13):
			for j in range(0,13):
				if(self.cardsInHand[i].type>self.cardsInHand[j].type):
					tmp=self.cardsInHand[i]
					#self.cardsInHand[i]=None
					self.cardsInHand[i]=self.cardsInHand[j]
					#self.cardsInHand[j]=None
					self.cardsInHand[j]=tmp
				elif(self.cardsInHand[i].type==self.cardsInHand[j].type):
					if(self.cardsInHand[i].name<self.cardsInHand[j].name):
						tmp=self.cardsInHand[i]
						self.cardsInHand[i]=self.cardsInHand[j]
						self.cardsInHand[j]=tmp
						pass

	def playAgain(self):
		self.cardsInHand=[]
		    
	def getCard(self,index):        
		return self.cardsInHand[index]

	def moveCard(self,index,x,y):
		self.cardsInHand[index].moveCard(x,y)
			
	def showCard(self,index,screen):
		background=self.getCardImg(index)
		screen.blit(background, (self.cardsInHand[index].rect))

	def moveAndShowCard(self,index,x,y,screen):
		self.moveCard(index, x, y)
		self.showCard(index, screen)

	def moveSlowly(self,index,x,y,screen):
		self.moveAndShowCard(index, x, y, screen)

	def refreshHand(self,screen):
		for i in range(0,13):
			if self.cardsInHand[i].isPlayed==False:
				self.showCard(i, screen)
			elif self.currentPlay!=None :
				if self.currentPlay.index==i:
					self.showCard(i, screen)


	def getForentCardImg(self,index):
		cardimg,cardrct=self.cardsInHand[index].getfrontImage()
		return cardimg

	def getCardImg(self,index):                
		
		#cardimg,cardrct=self.cardsInHand[index].getfrontImage()
		#return cardimg
		
		if self.isHuman==True :
			cardimg,cardrct=self.cardsInHand[index].getfrontImage()
		elif self.currentPlay!=None :
			if self.currentPlay.index==index :
					cardimg,cardrct=self.cardsInHand[index].getfrontImage()
			else:
					cardimg,cardrct=self.cardsInHand[index].getBackImage()
		else:
			cardimg,cardrct=self.cardsInHand[index].getBackImage()
		return cardimg

	def hastThisType(self,type):   
		for i in range(0,13):
			if self.cardsInHand[i].isPlayed==False:
				if self.cardsInHand[i].type==type:
					return True
		return False

	def checkIsPlayHeart(self,playedCard):
		if self.isQueenSpadesPlayed==True and self.isPlayHeart==True :
			return 
		for i in range(0,len(playedCard)):
			for j in range(0,4):
				if playedCard[i][j].type==cardType.Hearts:
					self.isPlayHeart=True
				if playedCard[i][j].type==cardType.Spades and  playedCard[i][j].name == cardNumber.queen :
					self.isQueenSpadesPlayed=True
				if self.isQueenSpadesPlayed==True and self.isPlayHeart==True :
					return 

	def checkPlayCard(self,cardToPlay,cardInGround,numOfDeckPlay):
#		if(numOfDeckPlay==0):
#			if len(cardInGround)==0:
#				if cardToPlay.type==cardType.Clubs:
#					if cardToPlay.name==cardNumber.num2 :
#						return True
#					self.errorMsg="You Must Start Game with 2 Clubs, Come on Don't Be Stupid !"
#					return False
#				if(cardToPlay.type==cardType.Hearts):
#					self.errorMsg="In First Deck You Can not Play With Hearts, Do You Know How To Play?"
#					return False
#				if(cardToPlay.type==cardType.Spades and cardToPlay.name==cardNumber.queen):
#					self.errorMsg="In First Deck You Can Not Play With Queen Of Spades , Do You Know How To Play? "
#					return False
#		if len(cardInGround)==0:
#			if(self.isPlayHeart==False  and cardToPlay.type==cardType.Hearts):
#				self.errorMsg="You Can Not Play Hearts Now ! Take Another Card"
#				return False
#		else:
		if len(cardInGround)!=0:
			if cardToPlay.type!=cardInGround[0][0].type:
				if self.hastThisType(cardInGround[0][0].type):
					self.errorMsg="Check Your Card To Play,You Should Play Card As Type First Deck"
					return False
#		if(cardToPlay.type==cardType.Hearts) :     
#			self.isPlayHeart=True
		self.errorMsg=None
		return True
