import pygame

board = [

		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0]

]

pygame.init()
pygame.font.init()
win = pygame.display.set_mode((550,550))
font = pygame.font.SysFont('Fugaz One', 120)
pygame.display.set_caption("Suduko")




run = True

while run:

	make_board(board)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()