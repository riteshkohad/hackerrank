from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reorder_list(head):
    # 1. Use fast and slow pointer pattern to find middle of the linked list
    slow, fast = head, head.next
    # use loop to move fast and slow pointers 
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # 2. Save second node and reverse the rest of the linked list 
    # starting from the slow.next 
    second = slow.next
    # define prev variable, make sure to set None to slow.next 
    prev, slow.next = None, None
    # loop to travel thru rest of the linked list 
    while second:
        # logic to reverse the linked list
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    
    # 3. Take a two pointers for first and second list 
    first, second = head, prev
    while second:
        # logic to add one of each node together 
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

    # return the node
    return head

def print_linked_list(head):
    cur = head
    while cur:
        print(cur.data)
        cur = cur.next


if __name__ == "__main__":
    inpt = [10,20,-22,21,-12]
    lnkList = LinkedList()
    lnkList.create_linked_list(inpt)
    print_linked_list(lnkList.head)
    result = reorder_list(lnkList.head)
    print_linked_list(result)
    print(result)