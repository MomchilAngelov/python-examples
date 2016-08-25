from turtle import *

def draw_square(chess):
	chess.begin_fill()
	for i in range(4):
		chess.left(90)
		chess.fd(50)
	chess.end_fill()

def draw_row(chess, row):
	for y in range(8):
		if (x + y) % 2 == 0:
			chess.fillcolor("black")
		else:
			chess.fillcolor("white")

		chess.pu()
		chess.setpos(y * 50 + start_x, x * 50 + start_y)
		chess.pd()
		draw_square(chess)


chess = Turtle()
chess.speed(0)
start_x = -200
start_y = -200
chess.pu()
chess.setpos(start_x, start_y)
chess.pd()

for x in range(8):
	draw_row(chess = chess,row = x)
exitonclick()