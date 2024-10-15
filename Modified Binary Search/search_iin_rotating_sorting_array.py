

def binary_search_rotated(nums, target):
    s, e = 0, len(nums) - 1

    while s <= e:
        m = (s + e) // 2
        if target == nums[m]:
            return m

        if nums[s] <= nums[m]:
            if target > nums[m] or target < nums[s]:
                s = m + 1
            else:
                e = m - 1
        else:
            if target < nums[m] or target > nums[e]:
                e = m - 1
            else:
                s = m + 1

    return -1


if __name__ == "__main__":
    inpt = [6,7,1,2,3,4,5]
    target = 1
    result = binary_search_rotated(inpt, target)
    print(result)