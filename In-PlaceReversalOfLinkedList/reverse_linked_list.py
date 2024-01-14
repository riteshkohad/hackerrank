from linked_list import LinkedList
from linked_list_node import LinkedListNode

"""
Time complexity: The time complexity of the function reverse is O(n), where n is the number of nodes in the linked list. 
This is because the function iterates through each node in the linked list once. The time complexity of the built-in Python 
functions used in the code, such as reversed and insert_node_at_head, is O(1) as they perform constant time operations.

Space complexity: The space complexity of the function reverse is O(1) because it only uses a constant amount of extra space for 
the variables prev, nxt, and curr. The built-in Python functions invoked by the code, such as reversed and str, do not contribute 
to the space complexity as they operate on the existing data without creating additional data structures.
"""



def reverse(head):
    # declare variables for prev and next
    prev, nxt = None, None
    # take current pointer
    curr = head

    # loop till curr is not None
    while curr:
        # print(f"prev:{ prev.data if prev else None} <- curr: { curr.data if curr else None} -> Next {nxt.data if nxt else None}")
        # take a next node and save it 
        nxt = curr.next
        # assign prev node to Next node to the current 
        curr.next = prev
        # assign current node to prev one so tha next time this code can be attached to the next node 
        prev = curr

        # make next node as a current 
        curr = nxt 

        # print(f"prev:{ prev.data if prev else None} <- curr: { curr.data if curr else None} -> Next {nxt.data if nxt else None}")
        # print("--")

    # return prev node 
    return prev


def main():
    inpt = [1,-2,3,4,-5,4,3,-2,1, 6]
    lnkList = LinkedList()
    lnkList.create_linked_list(inpt)
    print(lnkList)
    ret_val = reverse(lnkList.head)
    print(ret_val)
    lnkList.head = ret_val
    print(lnkList)
    


if __name__ == "__main__":
    main()

