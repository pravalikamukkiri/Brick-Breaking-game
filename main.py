from headers import *
from functions import *



while True:
	if(obj_board._lifes<=0 or obj_board.checkgame()==0 ):
		endgame()
		quit()
	os.system('clear')
	# print(obj_board.checkgame())
	# spped
	if(ball._speed==2):
		ball.speedball(paddle,obj_board)
	else:
		if(obj_board._userwill):
			ball.check_collision(paddle,obj_board)

	obj_board.powerupbrick(paddle,ball)

	if(obj_board._poweruptype==3):
		if(ball2._x==-1 and ball2._y==-1):
			obj_board._lifes+=2
			ball2.initialpos(paddle._x+1,paddle._y+5,obj_board)
		if(obj_board._userwill):
			ball2.check_collision(paddle,obj_board)
		obj_board.powerupbrick(paddle,ball2)

	if(obj_board._powerupcatched==0):
		obj_board._board[ball2._x][ball2._y]='-'
		ball2.setpos(-1,-1,-1,-1,-1,-1)

	obj_board.print_board()
	movepaddle()