import re

def reverse_words(sentence):
    sentence = re.sub(" +", " ", sentence.strip())
    # print(f"[{sentence}]")
    rev_str = sentence[::-1]
    print(rev_str)

    start, end = 0, 0
    ret_val = ""

    while end <= len(sentence)-1:
        if rev_str[end] == " " or end == len(sentence) -1:
            word = rev_str[start:end+1]
            ret_val = ret_val + " " + word[::-1]
            start = end
            # end +=1
        
        end += 1

    return re.sub(" +", " ", ret_val.strip())
        


if __name__ == "__main__":
    txt = "  hello how are you?  "
    val = reverse_words(txt)
    print(val)