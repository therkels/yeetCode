class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10,
                     "L": 50, "C": 100, "D": 500, "M": 1000}
        res_num = 0
        for i in range(0, len(s)-1):
            if roman_map[s[i+1]] > roman_map[s[i]]:
                print(f"i:{roman_map[s[i+1]]} i+1:{roman_map[s[i]]}")
                res_num -= roman_map[s[i]]
            else:
                res_num += roman_map[s[i]]

        return res_num + roman_map[s[len(s)-1]]


if __name__ == "__main__":
    S = Solution()
    s = "MCMXCIV"
    print(S.romanToInt(s))
