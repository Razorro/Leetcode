"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory.
Furthermore, a double period .. moves the directory up a level. For more information,
see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /,
and there must be only a single slash / between two directory names.
The last directory name (if it exists) must not end with a trailing /.
Also, the canonical path must be the shortest string representing the absolute path.



Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: "/a/./b/../../c/"
Output: "/c"
Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"

Runtime: 52 ms, faster than 40.79% of Python3 online submissions for Simplify Path.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Simplify Path.


The same idea, without other tricks.
"""


class Solution:
    def simplifyPath(self, path: 'str') -> 'str':
        pathArr = []
        i = 0
        while i < len(path):
            if path[i] == '/':
                i += 1
                collector = []
                while i < len(path) and path[i] != '/':
                    collector.append(path[i])
                    i += 1

                if len(collector):
                    dirPath = ''.join(collector)
                    if dirPath == '..':
                        if len(pathArr):
                            pathArr.pop()
                    elif dirPath == '.':
                        pass
                    else:
                        pathArr.append(dirPath)
        dirPath = '/'.join(pathArr)
        return '/' + dirPath


if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/home//foo/"))


