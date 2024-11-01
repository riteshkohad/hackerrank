

def romanToInt(s: str) -> int:
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, 
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900  }

    i = result = 0
    while i < len(s):
        char = s[i]

        if char in ["I", "X", "C"]:
            if i < len(s) - 1:
                if char + s[i+1] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                    result += dic[char + s[i+1]]
                    i += 2
                    continue

        result += dic[char]
        i += 1
    
    return result


if __name__ == "__main__":
    inpt = "MCMXCIV"
    result = romanToInt(inpt)
    print(result)