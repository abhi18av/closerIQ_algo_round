# def getBiggestRegion(grid):
#     longest_length = 0
#     for row in range(0, len(grid)):
#         for column in range(0, len(grid[0])):
#             length = exploreRegion(grid, row, column)
#             longest_length = max(length, longest_length)
#     return longest_length
#
#
# def exploreRegion(grid, row, col):
#     total = 1
#     if grid[row][col] == 0:
#         return 0
#     grid[row][col] = 0
#     if row - 1 >= 0 and col - 1 >= 0:
#         total += exploreRegion(grid, row - 1, col - 1)
#     if row - 1 >= 0:
#         total += exploreRegion(grid, row - 1, col)
#     if col - 1 >= 0:
#         total += exploreRegion(grid, row, col - 1)
#     if row + 1 < len(grid) and col + 1 < len(grid[0]):
#         total += exploreRegion(grid, row + 1, col + 1)
#     if row + 1 < len(grid):
#         total += exploreRegion(grid, row + 1, col)
#     if col + 1 < len(grid[0]):
#         total += exploreRegion(grid, row, col + 1)
#     if col + 1 < len(grid[0]) and row - 1 >= 0:
#         total += exploreRegion(grid, row - 1, col + 1)
#     if row + 1 < len(grid) and col - 1 >= 0:
#         total += exploreRegion(grid, row + 1, col - 1)
#     return total
#
#
# grid1 = [
#     [0, 1, 1, 1],
#     [0, 0, 1, 0],
#     [0, 0, 1, 0],
#     [1, 0, 0, 0],
#     [1, 1, 0, 0]
# ]
#
#
# print(getBiggestRegion(grid1))
#
# grid2 = [[0, 0, 1, 1, 1, 1],
#          [1, 0, 0, 0, 0, 1],
#          [1, 0, 0, 0, 0, 1],
#          [1, 0, 0, 0, 0, 0],
#          [1, 0, 1, 0, 0, 0],
#          [1, 1, 0, 1, 0, 0],
#          [1, 1, 1, 1, 0, 1]]
#
# print(getBiggestRegion(grid2))


###############

def getBiggestRegion(grid):
    maxRegion = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            maxRegion = max(maxRegion, countCells(grid, i, j))
    return maxRegion


def countCells(grid, i, j):
    rows = len(grid)
    columns = len(grid[0])

# i is r
# j is c
    if (not (i in range(rows) and j in range(columns))):
        return 0

    if (grid[i][j] == 0):
        return 0

    count = 1
    grid[i][j] = 0
    count += countCells(grid, i + 1, j)
    count += countCells(grid, i - 1, j)
    count += countCells(grid, i, j + 1)
    count += countCells(grid, i, j - 1)
    # count += countCells(grid, i + 1, j + 1)
    # count += countCells(grid, i - 1, j - 1)
    # count += countCells(grid, i - 1, j + 1)
    # count += countCells(grid, i + 1, j - 1)
    return count


grid1 = [
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]

## Should give 5
print(getBiggestRegion(grid1))

grid2 = [[0, 0, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0],
         [1, 1, 0, 1, 0, 0],
         [1, 1, 1, 1, 0, 1]]

## Should give 11
print(getBiggestRegion(grid2))

# #########
#
# def dfs(grid, i, j):
#     n, m = len(grid), len(grid[0])
#     positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
#                  (0, 1), (1, -1), (1, 0), (1, 1)]
#     grid[i][j] = 0
#     count = 1
#
#     for pos in positions:
#         if i + pos[0] in range(n) and j + pos[1] in range(m):
#             if grid[i + pos[0]][j + pos[1]] == 1:
#                 count += dfs(grid, i + pos[0], j + pos[1])
#
#     return count
#
#
# def getBiggestRegion(grid):
#     n, m = len(grid), len(grid[0])
#     max_region_size = 0
#
#     for i in range(n):
#         for j in range(m):
#             if grid[i][j] == 1:
#                 max_region_size = max(max_region_size, dfs(grid, i, j))
#
#     return max_region_size
