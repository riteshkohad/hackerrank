

def removeElement(nums, val: int) -> int:
    # Brut force solution could be loop thru the array and remove the each element that is asked to remove
    # remove() function will remove the element but we have to loop thru the entire array
    # optimal way is to use two pointers from start and end and keep swapping the element == val
    # in-short, push all those elements towards the end

    start, end = 0 , len(nums) -1
    # l = len(nums) - 1 

    result = 0
    while start <= end:
        if nums[end] == val:
            end -= 1
            continue

        if nums[start] == val:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1    

        result += 1
        start += 1
    return result



if __name__ == "__main__":
    inpt = [3,2,2,3]
    v = 3
    result = removeElement(inpt, v)
    print(result)
