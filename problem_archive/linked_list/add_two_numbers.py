# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        new_list = ListNode()
        head = new_list
        while l1 or l2 or carry:
            num_sum = carry
            if l1:
                num_sum += l1.val
                l1 = l1.next
            if l2:
                num_sum += l2.val
                l2 = l2.next
            carry = num_sum // 10
            num_sum = num_sum % 10
            new_list.val = num_sum
            if l1 or l2 or carry:
                new_list.next = ListNode(carry)
            new_list = new_list.next
        
        return head


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    S = Solution()
    list1 = create_linked_list([2, 4, 3])
    list2 = create_linked_list([5, 6, 4])
    merged_list = S.addTwoNumbers(list1, list2)
    print_linked_list(merged_list)