class Solution:
    def partitionString(self, s: str) -> int:
        unique_sets = list()
        curr_set = set()
        for char in s:
            if char not in curr_set:
                curr_set.add(char)
            else:
                unique_sets.append(curr_set)
                curr_set = set()
                curr_set.add(char)
            print(curr_set)
        print(unique_sets)
        return len(unique_sets)

if __name__ == "__main__":
  S = Solution()
  s = "abacaba"
  S.partitionString(s)
