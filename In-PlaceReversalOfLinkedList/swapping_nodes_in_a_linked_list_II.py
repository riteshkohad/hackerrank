from linked_list import LinkedList
from linked_list_node import LinkedListNode


def swap_nodes(head, k):
    # 1. Initialize the pointers curr and count 
    curr, count = head, 1

    # 2. traverse the list till count is equal to k, keep moving curr and count 
    while count < k:
        # moving count and curr
        count += 1
        curr = curr.next
    
    # 3. Assign curr to new variable called front and create new variable called end with initial value as head 
    front = curr
    end = head
    
    # 4. Keep traveling until curr.next is null while moving curr and end variable, 
    # at the end of the loop end will point to the node which needs to be swapped  
    while curr.next:
        # moving curr and end variable 
        curr = curr.next
        end = end.next
    
    # 5. swap front and end node DATA (values) not a pointers 
    tmp = end.data
    end.data = front.data
    front.data = tmp
    
    # 6. Return head
    return head


def print_linked_list(head):
    cur = head
    while cur:
        print(cur.data)
        cur = cur.next


if __name__ == "__main__":
    inpt = [1,2,3,4,5]
    k = 3
    lnkList = LinkedList()
    lnkList.create_linked_list(inpt)
    # print_linked_list(lnkList.head)
    result = swap_nodes(lnkList.head, k)
    print_linked_list(result)
    # print(f"head data: {result.data}")
