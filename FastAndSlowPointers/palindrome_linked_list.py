from linked_list import LinkedList
from linked_list_node import LinkedListNode
from linked_list_reverse import reverse_linked_list

"""
Time complexity:
The time complexity of the function palindrome is O(n), where n is the number of nodes in the linked list. 
This is because we traverse the linked list twice - once to find the middle node using the fast and slow pointers 
pattern, and once to compare the reversed second half of the linked list with the first half. The time complexity 
of reversing the second half of the linked list is also O(n).

Space complexity:
The space complexity of the function Palindrome Linked List is O(1). This is because the function only uses a 
constant amount of extra space to store the slow and fast pointers, as well as the variables used in the while loop. 
The space complexity does not include the space used by the built-in Python functions invoked by the code, as their 
space complexity is not explicitly mentioned in the code
"""

def palindrome(head):
    # define the slow and fast pointers at the head
    slow = head 
    fast = head

    # loop till end of the list 
    while fast.next:

        # if there is next.next still exists
        if fast.next.next:
            # move the slow pointer by 1
            slow = slow.next
            # move fast pointer by 1
            fast = fast.next.next
        else:
            # otherwise break the loop
            break
    
    # reverse the linked list from middle to end 
    # in first loop, fast pointer traveled to end 
    # and slow pointer was in middle, so give slow pointer to reverse the rest of the linked list  
    rev = reverse_linked_list(slow)

    # reset the slow pointer to head 
    slow = head

    # loop thru the reversed list
    while rev.next:
        # if data does not match with reverse and the original 
        if rev.data != slow.data:
            # then it is not palindrome string 
            return False
        
        # move to next element 
        slow = slow.next
        rev = rev.next
    
    # if all nodes are matching, return true
    return True


if __name__ == "__main__":
    lst = [6, 1, 0, 5, 1, 6]
    n = 6

    lnkLst = LinkedList()
    lnkLst.create_linked_list(lst)
    
    ret_val = palindrome(lnkLst.head)
    print(ret_val)