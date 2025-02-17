class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruit = 0
        first_basket = 0
        fruits = {fruits[0], fruits[1]}
        for next_basket in range(2, len(fruits)):
            curr_fruit = fruits(next_basket)


if __name__ == "__main__":
    fruits = [1, 2, 3, 2, 2]

    S = Solution()
    print(S.totalFruit(fruits))
