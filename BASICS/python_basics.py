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


def stack():
    # declare a list
    var_stack = []

    # we can use this list as a stack (LIFO) operations
    # 1. add values into it
    var_stack.append(2)
    var_stack.append(4)
    var_stack.append(6)
    var_stack.append(8)

    # print stack to see the values 
    print(f"Printing stack values: {var_stack}")

    # remove values from list like stack
    element = var_stack.pop(-1)
    print(f"last popped element is: {element}, remaining values in stack is: {var_stack}")
    element = var_stack.pop(-1)
    print(f"last popped element is: {element}, remaining values in stack is: {var_stack}")
    element = var_stack.pop(-1)
    print(f"last popped element is: {element}, remaining values in stack is: {var_stack}")


def queue():
    # declare a list
    var_queue = []

    # we can use this list as a Queue (FIFO) operations
    # 1. add values into it
    var_queue.append(2)
    var_queue.append(4)
    var_queue.append(6)
    var_queue.append(8)

    # print queue to see the values 
    print(f"Printing queue values: {var_queue}")

    # remove values from list like queue
    element = var_queue.pop(0)
    print(f"last popped element is: {element}, remaining values in queue is: {var_queue}")
    element = var_queue.pop(0)
    print(f"last popped element is: {element}, remaining values in queue is: {var_queue}")
    element = var_queue.pop(0)
    print(f"last popped element is: {element}, remaining values in queue is: {var_queue}")


def main():
    # min_heap()
    # stack()
    queue()



if __name__ == "__main__":
    main()