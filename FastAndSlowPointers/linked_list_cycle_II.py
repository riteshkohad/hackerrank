from linked_list import LinkedList
from linked_list_node import LinkedListNode


def detect_cycle(head):
    fast, slow = head.next.next, head

    while fast != None or fast == slow:
        if fast.next == None or fast.next.next == None:
            return False

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False


if __name__ == "__main__":
    lst = [69, 8, 49, 106, 116, 112]
    n = 49

    lnkLst = LinkedList()
    lnkLst.create_linked_list(lst)
    # print(lnkLst)

    ret = detect_cycle(lnkLst.head)
    print(ret)