class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    num_idx_map = dict()
    for idx, num in enumerate(nums):
      num_to_find = target - num
      if num_to_find in num_idx_map:
        return [idx, num_idx_map[num_to_find]]
      else:
        num_idx_map[num] = idx
        

if __name__ == "__main__":
  S = Solution()
  nums = [3,2,4]
  target = 6
  print(S.twoSum(nums, target))