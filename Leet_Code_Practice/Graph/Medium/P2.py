# #You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.


class Solution:
    def coordinates(self, iteration, coordinate):

        x, y = coordinate

        match iteration:

            case 1:
                return x - 1, y
            case 2:
                return x + 1, y
            case 3:
                return x, y + 1
            case 4:
                return x, y - 1

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        maxarea = 0

        for i in range(0, len(grid)):

            for j in range(0, len(grid[i])):

                if grid[i][j] == 1:

                    area = self.dfs(grid, (i, j))

                    if maxarea < area:
                        maxarea = area

        return maxarea

    def dfs(self, grid, start):

        x, y = start

        grid[x][y] = 0

        area = 1

        for i in range(1, 5):

            x1, y1 = self.coordinates(i, start)

            if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[x1]):

                if grid[x1][y1] == 1:
                    area += self.dfs(grid, (x1, y1))

        return area

# this is BigO(R*C) both in space and time where R is rows and C are columns


