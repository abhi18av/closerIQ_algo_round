def get_biggest_region(grid):
    """
    This function is the main public API to compute the biggest region sum.

    This solution, relies on the technique of dynamic programming to reduce the problem into
    sub-problems and relies on the helper function `countCells` to make the best decision for that sub-problem.

    Parameters:
    grid (a 2-d array): This is the main input grid in which we need to compute the maximum region

    Returns:
    int: Returns the number of all valid contiguous cells in the grid
    """
    max_region = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            max_region = max(max_region, count_cells(grid, r, c))
    return max_region


def count_cells(grid, r, c):
    """
    This function analyzes the current value and invokes itself again on the neighbouring valid values.

    Diagonals and any point outside the grid are considered as invalid.

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
    count += count_cells(grid, r + 1, c)
    count += count_cells(grid, r - 1, c)
    count += count_cells(grid, r, c + 1)
    count += count_cells(grid, r, c - 1)
    return count

    #########################


def traverse_component(grid, r, c, seen):
    """
    This function analyzes the current cell and invokes itself again on the neighbouring valid cells.

    Diagonals and any point outside the grid are considered as invalid.

    Parameters:
    r (int): The current row
    c (int): The current column

    Returns:
    int: Returns the value count depending upon whether the current cell in the grid is valid or not
    """

    """Returns no. of unseen elements connected to (r,c)."""

    seen[r][c] = True

    result = 1

    # Check all four neighbours

    if r > 0 and grid[r - 1][c] and not seen[r - 1][c]:
        result += traverse_component(grid, r - 1, c, seen)

    if c > 0 and grid[r][c - 1] and not seen[r][c - 1]:
        result += traverse_component(grid, r, c - 1, seen)

    if r < len(grid) - 1 and grid[r + 1][c] and not seen[r + 1][c]:
        result += traverse_component(grid, r + 1, c, seen)

    if c < len(grid[0]) - 1 and grid[r][c + 1] and not seen[r][c + 1]:
        result += traverse_component(grid, r, c + 1, seen)

    return result


def largest_connected_component(grid):
    """
   This function is the main public API to compute the biggest region sum.

   This solution, relies on the technique of dynamic programming to reduce the problem into
   sub-problems and relies on the helper function `countCells` to make the best decision for that sub-problem.

   Parameters:
   grid (a 2-d array): This is the main input grid in which we need to compute the maximum region

   Returns:
   int: Returns the number of all valid contiguous cells in the grid
   """

    nrows = len(grid)
    ncols = len(grid[0])
    """Find largest connected component of 1s on a grid."""

    seen = [[False] * ncols for _ in range(nrows)]

    # Tracks size of largest connected component found

    component_size = 0

    for r in range(nrows):
        for c in range(ncols):

            if grid[r][c] and not seen[r][c]:
                current_max_size = traverse_component(grid, r, c, seen)

                if current_max_size > component_size:
                    component_size = current_max_size

    return component_size


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

print(largest_connected_component(grid1))
print(get_biggest_region(grid1))

grid2 = [[0, 0, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0],
         [1, 1, 0, 1, 0, 0],
         [1, 1, 1, 1, 0, 1]]

print(largest_connected_component(grid2))
print(get_biggest_region(grid2))

grid3 = [
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]

print(largest_connected_component(grid3))
print(get_biggest_region(grid3))
