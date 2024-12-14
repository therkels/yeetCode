class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        count = 0
        for key,value in counter.items():
            if k == 0:
                if value > 1:
                    count += 1
            if k > 0 and key+k in counter:
                count += 1
        return count

if __name__ == "__main__":
  S = Solution()
  nums = [3,1,4,1,5]
  k = 2
  S.findPairs(nums,k)