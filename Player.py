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
		self.selectedGeneralCard=[13,2]
		if self.hasAceSpades==False:
			return self.selectedGeneralCard
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
					for card in self.cardsInHand:
						if card.name==i:
							hasCard=True
							inSuite=card.type
							break
					if hasCard==False:
						self.selectedGeneralCard=[i,inSuite]	
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
		
		
	
	def WhoWillWin(self,cardInGround,testcard, trump):
		#cardInGround: list of the cards already played
		#testcard: the card which we are thinking of playing
		#Returns the player number of the person who will currently win the hand
		
		
		
		#self.locationInPlayedCard	

			
		#number of cards played - players location modulous 4 tells us who started
		playerwhostarted=(len(cardInGround)-self.locationInPlayedCard)%4		
		startingsuit=cardInGround[0][0].type
		JackTrumpPlayed = False
		JackAltPlayed = False
		FollowedSuite = True
		TrumpPlayed = False
		Playedthe2 = None
		currentwinner = playerwhostarted
		
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
		
		#if you play the ace of spades you win the hand, easy short circuit
		if (testcard.type==1 and testcard.name==cardNumber.Ace):
			return self.locationInPlayedCard		
		for j in range(0,len(cardInGround)):
			#test for following suite
			if (cardInGround[j][0].type != startingsuit):
				FollowedSuite = False
			#test for 2
			if (cardInGround[j][0].name==1):
				Playedthe2 = j + playerwhostarted
				
			#if someone plays the ace of spades they win the hand
			if (cardInGround[j][0].type==2 and cardInGround[j][0].name==cardNumber.Ace):
				return j + playerwhostarted
			#test for the jack of trump
			elif (cardInGround[j][0].type==trump and cardInGround[j][0].name==cardNumber.jack):	
				JackTrumpPlayed= True
				currentwinner = j + playerwhostarted
				
				#in future may want to test if the Ace of spades has been played or if it can be played
			elif (cardInGround[j][0].type==coloralt and cardInGround[j][0].name==cardNumber.jack):
				JackAltPlayed = True
				if ( JackTrumpPlayed ==False):
					currentwinner = j + playerwhostarted
			elif (cardInGround[j][0].type==trump):
				TrumpPlayed = True
				if ( JackTrumpPlayed ==False and JackAltPlayed ==False ):
					if (cardInGround[currentwinner - playerwhostarted][0].type==trump):
						if (cardInGround[j][0].name>cardInGround[currentwinner - playerwhostarted][0].name):
							currentwinner = j + playerwhostarted
					else:
						currentwinner = j + playerwhostarted
			elif (cardInGround[j][0].type==startingsuit and cardInGround[j][0].name>cardInGround[currentwinner - playerwhostarted][0].name and trump!=startingsuit):
				if (JackTrumpPlayed ==False and JackAltPlayed ==False and TrumpPlayed == False):
					currentwinner = j + playerwhostarted
		if (FollowedSuite == True and JackTrumpPlayed ==False and JackAltPlayed ==False and (TrumpPlayed == False or trump==startingsuit) and Playedthe2!=None):
			currentwinner = Playedthe2
		#at this point if the test card is the jack of trump then it has to be the winner
		#this is unless there is a bug that would allow 2 players to have a juack of trump, or if the game were to be expanded to 2 decks for some reason, which in and of itself would be problematic for the rules
		if (cardInGround[j][0].type==trump and cardInGround[j][0].name==cardNumber.jack):
			return self.locationInPlayedCard
		elif (testcard.type==coloralt and testcard.name==cardNumber.jack):
			if ( JackTrumpPlayed ==False):
				return self.locationInPlayedCard
		#the cards is trump
		#it will win if the winner hasn't played trump
		#or if it's a higher trump

		elif (testcard.type==trump and trump!=startingsuit):
			if ( JackTrumpPlayed ==False and JackAltPlayed ==False ):
				if (cardInGround[currentwinner - playerwhostarted][0].type==trump):
					if (testcard.name>cardInGround[currentwinner - playerwhostarted][0].name):
						currentwinner = self.locationInPlayedCard
				else:
					currentwinner = self.locationInPlayedCard
		#if we are playing the starting suit
		#and everyone followed suite and no power cards were played including 2s
		#then if you are playing the higher card you win
		elif (testcard.type==startingsuit):
			if  ( JackTrumpPlayed ==False and JackAltPlayed ==False and FollowedSuite == True and Playedthe2 == False):		
				if (cardInGround[currentwinner - playerwhostarted][0].type==startingsuit and testcard.name>cardInGround[currentwinner - playerwhostarted][0].name):
					currentwinner = self.locationInPlayedCard
		#if you have the 2 and everyone followed suite
		#and  no power cards were played
		elif (testcard.type==startingsuit and testcard.name == 1 and FollowedSuite == True):
			#don't need to test for 2 here.. if everyone followed suite then this shoudl be the only 2
			if  ( JackTrumpPlayed ==False and JackAltPlayed ==False ):
				currentwinner = self.locationInPlayedCard
		return currentwinner
		
	def PointsPlayed(self,cardInGround):
	#returns the number of points played in this hand so far
	#does this by looping through what each player has played
		pointsplayed=0
		for j in range(0,len(cardInGround)):
			if cardInGround[j][0].name>=9:
				pointsplayed=pointsplayed+1
		#print "points played: %d\n" % (pointsplayed ,)
		return pointsplayed
		
	def play(self,cardInGround,playedCard,numOfDeckPlay,Players,Bid,Trump, Napoleon, General):
		#return self.playStratN1(cardInGround,playedCard,numOfDeckPlay,Players,Bid,Trump, Napoleon, General)
		return self.playStratSimplePlus(cardInGround,playedCard,numOfDeckPlay,Players,Bid,Trump, Napoleon, General)

	
	#this will be a much simpler strategy for the purposes of getting this started
	#basically the idea is that every player will be out for their own points
	#not very strategic as far as the general goes but lets see how it goes
	def playStratSimple(self,cardInGround,playedCard,numOfDeckPlay,Players,Bid,Trump, Napoleon, General):
		retcard=None
		self.analayzLastDeck(playedCard)
		pointsplayed=self.PointsPlayed(cardInGround)

		#if there are cards already played
		if len(cardInGround)!=0:
			if self.hastThisType(cardInGround[0][0].type)==True:
				if (pointsplayed > 0):
				#now try to play bigger One
					maxCardToPlay=0
					for card in self.cardsInHand:
						if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
							if (self.WhoWillWin(cardInGround,card, Trump) == self.locationInPlayedCard):
								maxCardToPlay=card.name
								retcard=card
					if retcard:
						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							return self.setAsPlay(retcard)
						else:
							retcard=None
					else:
						minCardToPlay=15
						for card in self.cardsInHand:
							if card.isPlayed==False and card.name<minCardToPlay and card.type==cardInGround[0][0].type :
									minCardToPlay=card.name
									retcard=card
						if retcard:
							if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
								return self.setAsPlay(retcard)
							else:
								retcard=None	
				else:
				#no points played.  not trying to win this

					minCardToPlay=15
					for card in self.cardsInHand:
						if (pointsplayed > 0):
							if card.isPlayed==False and self.WhoWillWin(cardInGround,card, Trump) == self.locationInPlayedCard and self.checkPlayCard(card, cardInGround, numOfDeckPlay):
								return self.setAsPlay(card)
						if (card.isPlayed==False and card.name<minCardToPlay):
								minCardToPlay=card.name
								retcard=card
					if retcard:
						if ( self.checkPlayCard(retcard, cardInGround, numOfDeckPlay)):
							return self.setAsPlay(retcard)
						else:
							retcard=None		
							

			else:
				#doesn't have the type played so is free to play anything
				#want to consider how to snipe with trump if there are points
				minCardToPlay=15
				for card in self.cardsInHand:
					if (pointsplayed > 0):
						if card.isPlayed==False and self.WhoWillWin(cardInGround,card, Trump) == self.locationInPlayedCard and self.checkPlayCard(card, cardInGround, numOfDeckPlay):
							return self.setAsPlay(card)
					if (card.isPlayed==False and card.name<minCardToPlay):
							minCardToPlay=card.name
							retcard=card
				if retcard:
					if ( self.checkPlayCard(retcard, cardInGround, numOfDeckPlay)):
						return self.setAsPlay(retcard)
					else:
						retcard=None	
		else:
			#here we will need to determine how far along the game is and then figure out what we can let go of
			#for now however it is being dumb and going to play a high card.  this will need to be changed. but i want to get it up and running
			maxCardToPlay=0
			for card in self.cardsInHand:
				if card.isPlayed==False and card.name>maxCardToPlay and self.checkPlayCard(card, cardInGround, numOfDeckPlay):
					maxCardToPlay=card.name
					retcard=card
					#need a who will win that considers all the cards that have already been played
					#and self.WhoWillWin(cardInGround,card, Trump) == self.locationInPlayedCard 
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

	
	#ok so this will be an extension of stratSimple, but we will take into account 
	#2s, so we will need to make sure it's not the first hand and everyone has followed suite, or that everyone so far has followed suite and it is an early hand
	#    this could get more complex in the future and check if anyone has gone out.. but really it should play the 2 as soon as a suite come out, or it should start with the 2 if 
	#    the hand is early and it has the lead
	#
	def playStratSimplePlus(self,cardInGround,playedCard,numOfDeckPlay,Players,Bid,Trump, Napoleon, General):
		retcard=None
		self.analayzLastDeck(playedCard)
		pointsplayed=self.PointsPlayed(cardInGround)

		#if there are cards already played
		if len(cardInGround)!=0:
			if self.hastThisType(cardInGround[0][0].type)==True:
				if numOfDeckPlay>0:
					for card in self.cardsInHand:
						if card.isPlayed==False and card.name==1 and card.type==cardInGround[0][0].type and self.checkPlayCard(card, cardInGround, numOfDeckPlay):
							return self.setAsPlay(card)
				if (pointsplayed > 0):
				#now try to play bigger One
					maxCardToPlay=0
					for card in self.cardsInHand:
						if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
							if (self.WhoWillWin(cardInGround,card, Trump) == self.locationInPlayedCard):
								maxCardToPlay=card.name
								retcard=card
					if retcard:
						if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
							return self.setAsPlay(retcard)
						else:
							retcard=None
					else:
						minCardToPlay=15
						for card in self.cardsInHand:
							if card.isPlayed==False and card.name<minCardToPlay and card.type==cardInGround[0][0].type :
									minCardToPlay=card.name
									retcard=card
						if retcard:
							if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
								return self.setAsPlay(retcard)
							else:
								retcard=None	
				else:
				#no points played.  not trying to win this

					minCardToPlay=15
					for card in self.cardsInHand:
						if (pointsplayed > 0):
							if card.isPlayed==False and self.WhoWillWin(cardInGround,card, Trump) == self.locationInPlayedCard and self.checkPlayCard(card, cardInGround, numOfDeckPlay):
								return self.setAsPlay(card)
						if (card.isPlayed==False and card.name<minCardToPlay and  card.name!=1):
								minCardToPlay=card.name
								retcard=card
					if retcard:
						if ( self.checkPlayCard(retcard, cardInGround, numOfDeckPlay)):
							return self.setAsPlay(retcard)
						else:
							retcard=None		
							

			else:
				#doesn't have the type played so is free to play anything
				#want to consider how to snipe with trump if there are points
				minCardToPlay=15
				for card in self.cardsInHand:
					if (pointsplayed > 0):
						if card.isPlayed==False and self.WhoWillWin(cardInGround,card, Trump) == self.locationInPlayedCard and self.checkPlayCard(card, cardInGround, numOfDeckPlay):
							return self.setAsPlay(card)
					if (card.isPlayed==False and card.name<minCardToPlay and card.name!=1):
							minCardToPlay=card.name
							retcard=card
				if retcard:
					if ( self.checkPlayCard(retcard, cardInGround, numOfDeckPlay)):
						return self.setAsPlay(retcard)
					else:
						retcard=None	
		else:
			#here we will need to determine how far along the game is and then figure out what we can let go of
			#for now however it is being dumb and going to play a high card.  this will need to be changed. but i want to get it up and running
			if numOfDeckPlay>0:
				for card in self.cardsInHand:
					if card.isPlayed==False and card.name==1 and self.checkPlayCard(card, cardInGround, numOfDeckPlay):
						return self.setAsPlay(card)
			else:
				for card in self.cardsInHand:
					#on the first hand try to play an ace that is not the ace of trump and not the ace of spades
					if card.isPlayed==False and card.name==13 and card.type!=Trump and card.type!=1 and self.checkPlayCard(card, cardInGround, numOfDeckPlay):
						return self.setAsPlay(card)
			maxCardToPlay=0
			for card in self.cardsInHand:
				if card.isPlayed==False and card.name>maxCardToPlay and self.checkPlayCard(card, cardInGround, numOfDeckPlay):
					maxCardToPlay=card.name
					retcard=card
					#need a who will win that considers all the cards that have already been played
					#and self.WhoWillWin(cardInGround,card, Trump) == self.locationInPlayedCard 
			if retcard:
				if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
					return self.setAsPlay(retcard)
				else:
					retcard=None
			

		if retcard==None:
		#Ok stupid ! play every thinh you want ! I dont know how much must learn you Napoleon Game :P
			for i in range(0,13):
				if self.cardsInHand[i].isPlayed==False:
					if self.checkPlayCard(self.cardsInHand[i], cardInGround, numOfDeckPlay):
						retcard=self.cardsInHand[i]
		return retcard




	def playStratN1(self,cardInGround,playedCard,numOfDeckPlay,Players,Bid,Trump, Napoleon, General):
		retcard=None
		self.analayzLastDeck(playedCard)
		pointsplayed=self.PointsPlayed(cardInGround)
		
		if self.isNapoleon==True:
			#player is his own general
			#this code won't be used until there is a pot because the computer user will currently never pick one of their cards as general
			if self.isGeneral==True:
				#if there are cards already played
				if len(cardInGround)!=0:
					if self.hastThisType(cardInGround[0][0].type)==True:
						if (pointsplayed > 0):
						#now try to play bigger One
							maxCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name>maxCardToPlay and card.type==cardInGround[0][0].type :
									if (self.WhoWillWin(cardInGround,card, Trump) == self.locationInPlayedCard):
										maxCardToPlay=card.name
										retcard=card
							if retcard:
								if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
									return self.setAsPlay(retcard)
								else:
									retcard=None
							else:
								minCardToPlay=0
								for card in self.cardsInHand:
									if card.isPlayed==False and card.name<maxCardToPlay and card.type==cardInGround[0][0].type :
											minCardToPlay=card.name
											retcard=card
								if retcard:
									if self.checkPlayCard(retcard, cardInGround, numOfDeckPlay):
										return self.setAsPlay(retcard)
									else:
										retcard=None	
						else:
						#no points played.  not trying to win this
							minCardToPlay=0
							for card in self.cardsInHand:
								if card.isPlayed==False and card.name<maxCardToPlay and card.type==cardInGround[0][0].type :
										minCardToPlay=card.name
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


	def setAsPlay(self,card):
		card.isPlayed=True
		return card

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
