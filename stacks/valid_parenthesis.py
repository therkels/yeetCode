class Solution:
    def isValid(self, s: str) -> bool:
        open_parens = []
        paren_map = {")":"(","}":"{","]":"["}
        for char in s:
            if char in ["(", "{", "["]:
                open_parens.append(char)
            elif char in [")", "}", "]"]:
                if len(open_parens) == 0:
                    return False
                if paren_map[char] == open_parens[-1]:
                    open_parens.pop(-1)
                else:
                    return False

        return len(open_parens) == 0

if __name__ == "__main__":
  S = Solution()
  s = "()[]{}"
  print(S.isValid(s))