
def find_exit_column(grid):
    rlen, clen = len(grid), len(grid[0])
    rcount, ccount = 0, 0

    output = []

    for ball in range(clen):
        is_stuck = False
        ccount = ball
        rcount = 0
        while rcount < rlen:
            val = grid[rcount][ccount]
            if val == 1 and ccount != clen-1:
                nxt_val = grid[rcount][ccount + 1]
                if nxt_val == 1:
                    ccount += 1
                else:
                    is_stuck = True
                    break
            elif val == -1 and ccount != 0:
                nxt_val = grid[rcount][ccount - 1]
                if nxt_val == -1:
                    ccount -= 1
                else:
                    is_stuck = True
                    break
            else:
                is_stuck = True
            
            rcount += 1

        
        result = ccount if is_stuck == False else -1
        output.append(result)
    
    return output



    


def print_grid(grid):
    for row in grid:
        line = ""
        for col in row:
            data = "\\" if col == 1 else "/"
            line += f"{data} "
        
        print(line)
            

if __name__ == "__main__":
    inpt = [[1,1,1,-1,1,1,1,1,1,-1,1,1],[-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1],[1,1,1,-1,1,1,1,1,1,-1,1,1],[-1,-1,-1,1,1,-1,-1,-1,-1,1,1,-1]]
    print_grid(inpt)
    result = find_exit_column(inpt)
    print(result)

