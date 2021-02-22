from headers import *
from functions import * 

class Ball:
	def __init__(self,x,y):
		self._x=x
		self._y=y
		self._xi=x
		self._yi=y
		self._xa=x
		self._ya=y
		self._rs=0
		self._speed=1
		self._dir=-1

	def placeball(self,x,y,brd):
		self._x=self._xa=x
		self._y=self._ya=y
		self.change_ball_pos(brd)

	def initialpos(self,x,y,brd):
		self._rs=0
		self._xi=self._x
		self._yi=self._y
		self._x=x
		self._y=y
		self._xa=x
		self._ya=y
		self.change_ball_pos(brd)

	def setpos(self,xi,yi,x,y,xa,ya):
		self._xi=xi
		self._yi=yi
		self._x=x
		self._y=y
		self._xa=xa
		self._ya=ya

	def change_ball_pos(self,brd):
		brd._board[self._xi][self._yi]='-'
		brd._board[self._x][self._y]='o'

	def check_collision(self,paddle,brd):
		if(self._x>=paddle._x):
			brd._lifes=brd._lifes-1
			#poweuploss
			brd._powerupcatched=0
			brd._powerup=0
			if(brd._poweruptype==3):
				brd._board[self._x][self._y]='-'
			elif(brd._poweruptype==1 or brd._poweruptype==2):
				paddle.paddlenormal(brd)
			elif(brd._poweruptype==4):
				self._speed=1
			brd._poweruptype=0
			brd._userwill=1
			brd._type=0

			self.initialpos(paddle._x-1,paddle._y+paddle._l//2,brd)
		elif(self._x== paddle._x-1 and paddle._y <= self._y < paddle._y+paddle._l and self._rs==0):#up/
			self._rs=1
			self.setpos(self._x,self._y,self._x-1,self._y+1,self._x-2,self._y+2)
			self.change_ball_pos(brd)
		elif(brd._board[self._xa][self._ya]=='p' or brd._board[self._x][self._y]=='p'):#padd/
			if(brd._poweruptype==6):
				brd._userwill==0
			else:
				self.setpos(self._x,self._y,self._x,self._y,self._x-1,self._ya)
				self.change_ball_pos(brd)

		elif(brd._board[self._xa][self._ya]=='5'):
			brd.bonusbrickcollision()
			self.change_ball_pos(brd)
		elif(brd._board[self._x][self._y-1]=='4' and brd._board[self._x][self._y+1]=='4'):
			self.initialpos(paddle._x-1,paddle._y+paddle._l//2,brd)
		elif((brd._board[self._xa][self._ya]=='1' or brd._board[self._xa][self._ya]=='2' or brd._board[self._xa][self._ya]=='3') and self._xa==self._x-1):
			brd.brickcollision(self._xa,self._ya,paddle,self)
			if(brd._poweruptype!=5):
				self._xa=self._x+1
			self.change_ball_pos(brd)
		elif((brd._board[self._xa][self._ya]=='1'  or brd._board[self._xa][self._ya]=='2' or brd._board[self._xa][self._ya]=='3')and self._xa==self._x+1):
			brd.brickcollision(self._xa,self._ya,paddle,self)
			if(brd._poweruptype!=5):
				self._xa=self._x-1
			self.change_ball_pos(brd)
		elif((brd._board[self._x][self._y+1]=='1' or brd._board[self._x][self._y+1]=='2' or brd._board[self._x][self._y+1]=='3') and  self._ya==self._y+1):
			brd.brickcollision(self._x,self._y+1,paddle,self)
			if(brd._poweruptype!=5):
				self._ya=self._y-1
			self.change_ball_pos(brd)
		elif((brd._board[self._x][self._y-1]=='1' or brd._board[self._x][self._y-1]=='2' or brd._board[self._x][self._y-1]=='3') and self._ya==self._y-1):
			brd.brickcollision(self._x,self._y-1,paddle,self)
			if(brd._poweruptype!=5):
				self._ya=self._y+1
			self.change_ball_pos(brd)

		elif(brd._board[self._xa][self._ya]=='4' and self._xa==self._x-1):
			if(brd._poweruptype==5):
				brd.brickcollision(self._xa,self._ya,paddle,self)
			elif(brd._board[self._x+1][self._ya]=='4'):
				self._xa=self._xi
				self._ya=self._yi
			else:
				self._xa=self._x+1
			self.change_ball_pos(brd)
		elif(brd._board[self._xa][self._ya]=='4' and self._xa==self._x+1):
			if(brd._poweruptype==5):
				brd.brickcollision(self._xa,self._ya,paddle,self)
			if(brd._board[self._x-1][self._ya]=='4'):
				self._xa=self._xi
				self._ya=self._yi
			else:
				self._xa=self._x-1
			self.change_ball_pos(brd)
		elif(brd._board[self._x][self._y+1]=='4' and  self._ya==self._y+1 ):
			if(brd._poweruptype==5):
				brd.brickcollision(self._xa,self._ya,paddle,self)
			if(brd._board[self._x][self._y-1]=='4'):
				self._ya=self._yi
				self._xa=self._xi
			else:
				self._ya=self._y-1
			self.change_ball_pos(brd)
		elif(brd._board[self._x][self._y-1]=='4' and self._ya==self._y-1):
			if(brd._poweruptype==5):
				brd.brickcollision(self._xa,self._ya,paddle,self)
			if(brd._board[self._x][self._y+1]=='4'):
				self._ya=self._yi
				self._xa=self._xi
			else:
				self._ya=self._y+1
			self.change_ball_pos(brd)

		elif(self._xa==3 ):#topu//
			self.setpos(self._x,self._y,self._x,self._y,self._x+1,self._ya)
			self.change_ball_pos(brd)
		elif(self._ya==0):#left//
			self.setpos(self._x,self._y,self._x,self._y,self._xa,self._y+1)
			self.change_ball_pos(brd)
		elif(self._ya==brd._width-1):#right\\
			self.setpos(self._x,self._y,self._x,self._y,self._xa,self._y-1)
			self.change_ball_pos(brd)

		elif(self._x-1==self._xa and self._y+1==self._ya and brd._board[self._xa][self._ya]=='-'):
			self.setpos(self._x,self._y,self._x-1,self._y+1,self._x-2,self._y+2)
			self.change_ball_pos(brd)
		elif(self._x+1==self._xa and self._y+1==self._ya and brd._board[self._xa][self._ya]=='-'):
			self.setpos(self._x,self._y,self._x+1,self._y+1,self._x+2,self._y+2)
			self.change_ball_pos(brd)
		elif(self._x-1==self._xa and self._y-1==self._ya and brd._board[self._xa][self._ya]=='-'):
			self.setpos(self._x,self._y,self._x-1,self._y-1,self._x-2,self._y-2)
			self.change_ball_pos(brd)
		elif(self._x+1==self._xa and self._y-1==self._ya and brd._board[self._xa][self._ya]=='-'):
			self.setpos(self._x,self._y,self._x+1,self._y-1,self._x+2,self._y-2)
			self.change_ball_pos(brd)
		else:
			self.initialpos(paddle._x-1,paddle._y+paddle._l//2,brd)

	

	def speedball(self,paddle,brd):
		#1/ \2
		#4\ /3 clockwise
		# 1--up,2- up, 3-left , 4-right
		if(self._rs==0):
			self._rs=1
			self.setpos(self._x,self._y,self._x-2,self._y+2,self._x-4,self._y+4)
			self._dir=1
			self.change_ball_pos(brd)
		elif(self._xa>=paddle._x):
			#poweuploss
			brd._powerupcatched=0
			brd._powerup=0
			self._speed=1
			brd._poweruptype=0
			brd._userwill=1
			brd._type=0
			brd._lifes=brd._lifes-1
			self.initialpos(paddle._x-1,paddle._y+paddle._l//2,brd)
		elif(brd._board[self._xa][self._ya]=='p' or brd._board[self._xa-1][self._ya]=='p' or brd._board[self._xa+1][self._ya]=='p'):
			if(self._dir==3):
				self._dir=4
			else:
				self._dir=3
			self.setpos(self._x,self._y,self._x,self._y,self._xi,self._ya)
			self.change_ball_pos(brd)
		elif(self._xa<=4):
			self.setpos(self._x,self._y,self._x,self._y,self._x+2,self._ya)
			self.change_ball_pos(brd)
			if(self._dir==1):
				self._dir=2
			if(self._dir==4):
				self._dir=3
			
		elif(self._ya<=1):
			self.setpos(self._x,self._y,self._x,self._y,self._xa,self._yi)
			if(self._dir==3):
				self._dir==2
			if(self._dir==4):
				self._dir=1
			self.change_ball_pos(brd)
		elif(self._ya>=brd._width-3):
			self.setpos(self._x,self._y,self._x,self._y,self._xa,self._yi)
			if(self._dir==2):
				self._dir=3
			if(self._dir==1):
				self._dir=4
			self.change_ball_pos(brd)

		elif(brd._board[self._xa][self._ya]=='1' or brd._board[self._xa][self._ya]=='2' or brd._board[self._xa][self._ya]=='3' or brd._board[self._xa][self._ya]=='4' ):
			if(brd._board[self._xa][self._ya]=='1' or brd._board[self._xa][self._ya]=='2' or brd._board[self._xa][self._ya]=='3'):
				brd.brickcollision(self._xa,self._ya,paddle,self)

			if(self._dir==1):
				self.setpos(self._x,self._y,self._x,self._y,self._x+2,self._y+2)
				self.change_ball_pos(brd)
				self._dir=2
			elif(self._dir==2):
				self.setpos(self._x,self._y,self._x,self._y,self._x-2,self._y+2)
				self.change_ball_pos(brd)
				self._dir=1
			elif(self._dir==3):
				self.setpos(self._x,self._y,self._x,self._y,self._x-2,self._y-2)
				self.change_ball_pos(brd)
				self._dir=4
			elif(self._dir==4):
				self.setpos(self._x,self._y,self._x,self._y,self._x+2,self._y-2)
				self.change_ball_pos(brd)
				self._dir=3

		elif(self._dir==1):
			self.setpos(self._x,self._y,self._x-2,self._y+2,self._x-4,self._y+4)
			self.change_ball_pos(brd)
		elif(self._dir==2):
			self.setpos(self._x,self._y,self._x+2,self._y+2,self._x+4,self._y+4)
			self.change_ball_pos(brd)
		elif(self._dir==3):
			self.setpos(self._x,self._y,self._x+2,self._y-2,self._x+4,self._y-4)
			self.change_ball_pos(brd)
		elif(self._dir==4):
			self.setpos(self._x,self._y,self._x-2,self._y-2,self._x-4,self._y-4)
			self.change_ball_pos(brd)
		else:
			self.initialpos(paddle._x-1,paddle._y+paddle._l//2,brd)








		
	





