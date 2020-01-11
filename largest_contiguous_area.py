def getBiggestRegion(grid):
    """
    This function is the main public API to compute the biggest region sum.

    This solution, relies on the technique of dynamic programming to reduce the problem into
    sub-problems and relies on the helper function `countCells` to make the best decision for that sub-problem.

    Parameters:
    grid (a 2-d array): This is the main input grid in which we need to compute the maximum region

    Returns:
    int: Returns the number of all valid contiguous cells in the grid
    """
    maxRegion = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            maxRegion = max(maxRegion, countCells(grid, i, j))
    return maxRegion


def countCells(grid, r, c):
    """
    This function analyzes the current value and invokes itself again on the neighbouring valid values.

    Diagonals and any point outside the grid is considered as invalid.

    Parameters:
    grid (a 2-d array): This is the main input grid in which we need to compute the maximum regions
    r (int): The current row
    c (int): The current column

    Returns:
    int: Returns the value count depending upon whether the current cell in the grid is valid or not
    """

    rows = len(grid)
    columns = len(grid[0])

    if (not (r in range(rows) and c in range(columns))):
        return 0

    if (grid[r][c] == 0):
        return 0

    count = 1
    grid[r][c] = 0
    count += countCells(grid, r + 1, c)
    count += countCells(grid, r - 1, c)
    count += countCells(grid, r, c + 1)
    count += countCells(grid, r, c - 1)
    return count


# ======================
# Test cases
# ======================

grid1 = [
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]

print(getBiggestRegion(grid1))

grid2 = [[0, 0, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0],
         [1, 1, 0, 1, 0, 0],
         [1, 1, 1, 1, 0, 1]]

print(getBiggestRegion(grid2))

