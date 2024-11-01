
def intToRoman(num: int) -> str:
    data = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1) ]
    result = ""
    
    for symbol, val in data:
        # print(num // val)
        if num // val:
            count = num // val
            result += symbol * count
            num = num % val

    return result


if __name__ == "__main__":
    inpt = 3749
    result = intToRoman(inpt)
    print(result)