from typing import Optional
from list_node import ListNode 
from linked_list import LinkedList

# this is fast and slow pointer solution in leetcode it is considered as two pointers 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        fast = head
        slow = head

        # for i in range(n):
        #     fast = fast.next
        while i < n:
            fast = fast.next
            i += 1

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head



def main():
    inpt = [1,2,3,4,5]
    num = 2
    lnkLst = LinkedList()
    lnkLst.create_linked_list(inpt)
    print(lnkLst)
    
    sln = Solution()
    ret_val = sln.removeNthFromEnd(lnkLst.head, num)




if __name__ == "__main__":
    main()