

def single_non_duplicate(nums): 
    s, e = 0, len(nums) - 1

    while s != e:
        mid = (s + e) // 2
        m = mid if mid % 2 == 0 else mid -1

        if nums[m] != nums[m +1]:
            e = m
        else:
            s = m + 2

    return nums[s]


if __name__ == "__main__":
    inpt = [1,1,2,2,3,3,4,4,5,5,8, 9,9]
    res = single_non_duplicate(inpt)
    print(res)


