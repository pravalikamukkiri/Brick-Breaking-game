from headers import *

class Paddle:
	def __init__(self,x,y,l):
		self._x=x
		self._y=y
		self._l=l
		self._s=2
	def changepos(self,d,brd,ball):
		if(brd._userwill==0 or (brd._poweruptype==6 and brd._powerupcatched==1)):
			ball._xi=ball._x
			ball._yi=ball._y
			ball._y+=d
			ball.change_ball_pos(brd)
		self._y=self._y+d

	def expandpaddle(self,brd):
		for i in range(self._l):
			brd._board[self._x][self._y+i]='-'
		if(self._y>6):
			self._y=self._y-6
		self._l+=6
		for i in range(self._l):
			brd._board[self._x][self._y+i]='p'



	def shrinkpaddle(self,brd):
		brd._board[self._x][self._y]=brd._board[self._x][self._y+1]=brd._board[self._x][self._y+self._l-1]=brd._board[self._x][self._y+self._l-2]='-'
		self._l-=4
		self._y+=2

	def paddlenormal(self,brd):
		for i in range(self._l):
			brd._board[self._x][self._y+i]='-'
		if(self._l>20):
			self._l=20
			for i in range(self._l):
				brd._board[self._x][self._y+i]='p'
		else:
			if(self._y>4):
				self._y=self._y-4
			self._l+=4
			for i in range(self._l):
				brd._board[self._x][self._y+i]='p'

			





