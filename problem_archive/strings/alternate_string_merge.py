import unittest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_word_len = min(len(word1), len(word2))
        ret_str = ""
        for i in range(min(len(word1), len(word2))):
            ret_str += word1[i]
            ret_str += word2[i]

        if len(word1) > len(word2):
            ret_str += word1[min_word_len:]
        else:
            ret_str += word2[min_word_len:]

        return ret_str


class TestSolution(unittest.TestCase):
    def setUp(self):
        self._s = Solution()

    def test_basic(self):
        word1 = "abcd"
        word2 = "pq"
        self.assertEqual(self._s.mergeAlternately(word1,word2), 'apbqcd')


if __name__ == "__main__":
    unittest.main()