from linked_list import LinkedList
from linked_list_node import LinkedListNode

def get_middle_node(head):
    if head == None:
        return None
    
    fast, slow = head, head

    while fast.next != None:
        if fast.next == None:
            return slow
        elif fast.next.next == None:
            return slow.next
        
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    lst = [1,2]

    lnkLst = LinkedList()
    lnkLst.create_linked_list(lst)
    # print(lnkLst)

    ret = get_middle_node(lnkLst.head)
    print(ret.data)