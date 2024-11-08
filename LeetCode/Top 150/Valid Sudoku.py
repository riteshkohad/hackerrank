
def isValidSudoku(board) -> bool:
    ln = len(board)

    for r in range(ln):
        dic = {}
        for c in range(ln):
            char = board[r][c]
            if char == ".":
                continue

            if char in dic:
                # print(f"char: {char} dict: {dic}")
                return False
            else:
                dic[char] = dic.get(char, 0 ) + 1
        # print(dic)
    
    for c in range(ln):
        dic = {}
        for r in range(ln):
            char = board[r][c]
            if char == ".":
                continue

            if char in dic:
                return False
            else:
                dic[char] = dic.get(char, 0 ) + 1
        # print(dic)

    rc, cc = 0, 0
    
    for i in range(3):
        rc = 0
        for j in range(3):
            cc = 0
            for r in range(3):
                dic = {}
                for c in range(3):
                    # print(r, c)
                    char = board[r + rc][c + cc]
                    if char == ".":
                        continue

                    if char in dic:
                        return False
                    else:
                        dic[char] = dic.get(char, 0 ) + 1
                    cc += 1
                rc += 1
                print(dic)

    return True

if __name__ == "__main__":
    inpt = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    result = isValidSudoku(inpt)
    print(result)



[
    [".",".",".", ".","5",".", ".","1","."],
    [".","4","." ,"3",".",".", ".",".","."],
    [".",".","." ,".",".","3", ".",".","1"],

    ["8",".","." ,".",".",".", ".","2","."],
    [".",".","2" ,".","7",".", ".",".","."],
    [".","1","5" ,".",".",".", ".",".","."],

    [".",".","." ,".",".","2", ".",".","."],
    [".","2","." ,"9",".",".", ".",".","."],
    [".",".","4" ,".",".",".", ".",".","."]]