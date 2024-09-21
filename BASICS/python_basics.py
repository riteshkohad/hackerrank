import heapq

def min_heap():
    # declare list 
    var_heap = []

    # convert list to heap (min heap) Python only support min heap
    heapq.heapify(var_heap)

    # add new item to the heap
    heapq.heappush(var_heap, 10)

    for i in range(5):
        heapq.heappush(var_heap, i*10)    
        print(f"Min heap after inserting {i*10}: {var_heap}")

    while var_heap:
        heapq.heappop(var_heap)
        print(f"Min heap after popping a root element: {var_heap}")


def main():
    min_heap()





if __name__ == "__main__":
    main()