class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res_list = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res_list.add([nums[i], nums[j], nums[k]])
                    j+= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                else: 
                    k -= 1
        return list(res_list)

if __name__ == "__main__":
  S = Solution()

  nums = [-1,0,1,2,-1,-4]
  print(S.threeSum(nums))