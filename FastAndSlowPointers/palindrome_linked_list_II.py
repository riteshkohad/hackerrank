from linked_list import LinkedList
from linked_list_node import LinkedListNode


def palindrome(head):
    slow = fast = head

    while fast.next != None:
        print(f"Slow: {slow.data} == Fast: {fast.data}")
                    
        if fast.next.next == None:
            fast = fast.next
            break 
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the remaining linked list 
    prev, nxt = None, None
    curr = slow
    while curr != None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    slow = head

    while fast.next != None:
        print(f"slow :{slow.data} fast : {fast.data}")
        if slow.data != fast.data:
            return False
        # if slow.next != None and fast.next != None:
        slow = slow.next 
        fast = fast.next
    
    return True







if __name__ == "__main__":
    lst = [1,2,3,2,1]

    lnkLst = LinkedList()
    lnkLst.create_linked_list(lst)
    # print(lnkLst)

    ret = palindrome(lnkLst.head)
    print(ret)