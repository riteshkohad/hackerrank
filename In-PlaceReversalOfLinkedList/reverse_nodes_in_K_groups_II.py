from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reverse_list(head, end):
    cur = head
    prev, nxt = None, None
    while cur!=end:
        nxt = cur.next
        cur.next = prev

        prev = cur
        cur = nxt
    
    ret_val = prev

    while prev.next:
        print(f"cur: {prev.data} -> next: {prev.next.data}")
        prev = prev.next

    return ret_val


def reverse_k_groups(head, k):
    i, curr = 0, head
    while curr :
        print(f"i= {i} curr data: {curr.data}")
        curr = curr.next
        if i == k-1:
            head = reverse_list(head, curr)
            i = 0
        else:
            i += 1


if __name__ == "__main__":
    inpt = [1,2,3,4,5]
    inpt2 = 2
    lnkList = LinkedList()
    lnkList.create_linked_list(inpt)
    result = reverse_k_groups(lnkList.head, inpt2)
    print(result)