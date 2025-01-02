from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        num_removed = 0
        idx = 0
        for i in range(len(nums)):
            if nums[i] in seen:
                num_removed += 1
            else:
                seen.add(nums[i])
            if num_removed+i < len(nums):
                nums[i] = nums[i+num_removed]
            else:
                break

        nums = nums[0:i-num_removed+1]

        return len(nums)


if __name__ == "__main__":
    S = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(S.removeDuplicates(nums))
