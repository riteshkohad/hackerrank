from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reverse(head):
    # check if head is null then return none
    if not head:
        return None
    
    # 1. Initialize the prev and nxt pointers
    prev, nxt = None, None
    # setting current pointer to the head
    current = head

    # 2. Traverse the linked list until "Current" pointer reaches the end of the list 
    while current:
        # 3. set the "Next" pointer to the next of the current node 
        nxt = current.next
        # and set the current node's pointer to point to the "Prev" node
        current.next = prev

        # 4. Update the "Prev" and "current" pointers 
        prev = current
        current = nxt

    # 5. After the loop, "Prev" pointer will point to the last node of the original linked list so set 
    # the "Head" pointer to the "Prev" pointer
    head = prev
    return head
    

if __name__ == "__main__":
    inpt = [1,-2,3,4,-5,4,3,-2,10]
    lnkList = LinkedList()
    lnkList.create_linked_list(inpt)
    result = reverse(lnkList.head)
    print(result.data)