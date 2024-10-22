

def productExceptSelf(nums):
    result = [1] * (len(nums))
    prod = 1

    # go left to right and calculate the product 
    for i, val in enumerate(nums):
        result[i] *= prod
        prod *= val

    # go right to left and calculate the product 
    prod = 1
    for i in range(len(nums) -1, -1, -1):
        result[i] *= prod
        prod *= nums[i]

    return result

if __name__ == "__main__":
    inpt = [-1,1,0,-3,3]
    result = productExceptSelf(inpt)
    print(result)