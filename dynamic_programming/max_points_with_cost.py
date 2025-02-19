from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])

        d = points[0]

        for i in range(1, rows):
            left_max = [0] * cols
            right_max = [0] * cols
            new_d = points[i].copy()

            left_max[0] = d[0]
            for j in range(1, cols):
                left_max[j] = max(d[j], left_max[j-1] - 1)

            right_max[cols-1] = d[cols-1]
            for j in range(cols - 2, -1, -1):
                right_max[j] = max(d[j], right_max[j+1] - 1)

            print(f"row {i}:")
            for j in range(cols):
                print(f"column {j}: left={left_max[j]} right={right_max[j]}")
                new_d[j] += max(left_max[j], right_max[j])

            d = new_d
        return max(d)


if __name__ == "__main__":
    S = Solution()
    points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    print(S.maxPoints(points))
