class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
      res = []

      def helper(sum_arr,j):
        if len(sum_arr) == k and sum(sum_arr) == n:
          res.append(sum_arr[:])
          return
        if sum(sum_arr) > n or len(sum_arr) == k:
          return
        
        for i in range(j,10):
          if i in sum_arr:
            continue
          sum_arr.append(i)
          helper(sum_arr,i+1)
          sum_arr.pop(-1)
      
      helper([],1)
      return res

if __name__ == "__main__":
  S = Solution()
  print(S.combinationSum3(4,1))
