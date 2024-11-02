
def strStr(haystack: str, needle: str) -> int:
    # ndl = len(needle)

    # for i in range(len(haystack) - ndl + 1 ):
    #     print(haystack[i: i + ndl])
    #     if haystack[i: i + ndl] == needle:
    #         return i

    # return -1

    # Sliding window approach 

    # l, r = 0, 0
    # ln = len(needle)

    # for l in range(len(haystack) - ln + 1):
    #     if haystack[l] == needle[0]:
    #         if ln > 1:
    #             for r in range(1, ln):
    #                 print(needle[r])
    #                 if haystack[l+r] != needle[r]:
    #                     break
                    
    #                 if r == ln -1:
    #                     return l
    #         else:
    #             return l
    # return -1

    # best approach 
    return haystack.find(needle)


if __name__ == "__main__":
    inpt = "leetcode"
    inpt2 = "leeto"
    result = strStr(inpt, inpt2)
    print(result)