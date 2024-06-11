import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in [0,1]:
            return len(s)
        substr_set = set()
        left, right = 0, 0
        max_len = 0
        curr_len = 0
        while right != len(s):
            if s[right] not in substr_set:
                substr_set.add(s[right])
                right += 1
            else:
                substr_set.remove(s[left])
                left += 1
            curr_len = right - left
            max_len = max(max_len, curr_len)
        return max_len
            
class TestSolution(unittest.TestCase):
    def setUp(self):
        self._s = Solution()

    def test_basic(self):
        s = "abcabcbb"
        self.assertEqual(self._s.lengthOfLongestSubstring(s), 3)

    def test_repeated(self):
        s = "bbbbb"
        self.assertEqual(self._s.lengthOfLongestSubstring(s), 1)

    def test_empty_string(self):
        s = ""
        self.assertEqual(self._s.lengthOfLongestSubstring(s), 0)
    
    def test_simple(self):
        s = "pwwkew"
        self.assertEqual(self._s.lengthOfLongestSubstring(s), 3)

    def test_repeated(self):
        s = "dvdf"
        self.assertEqual(self._s.lengthOfLongestSubstring(s), 3)

if __name__ == "__main__":
    unittest.main()