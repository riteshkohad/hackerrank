
def swap_char(word):
    lst_w = list(word)
    lst_w[0], lst_w[-1] = lst_w[-1], lst_w[0]

    return ''.join(lst_w)

def permute_word(word):
    tmp = ""
    if len(word) == 1:
        return tmp
    
    # do not pick
    


if __name__ == "__main__":
    inpt = "abc"
    result = permute_word(inpt)
    print(result)
