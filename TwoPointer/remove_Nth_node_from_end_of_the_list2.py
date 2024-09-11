from linked_list import LinkedList
from linked_list_node import LinkedListNode

def remove_nth_last_node(head, n):
    temp = left = right = head
    
    # go till the Nth node
    for i in range(n-1):
        right = right.next

    if right.next == None:
        print(f"Exiting")
        return head.next
    
    while right.next != None:
        print(f"going next: {right.data}")
        temp = left
        left = left.next
        right = right.next
    
    temp.next = left.next
    print(f"right: {right.data}")
    
    return head




if __name__ == "__main__":
    lst = [69, 8, 49, 106, 116, 112]
    n = 5

    lnkLst = LinkedList()
    lnkLst.create_linked_list(lst)
    print(lnkLst)

    print(lnkLst.head.data)
    print(lnkLst.head.next)

    head = remove_nth_last_node(lnkLst.head, n)

    while head != None:
        print(head.data)
        head = head.next
