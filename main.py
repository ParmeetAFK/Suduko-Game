
board = [

		[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]

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
				return(row,col)

	return None

def valid_move(board,num,row,col):

	# ROW VALIDATION
	for i in range(9):
		if board[row][i] == num:
			return False

	#COL VALIDATION
	for i in range(9):
		if board[i][col] == num:
			return False

	#CUBE VALIDATION
	row = row % 3 - row
	col = col % 3 - col
	
	for i in range(3):
		for j in range(3):
			if (board[row+i][col+j] == num):
				return False

	return True


def doit(board):
	gate = empty(board)
	if not gate:
		return True
	else:
		row,col = gate

	for i in range(1,10):
		valid = valid_move(board,i,row,col)
		if valid == True:
			board[row][col] = i

			if doit(board):
				return True

			board[row][col] = 0

	return False

print_board(board)
doit(board)
print("<------------------------------------------>")
print_board(board)