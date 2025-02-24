from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize so they are furthest apart
        buy = prices[0]
        profit = 0
        for price in prices:
            if price < buy:
                buy = price
            profit = max(profit, price-buy)

        return profit


if __name__ == "__main__":
    S = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(S.maxProfit(prices))
