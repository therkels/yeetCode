class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
      def does_path_exist(obstacleGrid,m,n):
        if m > 

        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        path_history = [[0]*m for i in range(n)]
        for row in range(n):
            for col in range(m):
                if (row == 0 or col == 0):
                  path_history[row][col] = 1
                else:
                  path_history[row][col] = path_history[row-1][col] + path_history[row][col-1]

                if obstacleGrid[row][col] == 1:
                  path_history[row][col] = 0

        
        return path_history[row][col]

if __name__ == "__main__":
  S = Solution()
  obstacleGrid = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
  print(S.uniquePathsWithObstacles(obstacleGrid))