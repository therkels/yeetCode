# Definition for singly-linked list.
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for ele in arr:
        current.next = ListNode(ele)
        current = current.next
    return dummy.next
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        ret_l = ListNode()
        pointer = ret_l
        overflow = 0
        while l1 is not None or l2 is not None:
            #set LL sums to 0
            l1_val, l2_val = 0, 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            new_val = l1_val + l2_val

            pointer.val += overflow + new_val
            
            if new_val >=10:
                pointer.val -= 10
                overflow = 1
            else:
                overflow = 0
            if (l1 or l2):
                pointer.next = ListNode()
                pointer = pointer.next
        if overflow:
            pointer.val += overflow
        
        return ret_l


if __name__ == "__main__":
    l_1 = [2,4,3]
    l_2 = [5,6,4]
    l1 = create_linked_list(l_1)
    l2 = create_linked_list(l_2)

    S = Solution()
    print(print_linked_list(S.addTwoNumbers(l1,l2)))

  
    