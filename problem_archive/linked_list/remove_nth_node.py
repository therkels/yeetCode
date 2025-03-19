from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def build_linked_list(arr):
    head = ListNode(arr[0])
    ptr = head
    for i in range(1, len(arr)):
        ptr.next = ListNode(arr[i])
        ptr = ptr.next
    return head
def print_linked_list(head):
    ptr = head
    while ptr:
        print(ptr.val, end=" ")
        ptr = ptr.next
    print()
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #set the pointers
        dummy = ListNode(0, head)
        lead_ptr = dummy
        remove_ptr = dummy
        #position lead pointer to offset by n (remove_ptr.next will be the node to remove)
        for i in range(n+1):
            lead_ptr = lead_ptr.next
        #find the end, moving the remove pointer
        while lead_ptr:
            lead_ptr = lead_ptr.next
            remove_ptr = remove_ptr.next
        
        remove_ptr.next = remove_ptr.next.next

        return dummy.next

        


if __name__ == "__main__":
    # print_linked_list(Solution().removeNthFromEnd(build_linked_list([1,2,3,4,5]), 2))
    # print_linked_list(Solution().removeNthFromEnd(build_linked_list([1]), 1))
    print_linked_list(Solution().removeNthFromEnd(build_linked_list([1,2]), 2))