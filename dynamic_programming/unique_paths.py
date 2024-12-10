class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_history = [[0]*n for i in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    path_history[row][col] = 1
                    continue
                path_history[row][col] = path_history[row-1][col] + path_history[row][col-1]

        return path_history[row][col]

if __name__ == "__main__":
  S = Solution()
  m = 3 
  n = 7
  print(S.uniquePaths(m, n))