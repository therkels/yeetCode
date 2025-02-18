class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        Take a string repr of a key and reformat using k segments.
        Args:
          s (str): the string
          k (int): the segment size

        Returns:
          str: A formatted string with k segments seperated by "-"
        """
        new_str = []
        k_local = 0
        # reverse the string so we are grouping with end-string priority
        for letter in reversed(s):
            if letter == "-":
                continue
            # keep track of k size
            if k_local < k:
                k_local += 1
            else:
                k_local = 1
                new_str.append("-")
            new_str.append(letter)
        # edge case: consider even groupings
        if new_str[0] == "-":
            new_str.pop(0)

        return "".join(new_str[::-1]).upper()


if __name__ == "__main__":
    S = Solution()
    s = "2-5g-3-J"
    k = 2
    print(S.licenseKeyFormatting(s, k))
