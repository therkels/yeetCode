class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i+1,len(nums)):
                    if nums[j] == 0:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
        

if __name__ == "__main__":
  