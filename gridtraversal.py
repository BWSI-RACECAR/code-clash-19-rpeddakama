"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #19 - Grid Traversal (gridtraversal.py)


Author: Wonjun Lee

Difficulty Level: 8/10

Prompt: Bill’s RACECAR is designed so that it can move either DOWN or RIGHT in a given m x n grid. 
The RACECAR begins at the top-left corner (grid[0][0]) and is trying to reach the bottom-right corner 
(grid[m-1][n-1]). Please write a function that returns the number of unique paths that Bill’s 
RACECAR can take to reach its destination.

Constraints: 1 <= m,n <= 100 ; the output will be less than 2 * 10^9

Test Cases:
Input: m=2; n=2; Output = 2
Input: m=3; n=2; Output = 3
Input: m=3; n=7; Output = 28

"""


class Solution:
    def uniquePaths(self, m, n):
        # type m: int
        # type n: int
        # return: int

        visited = [[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            visited[i][0] = 1
        for j in range(n):
            visited[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                visited[i][j] = visited[i - 1][j] + visited[i][j - 1]

        return visited[m - 1][n - 1]


def main():
    num1 = int(input())
    num2 = int(input())

    tc1 = Solution()
    ans = tc1.uniquePaths(num1, num2)
    print(ans)


if __name__ == "__main__":
    main()
