

def longestCommonPrefix(strs) -> str:
    min_str = min(strs)
    min_length = len(min_str)
    output = ""
    for i in range(min_length):
        char = min_str[i]
        for s in strs:
            if s[i] != char:
                return output
                
        output += char

    return output



if __name__ == "__main__":
    inpt = ["hello", "hell", "hel"]
    result = longestCommonPrefix(inpt)
    print(result)
