class Solution:
  def letterCombinations(self, digits: str) -> list[str]:
    keyboard = {
      2: "abc",
      3: "def",
      4: "ghi",
      5: "jkl",
      6: "mno",
      7: "pqrs",
      8: "tuv",
      9: "wxyz"
    }
    res = []
    def helper(idx, combo):
      if idx == len(digits):
        res.append(combo)
        return
      for char in keyboard[digits[idx]]:
        helper(idx+1, combo+char)
    
    helper(0,"")
    return res

      

if __name__ == "__main__":
  S = Solution()
  input_nums = []
  print(S.letterCombinations(input_nums))
