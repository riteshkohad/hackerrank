
def minSubArrayLen(target: int, nums) -> int:
    l, r = 0, 0
    ln = len(nums)
    total, min_len = 0, ln + 1

    while r < ln:
        # while total < target:
        total += nums[r]
        
        # print(f"l: {l}, r: {r}")
        while total >= target:
            if total >= target:
                # print(f"total {total} l: {l}, r: {r}")    
                total -= nums[l]
                min_len = min(min_len, r - l + 1)
                l += 1

        r += 1

    return min_len if min_len <= ln else 0


if __name__ == "__main__":
    inpt = 7
    inpt2 = [2,3,1,2,4,3]
    result = minSubArrayLen(inpt, inpt2)
    print(result)