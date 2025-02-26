class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_path_len = 0
        curr_tab_len = 0
        stack = []
        for line in input.split("\n"):
            line_stripped = line.lstrip("\t")
            t_len = len(line) - len(line_stripped)
            while t_len < len(stack):
                stack.pop(-1)
            if len(stack) == 0:
                stack.append(len(line_stripped))
            elif t_len >= len(stack):
                stack.append(stack[t_len-1]+len(line_stripped)+1)
            if "." in line_stripped:
                max_path_len = max(max_path_len, stack[t_len])
        return max_path_len


if __name__ == "__main__":
    S = Solution()
    s2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    s = "file1.txt\nfile2.txt\nlongfile.txt"
    print(S.lengthLongestPath(s2))
