from helpers.linked_list import ListNode, print_linked_list, create_linked_list

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

if __name__ == "__main__":
    S = Solution()
    head = create_linked_list([1, 2, 3, 4])
    swapped = S.swapPairs(head)
    print_linked_list(swapped)