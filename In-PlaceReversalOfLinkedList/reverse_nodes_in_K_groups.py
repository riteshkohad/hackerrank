from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reverse_k_groups(head, k):
    if not head:
        print("No head")
        return

    if not k or k<1:
        print("No K")
        return 

    curr, nxt, prev, last = head, None, None, None 
    set_head = False
    new_head = None
    
    while curr:
        i = 1
        while i <= k and head.next:
            last = head.next
            i += 1

        head = last
        
        if set_head == False:
            new_head = last
            set_head = True
        
        print(f"i: {i} | k: {k}")

        if i == k+1:
            while curr != last:
                print(f"prev: {prev.data if prev else None} | curr: {curr.data if curr else None} | next: {nxt.data if nxt else None} | last: {last.data if last else None}")
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            print(curr.data)
            prev.next = curr
            curr = curr.next

    
    return new_head


def main():
    inpt = [1,2,3,4,5]
    k = 2
    lnkList = LinkedList()
    lnkList.create_linked_list(inpt)
    print(lnkList)

    ret_val = reverse_k_groups(lnkList.head, k)

    print(lnkList)


if __name__ == "__main__":
    main()


