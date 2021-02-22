from headers import *
from functions import *

from board import Board
from paddle import Paddle
from ball import Ball
from bricks import *

paddle=Paddle(hight-2,width//2,20)
obj_board=Board(hight,width)
obj_board.setpaddle(paddle)


ball=Ball(paddle._x-1,paddle._y+paddle._l//2)
ball2=Ball(-1,-1)
obj_board.setball(ball)

obj_board.setbricks()



def movepaddle():	
	print("enter a to left and d to right")	
	# print(paddle._l,'  ',paddle._y)
	# print(ball._xi,ball._yi,ball._x,ball._y,ball._xa,ball._ya,ball2._x,ball2._y,ball._dir)
	char=input_to()
	if char=='a' or char=='A':
		obj_board.changepadlpos(paddle,-1,ball)

	elif char=='d' or char=='D':
		obj_board.changepadlpos(paddle,1,ball)
	elif char=='b' or char=='B':
		obj_board._userwill=1
		# if(obj_board._poweruptype==6):
		# 	ball.setpos(ball._x,ball._y,ball._x,ball._y,ball._x-1,ball._ya)
		# 	ball.change_ball_pos(obj_board)

	elif char=='q' or char=='Q':
		endgame()
		quit()

def endgame():
	print("Game over")
	print("Thank you for playing this game")
	print("Your score: ",obj_board._score)









