from tkinter import *
import tkinter as tk

board = [

		[7,1,2,3,4,5,6,8,9],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,5,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,3,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0]

]

root = Tk()
root.title('Sudoku')
#root.geometry('500x500')

# create all of the main containers
center = Frame(root, bg='white', width=500, height=500, padx=3, pady=3)

cells = {}
for row in range(9):
    for column in range(9):
        cell = Frame(root, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=1,
                     width=50, height=50,  padx=3,  pady=3)
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell

for i in range(len(board)):
	for j in range(len(board)):
		for k in cells:
			k = Label(root,text=board[i][j])
			


root.mainloop()