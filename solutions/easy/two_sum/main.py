class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_idx_map = dict()
        for idx, num in enumerate(nums):
            num_to_find = target - num
            if num_to_find in num_idx_map:
                return [idx, num_idx_map[num_to_find]]
            else:
                num_idx_map[num] = idx
