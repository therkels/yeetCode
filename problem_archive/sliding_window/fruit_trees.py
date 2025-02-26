from typing import List


class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        """
        Get the maximum number of fruits that can be pulled from an array of "trees". 
        (problem:https://leetcode.com/problems/fruit-into-baskets/description/)

        Args:
          fruits (List[int]): the array of fruits

        Returns:
          int: the longest continguous length of two fruits
        """
        max_fruit = 0
        basket = {}
        left = 0

        # Sliding window, use right as the leading window (2*O(N))
        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            # basket needs to be emptied (move left window until only two fruits remain)
            while len(basket) > 2:
                move_cnt = basket[fruits[left]]
                basket[fruits[left]] -= 1
                # exit condition
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            # add one since problem is 0 indexed
            max_fruit = max(max_fruit, right - left + 1)

        return max_fruit


if __name__ == "__main__":
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

    S = Solution()
    print(S.totalFruit(fruits))
