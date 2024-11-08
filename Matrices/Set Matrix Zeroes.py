def set_matrix_zeros(mat):
    fcol, frow = False, False
    rlen, clen = len(mat), len(mat[0])

    for c in range(clen):
        if mat[0][c] == 0:
            frow = True
            break
    
    for r in range(rlen):
        if mat[r][0] == 0:
            fcol = True
            break

    for r, row in enumerate(mat):
        for c, val in enumerate(row):
            if val == 0:
                mat[r][0] = 0
                mat[0][c] = 0
    print_matrix(mat)
    # fill in cols with zeros
    for c in range(1, clen):
        if mat[0][c] == 0:
            for r in range(1, rlen):
                mat[r][c] = 0

    # fill in rows with zeros
    for r in range(1, rlen):
        if mat[r][0] == 0:
            for c in range(1, clen):
                mat[r][c] = 0
    
    # if first col is zero then mark 0th col with zero in all rows
    if fcol == True:
        for r in range(1, rlen):
            mat[r][0] = 0

    if frow == True:
        for c in range(1, clen):
            mat[0][c] = 0

    # print_matrix(mat)
    return mat

def print_matrix(mat):
    for lst in mat:
        print(lst)

    print("-"*10)

if __name__ == "__main__":
    inpt = [[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1]]

    print_matrix(inpt)
    
    result = set_matrix_zeros(inpt)
    print_matrix(inpt)
    # print(result)