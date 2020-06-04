import pygame

board = [

		[7,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,5,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,3,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0]

]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def empty(board):
	for row in range(len(board)):
		for col in range(len(board[row])):
			if board[row][col] == 0:
				print(row,col)





empty(board)