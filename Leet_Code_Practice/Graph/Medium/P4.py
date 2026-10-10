# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

class Solution:

    def coordinates(self, start, iteration):

        x, y = start

        match iteration:

            case 1:
                return x + 1, y
            case 2:
                return x - 1, y
            case 3:
                return x, y + 1
            case 4:
                return x, y - 1

    def orangesRotting(self, grid: list[list[int]]) -> int:

        queue = deque()

        for i in range(0, len(grid)):

            for j in range(0, len(grid[i])):

                if grid[i][j] == 2:
                    queue.append((i, j))

        Bool = False

        if not queue:
            Bool = True

        count = -1

        while queue:

            iterations = len(queue)

            count += 1

            while iterations > 0:

                coor = queue.popleft()

                for i in range(1, 5):

                    x, y = self.coordinates(coor, i)

                    if 0 <= x < len(grid) and 0 <= y < len(grid[x]):

                        if grid[x][y] == 1:
                            queue.append((x, y))

                            grid[x][y] = 2

                iterations -= 1

        for i in range(0, len(grid)):

            for j in grid[i]:

                if j == 1:
                    return -1

        if Bool:
            return 0

        return count

# This is BigO(R*C) in Time and Space , where R are rows and C is Columns

#Standard in structure, but one detail differs from the usual version:
# the typical solution counts fresh oranges up front and decrements as
# they rot, then returns -1 if any are left. That replaces your final
# full-grid scan and the Bool flag (the “no rotten oranges” case falls out
# naturally). Same Big-O, just a bit tidier.