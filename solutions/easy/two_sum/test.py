import unittest
from parameterized import parameterized
if __name__ == "__main__":
    from main import Solution
else:
    from solutions.easy.two_sum.main import Solution


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    @parameterized.expand(test_cases)
    def test_case(self, nums, target, expected):
        self.assertEqual(sorted(self.solution.twoSum(nums, target)), expected)

    @staticmethod
    def run_tests():
        test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(
            TestCases)
        unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    TestCases.run_tests()
