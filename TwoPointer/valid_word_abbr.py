def valid_word_abbreviation(word, abbr):
    wrd_pointer = abbr_pointer = 0
    num = ""

    if len(abbr) > len(word):
        return False
    elif len(abbr) == 1:
        if abbr.isnumeric() and int(abbr) == len(word):
            return True
        # else:
        #     return True
        

    for indx, val in enumerate(abbr):
        if val.isnumeric():
            num += val
            print(num)
            if wrd_pointer + int(num) > len(word) -1:
                return False
        else:
            if len(num) > 0:
                wrd_pointer += int(num)
                if wrd_pointer > len(word)-1:
                    return False

            if val != word[wrd_pointer]:
                return False
            
            num = ""
            wrd_pointer +=1
        # print(f" {abbr[indx]} is numeric: {abbr[indx].isnumeric()}")    
    return wrd_pointer == len(word) and indx == len(abbr)



if __name__ == "__main__":
    word = "lu"
    abbr = "2"

    val = valid_word_abbreviation(word=word, abbr=abbr)
    print(val)