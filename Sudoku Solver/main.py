# We use backtracking when we have to proceed with several choices
# Project on Backtracking and Recursion


def is_valid_move(grid, row, col, number): #This function checks whether placing number at grid[row][col] is valid.
    for x in range(9): #For checking for same number in row
        if grid[row][x] == number:
            return False
    for x in range(9): #for checking of same number in column
        if grid[x][col] == number:
            return False
        
    corner_row = row - row%3
    corner_col = col - col%3

    for x in range(3): #For checking for same number in 3x3 Grid
        for y in range(3): 
           if grid[corner_row + x][corner_col + y] == number:
              return False
        
    return True

def solve(grid, row, col): #Recursively Solves The Grid using Backtracking

    if col == 9:
        if row == 8:
            return True
        row += 1  # Last Column reached now we will check new next row and start from 1st column
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col +1) #Recursion
    
    for num in range(1,10):

        if is_valid_move(grid, row, col, num):

            grid[row][col] = num

            if solve(grid, row, col +1):
                return True
            
        grid[row][col] = 0

    return False

grid = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]
 #Initialising Sudoku Grid

if solve(grid,0 ,0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No Solution For This Sudoku")