from heapq import *


def k_smallest_pairs(nums1, nums2, k):
    if not nums1 and not nums2:
        return -5

    # 1. Initialize min heap to store tuple(sum, i, j)
    min_sum = []
    # 1.1 Initialize set to store visited locations 
    visited = set()

    # 1.2 calculate tuple (sum of index 0 from both lists,0, 0)
    val = (nums1[0] + nums2[0], 0, 0)
    # 1.3 push it to min heap and add indexes to the visited list
    heappush(min_sum, val)
    visited.add((0, 0))

    # 2. Define result list and loop until k > 0 and heap has some value in it
    result = []
    while k > 0 and min_sum:
        # 2.1 pop the element from heap, it will be the smallest one always
        s, i, j = heappop(min_sum)
        # 2.2 add it to the result list and reduce the k as we found the element 
        result.append([nums1[i], nums2[j]])
        k -= 1

        # 2.3 check if i+1 element exists in 1st list, if so, then create a tuple (sum of i+1 and j, i+1 , j) and push it in the min heap
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            val = (nums1[i + 1] + nums2[j], i + 1, j)
            heappush(min_sum, val)
            visited.add((i + 1, j))
        
        # 2.4 check if j+1 element exists in 2nd list, if so, then create a tuple (sum of i and j+1, i , j+1) and push it in the min heap
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            val = (nums1[i] + nums2[j + 1], i, j + 1)
            heappush(min_sum, val)
            visited.add((i, j + 1))

    # 3. return the result set
    return result



if __name__ == "__main__":
    inpt_list1 = [1, 7, 11]
    inpt_list2 = [2, 4, 6]
    inpt_k = 3

    ret_val = k_smallest_pairs(inpt_list1, inpt_list2, inpt_k)
    print(ret_val)