import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        factors = []
        factors_large = []
        while i < round(math.sqrt(12)) + 1:
            if n % i == 0:
                factors.append(i)
                factors_large.insert(0, n//i)
            i += 1
        factors.extend(factors_large)
        return factors[k-1] if k-1 < len(factors) else -1

if __name__ == "__main__":
    S = Solution()
    
    print(S.kthFactor(12, 3))
    print(S.kthFactor(7, 2))
    print(S.kthFactor(4, 4))
    print(S.kthFactor(1, 1))
    print(S.kthFactor(1000, 3))
