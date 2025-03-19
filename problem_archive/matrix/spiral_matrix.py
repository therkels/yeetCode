from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_seq = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= bottom:
            #Left->Right
            for j in range(left, right+1):
                spiral_seq.append(matrix[top][j])
            top += 1
            #Top->Bottom
            for i in range(top, bottom + 1):
                spiral_seq.append(matrix[i][right])
            right -= 1
            #Right->Left
            if top <= bottom:
                for j in range(right, left -1, -1):
                    spiral_seq.append(matrix[bottom][j])
                bottom-= 1
            #Bottom->Top
            if left <= right:
                for i in range(bottom, top -1, -1):
                    spiral_seq.append(matrix[i][left])
                left += 1
        
        return spiral_seq
                    



if __name__ == "__main__":
    S = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(S.spiralOrder(matrix))
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] 
    print(S.spiralOrder(matrix))
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(S.spiralOrder(matrix))