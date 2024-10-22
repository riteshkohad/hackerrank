
def merge(nums1, m: int, nums2, n: int) -> None:
    # Brute force solution could be go over the both arrays and create a new array with sorted elements 
    # Brute force solution could be to add nums 2 to the nums1 array at the end and use sort function to sort it, it will take O(n log n) time
    # Optimal way is to use two pointers, check elements from backwards from m & n location and update the nums1 array

    # declare two pointers 
    one, two = m-1, n-1
    l = len(nums1) - 1

    # loop thru until both pointers are >= 0
    while one >= 0 and two >= 0:
        max_value = 0
        if nums1[one] >= nums2[two]:
            nums1[l] = nums1[one]
            one -= 1
        else:
            nums1[l] = nums2[two]
            two -= 1
        
        l -= 1
    
    # loop thru the remaining elements if there are any
    while two >= 0:
        nums1[l] = nums2[two]
        two -= 1
        l -= 1
    
    print(nums1)


    


if __name__ == "__main__":
    inpt1 = [1,2,3,0,0,0]
    inpt2 = [2,5,6]
    m = 3
    n = 3
    result = merge(inpt1, m, inpt2, n)
    print(result)