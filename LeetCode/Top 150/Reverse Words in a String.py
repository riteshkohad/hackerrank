
def reverseWords(s: str) -> str:
    tmp = output = ""

    for char in s.strip():
        tmp += char
        if char == " ":
            output = tmp.strip() + " " + output.strip()
            tmp = ""

    return tmp.strip() + " " + output.strip()


if __name__ == "__main__":
    inpt = " a good   example "
    result = reverseWords(inpt)
    print(result)