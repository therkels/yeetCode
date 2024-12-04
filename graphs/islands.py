class Solution:
  def numIslands(self, grid: list[list[str]]) -> int:
    def dfs(row, col, grid, visited):
      if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return
      if visited[row][col]:
        return
      if grid[row][col] == "0" or grid[row][col] == "0":
        return
      
      visited[row][col] = True
      dfs(row+1,col,grid,visited)
      dfs(row-1,col,grid,visited)
      dfs(row,col+1,grid,visited)
      dfs(row,col-1,grid,visited)

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    islands = 0
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == "1" and not visited[row][col]:
          islands +=1
          dfs(row,col, grid, visited)

    return islands
      

if __name__ == "__main__":
  S = Solution()
  grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","1"]
  ]
      
  print(S.numIslands(grid))
