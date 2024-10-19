
def permute_word(word):
    if len(word) == 0:
        return [""]
    
    combo = permute_word(word[1:])
    result = []
    for c in combo:
        for i in range(len(c) + 1):
            print(f"c: {c}")
            c_copy = c + word[0]
            # c_copy += word[0]
            result.append(c_copy)
    return result


if __name__ == "__main__":
    inpt = "abc"
    result = permute_word(inpt)
    print(result)