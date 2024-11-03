
def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        sm = numbers[l] + numbers[r]
        if sm == target:
            return [l + 1, r + 1]
        elif sm < target:
            l += 1
        elif sm > target:
            r -= 1


if __name__ == "__main__":
    inpt = [-1,0]
    inpt2 = -1
    result = twoSum(inpt, inpt2)
    print(result)