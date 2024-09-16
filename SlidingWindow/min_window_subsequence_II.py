

def min_window(str1, str2):
    s, e = 0, 0
    start_found = end_found = False
    output = ""
    cur_str2_char = 0

    for i, ch in enumerate(str1):
        # print(f"index:{i} char: {ch}")
        # print(f"str2 {str2[cur_str2_char]}")
        if ch == str2[cur_str2_char]:
            # print(f"char found: {ch} - {str2[cur_str2_char]}: count {cur_str2_char}")

            if start_found == False and str2[0] == ch:
                start_found = True
                s = i
                continue
                # print(f"START found: {s} :char :{str1[s]}")
            
            if end_found == False and str2[-1] == ch:
                end_found = True
                e = i
                # print(f"END found: {e} :char :{str1[e]}")

            if cur_str2_char < len(str2)-1:
                cur_str2_char += 1


        if start_found == True and end_found == True:
            # print(f"phase 2")
            tmp = e
            for ch2 in range(tmp,0 ,-1):
                ln = len(str2) - 1
                # print(f"ch2: {ch2}")
                if str2[ln] == str1[ch2]:
                    # print(f"found: {str2[0]} == {str1[tmp]}")
                    ln -= 1

                    if ln == 0:
                        s = tmp
                        break
        
        output = str1[s:e+1]
    return output


    



if __name__ == "__main__":
    inpt_str1 = "afgegrwgwga"
    inpt_str2 = "aa"
    val = min_window(inpt_str1, inpt_str2)
    print(val)

