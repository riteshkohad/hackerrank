from linked_list import LinkedList
from linked_list_node import LinkedListNode

"""
Time complexity:
The time complexity of the function get_middle_node is O(n), where n is the number of nodes in the linked list. 
This is because we iterate through the linked list once using the fast and slow pointers, and the number of iterations 
is proportional to the number of nodes in the linked list. The time complexity of the built-in Python functions used 
in the code, such as reversed and __str__, is not considered in the analysis as they have a time complexity of O(n) or less.

Space complexity:
The space complexity of the function get_middle_node is O(1) because it only uses a constant amount of extra space to store the 
slow and fast pointers. The space complexity of the built-in Python functions invoked by the code is also O(1) because they 
do not use any extra space that grows with the input size.
"""


def get_middle_node(head):
    # check if next node is available 
    if head.next == None:
        # if not, return the head
        return head
    
    # declare fast and slow pointers and assign with the same starting position 
    slow = head
    fast = head

    # loop till the last node 
    while fast.next:
        # move slow pointer by 1 iteration 
        slow = slow.next
        # move fast by 2 iterations 
        fast = fast.next.next

        # if fast is none or next of fast is none that means we are at the end of the list 
        if fast == None or fast.next == None:
            # return the slow pointer 
            return slow



if __name__ == "__main__":
    lst = [69, 8, 49, 106, 116]
    n = 6

    lnkLst = LinkedList()
    lnkLst.create_linked_list(lst)
    
    ret_val = get_middle_node(lnkLst.head)
    print(ret_val.data)
