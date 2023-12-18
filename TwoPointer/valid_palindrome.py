

def is_palindrome(s):
    ln = len(s) // 2
    for x in range(ln):
        if s[x] != s[(len(s)-1) - x]:
            return False 

    return True

def is_palindrome_real_two_pointers(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1 
        right = right - 1
    return True


if __name__ == "__main__":
    input = "abba"
    result = is_palindrome(input)

    print(f"Input string is Palindrome: {result}")