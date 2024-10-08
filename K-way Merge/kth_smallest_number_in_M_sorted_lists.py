from heapq import *



def k_smallest_number(lists, k):
    # 1. Define min heap
    min_heap = []
    is_empty = True

    # 1.1 Add first element of each list in the min heap
    for i in range(len(lists)):
        if lists[i]:
            is_empty = False
            val = (lists[i][0], i, 0) 
            heappush(min_heap, val)
        

    if is_empty:
        return 0

    # 2. Loop till count < k
    count = 0

    # 3. Pop the min element from the heap if heap is not empty
    while count < k:
        if min_heap: 
            min_val, list_index, element_index = heappop(min_heap)
            count += 1

            # 3.1 If count == k, return min_val
            if count == k:
                return min_val
            
            # 3.2 Add next element of the list in the heap if list has more elements
            if element_index + 1 < len(lists[list_index]):
                next_val = (lists[list_index][element_index+1], list_index, element_index+1)
                heappush(min_heap, next_val)
        else:
            return min_val

    return -1


if __name__ == "__main__":
    inpt_list = [[1,1,1],[1,1,1]]
    inpt_k = 4

    ret_val = k_smallest_number(inpt_list, inpt_k)
    print(ret_val)

