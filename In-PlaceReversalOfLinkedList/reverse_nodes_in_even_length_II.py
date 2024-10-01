from linked_list import LinkedList
from linked_list_node import LinkedListNode

# incomplete 

def reverse_even_length_groups(head):
    l,n = 1, 1
    cur = head
    while cur:
        if n > l:
            n = 1
            l += 1
        else:
            print(f"processing l: {l} group and n: {n}th node {cur.data}")
            n += 1
        cur = cur.next
            


    print("hello")
    return head


if __name__ == "__main__":
    inpt = [1,2,3,4]
    lkd_lst = LinkedList()
    lkd_lst.create_linked_list(inpt)
    lkd_lst.print_linked_list()
    ret_val = reverse_even_length_groups(lkd_lst.head)
    print(ret_val)