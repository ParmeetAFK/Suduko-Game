
# ---------------------------------------------- 2x2 Board ---------------------------------------
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

# --------------------------------------------- f() for printing board on cmd --------------------------

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


# -------------------------------------f() for finding empty spaces in board ---------------------------------------
def empty(board):
	for row in range(len(board)):
		for col in range(len(board[row])):
			if board[row][col] == 0:
				return(row,col)

	return None

# --------------------------------------- f() for Validating the move --------------------------------------------------

def valid_move(board,num,row,col):

	# ROW VALIDATION
	for i in range(9):
		if board[row][i] == num and col != i:
			return False

	#COL VALIDATION
	for i in range(9):
		if board[i][col] == num and row != i:
			return False

	#CUBE VALIDATION
	box_x = col // 3
	box_y = row // 3
	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x * 3, box_x*3 + 3):
			if board[i][j] == num and (i,j) != (row,col):
				return False

	return True

# --------------------- Main function to solve full board using recursion ---------------------------------------------
def doit(board):
    find = empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid_move(board, i, row, col):
            board[row][col] = i

            if doit(board):
                return True

            board[row][col] = 0

    return False



print_board(board)
doit(board)
print("<------------------------------------------>")
print_board(board)