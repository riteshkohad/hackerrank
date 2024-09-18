

def longest_repeating_character_replacement(s, k):
    max_len = start = end = 0 
    char_len = {}

    # start with the end pointer 
    while end < len(s):
        # check if current char is in the hashmap
        if s[end] in char_len:
            # if it is, then increment it by 1
            char_len[s[end]] += 1
        else:
            # if not, add it 
            char_len[s[end]] = 1

        # maintain the variable with max length 
        max_len = max(max_len, char_len[s[end]])

        # check if sliding window is exceeded 
        # (end - start) + 1 - max_length should be less than or equal to the k
        if end - start + 1 - max_len > k:
            # if it exceeded then decrement the count 
            char_len[s[start]] -= 1
            # move the starting pointer of the sliding window 
            start +=1 

        print(char_len)
        end += 1
    
    return end - start


if __name__ == "__main__":
    inpt_str = "aaacbbbaabab"
    inpt_cht = 2
    val = longest_repeating_character_replacement(inpt_str, inpt_cht)
    print(val)