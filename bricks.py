from headers import *
class Brick:
	def __init__(self,x,y):
		self._x=x
		self._y=y
	def placebrick(self,brd):
		p=random.randint(1,4)
		if(p==3):
			pow3Brick(brd,self._x,self._y)
		elif(p==2):
			pow2Brick(brd,self._x,self._y)
		elif(p==1):
			pow1Brick(brd,self._x,self._y)
		elif(p==4):
			pow4Brick(brd,self._x,self._y)

class bonusbrick(Brick):
	def __init__(self,brd,x,y):
		Brick.__init__(self,x,y)
		self._p=5

		for i in range(3):
			brd._board[x][y+i]=str(self._p)
			brd._board[x+1][y+i]=str(self._p)


class pow3Brick(Brick):
	def __init__(self,brd,x,y):
		Brick.__init__(self,x,y)
		self._p=3

		for i in range(9):
			brd._board[x][y+i]=str(3)
			brd._board[x+1][y+i]=str(3)
class pow2Brick(Brick):
	def __init__(self,brd,x,y):
		Brick.__init__(self,x,y)
		self._p=2

		for i in range(9):
			brd._board[x][y+i]=str(2)
			brd._board[x+1][y+i]=str(2)
class pow1Brick(Brick):
	def __init__(self,brd,x,y):
		Brick.__init__(self,x,y)
		self._p=1

		for i in range(9):
			brd._board[x][y+i]=str(1)
			brd._board[x+1][y+i]=str(1)

class pow4Brick(Brick):
	def __init__(self,brd,x,y):
		Brick.__init__(self,x,y)
		self._p=4

		for i in range(9):
			brd._board[x][y+i]=str(4)
			brd._board[x+1][y+i]=str(4)
