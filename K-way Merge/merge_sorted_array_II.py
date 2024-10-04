

def merge_sorted(nums1, m, nums2, n):
    # 1. Initialize 2 end pointers to store last data points
    e1, e2 = m-1, n-1
    # 2. Initialize a pointer to track a last position of the nums1 list
    cur = len(nums1)-1

    # 3. Loop till both end pointers are >= 0 
    while e1 >= 0 and e2 >= 0:
        # 4. Compare value of nums1 vs nums2
        if nums1[e1] > nums2[e2]:
            # 4.1 if nums1 is > swap it with nums1[curr] 
            nums1[cur] = nums1[e1]
            # 4.1.1 Move end pointer backwards
            e1 = e1 - 1 
        else:
            # 4.2 otherwise, swap nums1[curr] with nums[e2] 
            nums1[cur] = nums2[e2]
            # 4.2.1 Move end pointer backwards
            e2 = e2 - 1 

        # 5. move end pointer backwards 
        cur -= 1

    # 6. Travel all the numb2 leftover elements and add it in the nums1[curr]
    while e2 >= 0:
        nums1[cur] = nums2[e2]
        e2 = e2 - 1
        cur -= 1

    # 7. return nums1
    return nums1


if __name__ == "__main__":
    inpt1 = [0,1,4,9,0,0,0,0,0,0]
    inpt2 = [-111,-20,-5,5,11,20]  
    m, n = 4, 6

    ret_val = merge_sorted(inpt1, m, inpt2, n)
    print(ret_val)