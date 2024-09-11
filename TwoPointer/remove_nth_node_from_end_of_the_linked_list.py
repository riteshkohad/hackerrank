from linked_list import LinkedList
from linked_list_node import LinkedListNode


"""
Solution summary
1. Two pointers, right and left, are set at the head node.
2. Move the right pointer n steps forward.
3. If right reaches NULL, return head's next node.
4. Move both right and left pointers forward till right reaches the last node.
5. Relink the left node to the node at left's next to the next node.
6. Return head.

Time complexity
The time complexity is O(n), where n is the number of nodes in the linked list.

Space complexity
The space complexity is O(1) because we use constant space to store two pointers
"""


def remove_nth_last_node(head, n):
    # declare temp nodes
    right = head
    left = head 
    i = 0
    # loop till nth place and advance the right node
    while i < n:
        right = right.next
        i += 1

    # if right is already at the end that means we need to remove first node
    if right == None:
        return head.next

    # loop till end of the linked list, move both pointers
    while right.next != None:
        right = right.next
        left = left.next
        
    # print(left.data)
    # print(right.data)

    # take next to next node 
    tmp = left.next.next
    # print(tmp.data)
    # assign to next to left node
    left.next = tmp
    # print("--"*10)

    # return head
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

    while head.next != None:
        print(head.data)
        head = head.next

