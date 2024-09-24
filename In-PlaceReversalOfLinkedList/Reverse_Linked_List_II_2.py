from linked_list import LinkedList
from linked_list_node import LinkedListNode


# Function to reverse the sublist within the linked list
def reverse_between(head, left, right):
    # 1. Create a dummy node with head as a next 
    dummy = LinkedListNode(0, head)

    # 2. create a variables to hold previous to left and current node 
    left_prev, curr = dummy, head

    # 3. Travel till left location while saving previous and next node in the variables above 
    for i in range(left -1):
        left_prev, curr = curr, curr.next
    
    # define a variable to hold prev node 
    prev = None
    # 4. loop thru all the elements till right location 
    for i in range(right - left + 1):
        # reverse the linked list 
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    
    # 5. reassign left and last pointer 
    left_prev.next.next = curr
    left_prev.next = prev

    # 6. Return the starting of the linked list 
    return dummy.next


def print_linked_list(head):
    cur = head
    while cur:
        print(cur.data)
        cur = cur.next


if __name__ == "__main__":
    inpt = [1,2,3,4,5,6,7,8,9]
    l = 2
    r = 5
    lnkList = LinkedList()
    lnkList.create_linked_list(inpt)
    print_linked_list(lnkList.head)
    result = reverse_between(lnkList.head, l, r)
    print_linked_list(result)
    print(result.data)