class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
      left = 0
      for right in range(len(nums)):
        if nums[right] != 0:
          nums[left] = nums[right]
          nums[right]=0
          left += 1

if __name__ == "__main__":
  S = Solution()
  a = [1,0,0]
  S.moveZeroes(a)
  print(a)