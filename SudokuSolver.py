import numpy as np

sudokuBoard = np.random.randint(1, high = 10, size = (9, 9)) 


grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]
   
def solve(bo):
	find = find_empty(bo)
	if not find:
		return True
	else:
		row, col, = find
	
	for i in range(1,10):
		if valid(bo, i, (row, col)):
			bo[row][col] = i
			
			# recursively solve board
			if solve(bo):
				return True
				
			bo[row][col] = 0
	
	return False
	  
         
def valid(bo, number, position):
	#check row
	for i in range(len(bo[0])):
		if bo[position[0]][i] == number and position[1] != i:
			return False
	
	#check col
	for i in range(len(bo)):
		if bo[i][position[1]] == number and position[0] != i:
			return False
		
	#check the 3x3 box
	box_x = position[1] // 3
	box_y = position[0] // 3
	
	for i in range(box_y * 3, box_y*3 + 3):
		for j in range(box_x * 3, box_x*3 + 3):
			if bo[i][j] == number and (i,j) != position:
				return False
	
	return True
	
def print_board(bo):
	
		# print horizontal line every 3rd row
		for i in range(len(bo)):
			if i % 3 == 0 and i != 0:
				print("- - - - - - - - - - - - - ")
			
			# print vertical lines
			for j in range(len(bo[0])):
				if j % 3 == 0 and j != 0:
					print(" | ", end = "")
				
				# check if in last position
				if j == 8:
					print(bo[i][j])
				else:
					print(str(bo[i][j]) + " ", end = "")
					
					
def find_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return(i, j)
	return None
				
		 
print_board(grid)
solve(grid)
print("")
print_board(grid)




