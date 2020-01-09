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

