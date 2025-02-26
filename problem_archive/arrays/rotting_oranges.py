class Solution:
  def orangesRotting(self, grid: list[list[int]]) -> int:        
    time = 0
    fresh_count = 0
    queue = []
    subqueue = []
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == 2:
          queue.append((row,col))
        if grid[row][col] == 1:
          fresh_count += 1

    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    r_len = len(grid)
    c_len = len(grid[0])
    while queue:
      r, c = queue.pop(0)
      for d in dirs:
        if 0 <= r+d[0] < r_len and 0 <= c+d[1] < c_len and grid[r+d[0]][c+d[1]] == 1:
          fresh_count -= 1
          grid[r+d[0]][c+d[1]] = 2
          subqueue.append((r+d[0], c+d[1]))
    
      if not queue and subqueue:
        time += 1
        queue.extend(list(subqueue))
        subqueue = []
      
    if fresh_count > 0:
      return -1

    return time

if __name__ == "__main__":
    S = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(S.orangesRotting(grid))