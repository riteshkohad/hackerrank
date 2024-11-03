

def lengthOfLongestSubstring(s: str) -> int:
    mx_len, tot = 0, 0
    dic = set()
    l, r = 0, 0

    while r < len(s):
        while s[r] in dic:
            dic.remove(s[l])
            l += 1
        
        dic.add(s[r])
        mx_len = max(mx_len, r - l + 1)
        r += 1

    return mx_len

if __name__ == "__main__":
    inpt = "abcabcbb"
    print(inpt)
    result = lengthOfLongestSubstring(inpt)
    print(result)