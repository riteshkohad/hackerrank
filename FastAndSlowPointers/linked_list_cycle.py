from linked_list import LinkedList
from linked_list_node import LinkedListNode


def detect_cycle(head):
    # define slow and fast pointers
    slow = head 
    fast = head.next.next

    # declare loop to keep traversing the linked list 
    while fast != None or fast == slow:
        # check if next to fast or next to next to fast is a None value
        if fast.next == None or fast.next.next == None:
            # if so that means linked list will be ending and no cycle exists 
            return False

        # increment slow pointer by one iteration 
        slow = slow.next
        # increment fast pointer by two iterations 
        fast = fast.next.next

        # check if fast pointer is matching with slow 
        if fast == slow:
            # if so, then cycle exists in the linked list
            return True

    # if code come out of loop that means no cycle exists 
    return False



if __name__ == "__main__":
    lst = [69, 8, 49, 106, 116, 112]
    n = 6

    lnkLst = LinkedList()
    lnkLst.create_linked_list(lst)
    print(lnkLst)

    ret = detect_cycle(lnkLst.head)
    print(ret)

