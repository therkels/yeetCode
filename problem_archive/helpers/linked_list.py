from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_list = ListNode()
        merge_head = merge_list
        while list1 or list2:
            itms = []
            if list1:
                itms.append(list1.val)
                list1 = list1.next
            if list2:
                itms.append(list2.val)
                list2 = list2.next
            itms.sort()
            for itm in itms:
                merge_list.val = itm
                merge_list.next = ListNode()
                follow_node = merge_list
                merge_list = merge_list.next
        return merge_head


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
