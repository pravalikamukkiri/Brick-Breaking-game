from headers import *
from functions import *

class Board:
	def __init__(self,hight,width):
		self._hight=hight
		self._width=width
		self._score=0
		self._time=0
		self._lifes=15
		self._powerup=0
		self._powerupx=0
		self._powerupy=0
		self._powerupcatched=0
		self._powerupstime=0
		self._poweruptype=0
		self._userwill=0
		self._type=0
		self._start_time = time.time()
		self._board=[["-" for a in range(width)] for b in range(hight)]
		self._bonusbricks=[]
		title="Welcome to Brick Breaker Game"
		t=(width-len(title))//2
		for i in range(len(title)):
			self._board[1][t]=title[i]
			t=t+1
	def setpaddle(self,pad):
		for i in range(0,pad._l):
			self._board[pad._x][pad._y+i]='p'


	def setball(self,user_b):
		self._board[user_b._x][user_b._y]='o'

	def setbricks(self):
		midx=(self._hight-5)//2
		midy=(self._width-5)//2
		#bonus bricks
		for i in range(-2,3):
			bonusbrick(self,midx+i*3,6)
		for i in range(-1,2):
			bonusbrick(self,midx+i*3,2)
		self.setbrick(midx,midy)
		self.setbrick(midx-3,midy)
		for i in range(-2,2):
			if(midx+i*3 >3 and midx+i*3<self._hight-3):
				self.setbrick(midx+i*3,midy+10)
				self.setbrick(midx+i*3,midy-10)
		for i in range(-3,3):
			if(midx+i*3 >3 and midx+i*3<self._hight-3):
				self.setbrick(midx+i*3,midy+20)
				self.setbrick(midx+i*3,midy-20)
		
		f=3
		a=1
		b=-2
		while(f>0):
			if(midx+(a+2)*3<=self._hight-10 and midy+7*f <self._width and midy-7*f>5  and midx-i*3>10):
				for i in range(a,a+3):
					self.setbrick(midx+i*3 ,midy+10*f)
					self.setbrick(midx+i*3 ,midy-10*f)
					self.setbrick(midx-i*3 ,midy+10*f)
					self.setbrick(midx-i*3 ,midy-10*f)
				a=a+1
				f=f+1
			else:
				f=0
				break

	def setbrick(self,x,y):
		brick=Brick(x,y)
		brick.placebrick(self)

	def print_board(self):

		for i in range(len(self._board)):
			if(i==0 or i==2):
				for j in self._board[i]:
					print(Back.MAGENTA+" ",end="")
				print(Style.RESET_ALL,end="")
			elif(i==1):
				for j in self._board[i]:
					if(j=='-'):
						print(Back.MAGENTA+" ",end="")
					else:
						print(Back.MAGENTA+j,end="")

			elif(i==3):
				for j in range(self._width):
					self._board[i][j]='-'
				temps="score: "+str(self._score)
				temps+="     Lifes:   "+str(self._lifes)
				x=round(self._start_time)-round(time.time())
				temps+="    Time :"+str(x)
				temps+="    power  :  "+str(self._powerup)+str(self._powerupcatched)+str(self._poweruptype)

				if(self._powerupcatched):
					temps+='powerup time   '+str(round(time.time())-round(self._powerupstime))
				temps+="     3:RED 2:YEL 1:BLUE  B:MAG   "
				for j in range(len(temps)):
					self._board[i][j]=temps[j]
				for j in self._board[i]:
					if(j=='-'):
						print(Back.YELLOW+" ",end="")
						print(Style.RESET_ALL,end="")
					else:
						print(Back.YELLOW+j,end="")
						print(Style.RESET_ALL,end="")
			else:
				for j in range(len(self._board[i])):
					t=self._board[i][j]
					if(j==0 or j==self._width-1 or i==self._hight-1):
						print(Back.	YELLOW+' ',end="")
						print(Style.RESET_ALL,end="")
					elif(t=='3'):
						print(Back.RED+' ',end="")
						print(Style.RESET_ALL,end="")
					elif(t=='2'):
						print(Back.YELLOW+' ',end="")
						print(Style.RESET_ALL,end="")
					elif(t=='1'):
						print(Back.CYAN+' ',end="")
						print(Style.RESET_ALL,end="")
					elif(t=='4'):
						print(Back.GREEN+' ',end="")
						print(Style.RESET_ALL,end="")
					elif(t=='5'):
						print(Back.MAGENTA+' ',end="")
						print(Style.RESET_ALL,end="")
					elif(t=='x'):
						list=['x','E','S','M','F','T','g']
						print(list[self._type],end="")
					elif(t=='p'):
						print(Back.GREEN+'p',end="")
						print(Style.RESET_ALL,end="")
					elif(t=='o'):
						print(t,end="")
					else:
						print(' ',end="")

	def changepadlpos(self,pad,d,ball):
		s=pad._s #speed
		if(s==1):
			if(d==-1  and pad._y>1):
				self._board[pad._x][pad._y-1]='p'
				self._board[pad._x][pad._y+pad._l-1]='-'
				pad.changepos(-1,self,ball)
				
			elif(d==1 and pad._y+pad._l<width-2):
				self._board[pad._x][pad._y+pad._l]='p'
				self._board[pad._x][pad._y]='-'
				pad.changepos(1,self,ball)
		elif(s==2):
			if(d==-1  and pad._y>2):
				for i in range(1,3):
					self._board[pad._x][pad._y-i]='p'
					self._board[pad._x][pad._y+pad._l-i]='-'
				pad.changepos(-2,self,ball)
			
			elif(d==1 and pad._y+pad._l<width-3):
				for i in range(2):
					self._board[pad._x][pad._y-i]='-'
					self._board[pad._x][pad._y+pad._l+i]='p'
				pad.changepos(2,self,ball)
		elif(s==3):
			if(d==-1  and pad._y>3):
				for i in range(1,4):
					self._board[pad._x][pad._y-i]='p'
					self._board[pad._x][pad._y+pad._l-i]='-'
				pad.changepos(-2,self,ball)
			
			elif(d==1 and pad._y+pad._l<width-4):
				for i in range(3):
					self._board[pad._x][pad._y-i]='-'
					self._board[pad._x][pad._y+pad._l+i]='p'
				pad.changepos(2,self,ball)
	def setpowerupbrick(self,x,y,pad,bal):
		tx=x
		ty=y
		
		while (self._board[tx][ty]=='1' or self._board[tx][ty]=='2' or self._board[tx][ty]=='3' or self._board[tx][ty]=='4'):
			self._board[tx][ty]='x'	
			self._powerupy=ty		
			ty=ty-1
		tx=x
		ty=y+1
		while (self._board[tx][ty]=='1' or self._board[tx][ty]=='2' or self._board[tx][ty]=='3' or self._board[tx][ty]=='4'):
			self._board[tx][ty]='x'
			ty=ty+1


	def brickcollisionfunction(self,x,y,pad,bal):
		tx=x
		ty=y
		while (self._board[tx][ty]=='1' or self._board[tx][ty]=='2' or self._board[tx][ty]=='3' or self._board[tx][ty]=='4'):
			if(self._powerupcatched==1 and self._poweruptype==5):
				self._board[tx][ty]='-'			
			elif(self._board[tx][ty]=='1'):
				self._board[tx][ty]='-'
			elif(self._board[tx][ty]=='2'):
				self._board[tx][ty]='1'
			elif(self._board[tx][ty]=='3'):
				self._board[tx][ty]='2'
			ty=ty-1
		tx=x
		ty=y+1
		while (self._board[tx][ty]=='1' or self._board[tx][ty]=='2' or self._board[tx][ty]=='3' or self._board[tx][ty]=='4'):
			if(self._powerupcatched==1 and self._poweruptype==5):
				self._board[tx][ty]='-'
			elif(self._board[tx][ty]=='1'):
				self._board[tx][ty]='-'
			elif(self._board[tx][ty]=='2'):
				self._board[tx][ty]='1'
			elif(self._board[tx][ty]=='3'):
				self._board[tx][ty]='2'
			ty=ty+1

		
	def brickcollision(self,x,y,pad,bal):
		self._score+=5
		temp=0
		for i in self._board:
			for j in i:
				if(j=='x'):
					temp=1
					break
		flag=0
		if(self._powerupcatched==0 and self._poweruptype==0 and self._powerup==0 and temp==0 and random.randint(0,1)==0):
			f=0
			for i in range(x+2,self._hight-3):
				if(self._board[i][y]=='1' or self._board[i][y]=='2' or self._board[i][y]=='3' or self._board[i][y]=='4' or self._board[i][y]=='x'):
					f=1
					break
			if(f==0):
				self._powerup=1
				flag=1
				self._type=random.randint(1,6)

		if(flag==0):
			self.brickcollisionfunction(x,y,pad,bal)
			self.brickcollisionfunction(x+1,y,pad,bal)
			self.brickcollisionfunction(x-1,y,pad,bal)
		else:
			if(self._board[x+1][y]=='1' or self._board[x+1][y]=='2' or self._board[x+1][y]=='3'):
				self._powerupx=x
			else:
				self._powerupx=x-1
			self.setpowerupbrick(x,y,pad,bal)
			self.setpowerupbrick(x+1,y,pad,bal)
			self.setpowerupbrick(x-1,y,pad,bal)

		
	def bonusbrickcollision(self):
		for i in range(4,self._hight):
			for j in range(self._width):
				if(self._board[i][j]=='5'):
					self._board[i][j]='-'


	def powerupbrick(self,pad,ball):
		if(self._powerupcatched==0 and self._poweruptype==0 and self._powerup==0):
			for a in range(hight):
				for b in range(width):
					if(self._board[a][b]=='x'):
						self._board[a][b]='-'
		if(self._powerupcatched and (round(time.time())-round(self._powerupstime))>=10):
			self._powerupcatched=0
			self._powerup=0
			if(self._poweruptype==3):
				self._board[ball._x][ball._y]='-'
			elif(self._poweruptype==1 or self._poweruptype==2):
				pad.paddlenormal(self)
			elif(self._poweruptype==4):
				ball._speed=1
			self._poweruptype=0
			self._userwill=1
			self._type=0
			

		if(self._powerup):
			if(self._powerupx<self._hight-4):
				if(ball._x==self._powerupx+2 and ball._y>=self._powerupy and ball._y<self._powerupy+9):
					self._powerupx=self._powerupx
				else:
					for i in range(self._powerupy,self._powerupy+9):
							self._board[self._powerupx][i]='-'
							self._board[self._powerupx+2][i]='x'
					self._powerupx=self._powerupx+1

			elif(self._powerupx==self._hight-4 and (self._board[self._powerupx+2][self._powerupy]=='p' or self._board[self._powerupx+2][self._powerupy+8]=='p' )):
				self._powerupcatched=1
				self._powerupstime=time.time()
				self._poweruptype=self._type
				self._powerup=0
				
				for i in  range(self._powerupy,self._powerupy+9):
					self._board[self._powerupx][i]='-'
					self._board[self._powerupx+1][i]='-'
				self._powerupx=self._powerupy=0
				self.powerupfun(pad,ball)

			elif(self._powerupx>=self._hight-4):
				self._powerup=0
				for i in  range(self._powerupy,self._powerupy+9):
					self._board[self._powerupx][i]='-'
					self._board[self._powerupx+1][i]='-'
				self._powerupx=self._powerupy=0


	def powerupfun(self,pad,ball):
		if(self._powerupcatched==1 and self._poweruptype==1):
			pad.expandpaddle(self)
		elif(self._powerupcatched==1 and self._poweruptype==2):
			pad.shrinkpaddle(self)
		elif(self._powerupcatched==1 and self._poweruptype==4):
			ball._speed=2

	def checkgame(self):
		c=0
		for i in range(4,self._hight):
			for t in range(self._width):
				j=self._board[i][t]
				if(j=='1' or j=='2' or j=='3' or j=='5' or j=='x'):
					c+=1
		return c
