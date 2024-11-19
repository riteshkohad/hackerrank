
def spiralOrder(matrix):
    # define walls
    lwall, rwall, bwall, twall = 0, len(matrix) - 1, len(matrix[0]) -1, 0
    direction = "Right"
    row, col = 0, 0
    output = []

    while (lwall != rwall) or (twall != bwall):
        if direction == "Right":
            row = lwall
            col = twall
            
            for i in range(rwall + 1):
                output.append(matrix[row][col])
                col += 1

            twall += 1
            direction = "Down"
        elif direction == "Down":
            row = twall
            col = rwall

            for i in range(bwall):
                output.append(matrix[row][col])
                row += 1

            rwall -= 1
            direction = "Left"
        elif direction == "Left":
            row = bwall
            col = rwall

            for i in range(rwall + 1):
                output.append(matrix[row][col])
                col -= 1
            
            bwall -= 1
            direction = "Up"
        elif direction == "Up":
            row = bwall
            col = lwall
            # row -= 1
            for i in range(twall):
                output.append(matrix[row][col])
                row -= 1
            
            lwall += 1
            direction = "Right"

    return output
4

if __name__ == "__main__":
    inpt = [[1,2,3],[4,5,6],[7,8,9]]
    result = spiralOrder(inpt)
    print(result)