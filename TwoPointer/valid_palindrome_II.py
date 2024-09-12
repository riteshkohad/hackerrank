# Incorrect code it is failing for the example listed below

def is_palindrome(s):
    start, end = 0, len(s)-1 
    mismatch = 0
    while start<=end:
        if s[start] != s[end]:
            if s[start + 1] != s[end]:
                print(f"start: {start}, end: {end}, {s[start]} == {s[end]}, mistmatches: {mismatch}")

                if s[start] != s[end -1]:
                    print(f"start: {start}, end: {end}, {s[start]} == {s[end]}, mistmatches: {mismatch}")
                    return False
                else:
                    end -= 1
                    mismatch += 1
            else:
                start += 1
                mismatch += 1
            
            start += 1
            end -= 1
        else:
            start += 1
            end -= 1

    print(f"total mistmatchs: {mismatch}")
    if mismatch > 1:
        return False

    return True



if __name__ == "__main__":
    str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVgVUTSRQPONMLKLJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
    val = is_palindrome(str)
    print(val)