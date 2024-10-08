from linked_list import LinkedList
from linked_list_node import LinkedListNode
from heapq import *


def merge_k_lists(lists):
    min_heap = []

    for i, node in enumerate(lists):
        val = (node.data, i, node)
        heappush(min_heap, val)
    
    dummy = LinkedListNode(None)
    curr = dummy

    while min_heap:
        data, i, node = heappop(min_heap)
        curr.next = node
        curr = node
        node = node.next

        if node:
            val = (node.data, i, node)
            heappush(min_heap, val)
            
    return dummy.next


if __name__ == "__main__":
    print("Hello")
    lsts = [[21,23,42],[1,2,4]]

    lists = []
    for lst in lsts:
        lnkLst = LinkedList()
        lnkLst.create_linked_list(lst)

        lists.append(lnkLst.head)
    # print(lnkLst)

    ret = merge_k_lists(lists)
    while ret:
        print(ret.data)
        ret = ret.next
    
