#You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:
#
# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.


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

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        queue = deque()
        visited = set()

        queue.append((sr, sc))

        visited.add((sr, sc))

        pixal = image[sr][sc]

        while queue:

            x, y = queue.popleft()

            image[x][y] = color

            for i in range(1, 5):

                x1, y1 = self.coordinates(i, (x, y))

                if 0 <= x1 < len(image) and 0 <= y1 < len(image[x1]):

                    if image[x1][y1] == pixal and (x1, y1) not in visited:
                        queue.append((x1, y1))

                        visited.add((x1, y1))

        return image

# this is BigO(R*C) in both space and Time ,where R is rows, and C is coloum