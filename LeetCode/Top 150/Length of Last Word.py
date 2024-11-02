

def lengthOfLastWord(s: str) -> int:
    count = 0
    for char in s.strip()[::-1]:
        # print(char)
        if char == " ":
            return count
        else:
            count += 1

    return count


if __name__ == "__main__":
    inpt = "Hello World"
    result = lengthOfLastWord(inpt)
    print(result)