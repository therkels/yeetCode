from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_p, close_p, n, val, res):
            if open_p == close_p and close_p+open_p == 2*n:
                res.append(val)
                return
            if open_p < n:
                dfs(open_p+1, close_p, n, val+'(', res)
            if close_p < open_p:
                dfs(open_p, close_p+1, n, val+')', res)

        dfs(0, 0, n, '', res)
        return res


if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))
