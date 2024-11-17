
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    # output = [[0]* rows] * cols       # does not make a deep copy 
    # although output array is separate from matrix, the rows and cols are not deep copied, use following method

    output = [[0] * rows for _ in range(cols)] 

    for r in range(rows):
        for c in range(cols):
            output[c][r] = matrix[r][c]

    return output 
    


if __name__ == "__main__":
    inpt = [[1,2,3],[4,5,6]]
    result = transpose_matrix(inpt)
    print(result)

# 1   2   3
# 4   5   6
# 7   8   9

# 1   4   7
# 2   5   8
# 3   6   9


# 1   4   7
# 2   5
# 3