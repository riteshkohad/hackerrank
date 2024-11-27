
def find_exit_column(grid):
    rows, cols = len(grid), len(grid[0])
    output = []
    dead_end = False

    for ball in range(cols):
        row, col = 0, ball

        while row < rows and col < cols:
            val = grid[row][col]
            if val == 1:
                if col != cols -1 and grid[row][col + 1] != -1:
                    col += 1
                else:
                    dead_end = True
                    break
            else:
                if col > 0 and grid[row][col - 1] != 1:
                    col -= 1
                else:
                    dead_end = True
                    break
            
            row += 1

        output.append(col if dead_end == False else -1)

    return output

def print_grid(grid):
    for item in grid:
        print(item)
    
    print("-"*10)

if __name__ == "__main__":
    inpt = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    print_grid(inpt)
    result = find_exit_column(inpt)
    print(result)