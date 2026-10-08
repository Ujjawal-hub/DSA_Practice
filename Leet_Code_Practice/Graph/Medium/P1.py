# #Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#

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

    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()

        count = 0

        for i in range(0, len(grid)):

            for j in range(0, len(grid[i])):

                if (i, j) not in visited and grid[i][j] == "1":
                    self.dfs(grid, (i, j), visited)

                    count += 1

        return count

    def dfs(self, grid, start, visited):

        visited.add(start)

        for i in range(1, 5):

            x1, y1 = self.coordinates(i, start)

            if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[x1]):

                if (x1, y1) not in visited and grid[x1][y1] == "1":
                    self.dfs(grid, (x1, y1), visited)

        return

# this is BigO(R*C) both in space and time where R is rows and C are columns
