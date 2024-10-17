class Solution:
  def longestOnes(self, nums: list[int], k: int) -> int:
    left, right = 0, 0
    max_len = 0
    zero_count = 0
    for right in range(len(nums)):
      if nums[right] == 0:
        zero_count += 1
        if zero_count > k:
          while nums[left] != 0 and left < right:
            left += 1
          left += 1
          zero_count -= 1
      max_len = max(max_len, right-left+1)
    return max_len
if __name__ == "__main__":
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3

    S = Solution()
    print(S.longestOnes(nums,k))

  
    