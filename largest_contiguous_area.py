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


#########################

def largest_connected_component(nrows, ncols, grid):
    """Find largest connected component of 1s on a grid."""

    def traverse_component(i, j):

        """Returns no. of unseen elements connected to (i,j)."""

        seen[i][j] = True

        result = 1

        # Check all four neighbours

        if i > 0 and grid[i - 1][j] and not seen[i - 1][j]:
            result += traverse_component(i - 1, j)

        if j > 0 and grid[i][j - 1] and not seen[i][j - 1]:
            result += traverse_component(i, j - 1)

        if i < len(grid) - 1 and grid[i + 1][j] and not seen[i + 1][j]:
            result += traverse_component(i + 1, j)

        if j < len(grid[0]) - 1 and grid[i][j + 1] and not seen[i][j + 1]:
            result += traverse_component(i, j + 1)

        return result

    seen = [[False] * ncols for _ in range(nrows)]

    # Tracks size of largest connected component found

    component_size = 0

    for i in range(nrows):

        for j in range(ncols):

            if grid[i][j] and not seen[i][j]:

                temp = traverse_component(i, j)

                if temp > component_size:
                    component_size = temp

    return component_size


#########################

def maxAreaOfIsland(grid):
    seen = set()
    ans = 0
    for r0, row in enumerate(grid):
        for c0, val in enumerate(row):
            if (val and (r0, c0) not in seen):
                shape = 0
                stack = [(r0, c0)]
                seen.add((r0, c0))
                while stack:
                    r, c = stack.pop()
                    shape += 1
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if (0 <= nr < len(grid)
                                and 0 <= nc < len(grid[0])
                                and grid[nr][nc]
                                and (nr, nc)
                                not in seen):
                            stack.append((nr, nc))
                            seen.add((nr, nc))
                ans = max(ans, shape)
    return ans


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

grid3 = [
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]

print(getBiggestRegion(grid3))
