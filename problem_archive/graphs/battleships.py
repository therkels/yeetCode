from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])

        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols and board[row][col] != "."

        def dfs(row, col):
            if visited[row][col]:
                return

            visited[row][col] = True

            positions = [(row+1, col), (row-1, col),
                         (row, col+1), (row, col-1)]

            for pos_x, pos_y in positions:
                if is_valid(pos_x, pos_y):
                    dfs(pos_x, pos_y)

        visited = [[False] * cols for _ in range(rows)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                x = visited[i][j]
                y = board[i][j]
                if board[i][j] == ".":
                    visited[i][j] = True
                elif not visited[i][j] and board[i][j] == "X":
                    count += 1
                    dfs(i, j)

        return count


if __name__ == "__main__":
    S = Solution()
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]

    print(S.countBattleships(board))
