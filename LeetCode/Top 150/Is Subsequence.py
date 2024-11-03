
def isSubsequence(s: str, t: str) -> bool:
    if not s:
        return False

    l = 0
    ln = len(s)

    for char in t:
        if char == s[l]:
            l += 1
            if l == ln:
                return True
    
    return True if ln == l else False


if __name__ == "__main__":
    inpt = "b"
    inpt2 = "abc"
    result = isSubsequence(inpt, inpt2)
    print(result)