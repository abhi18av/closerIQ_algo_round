def triple_numbers_iterative(n):
    """
   Computes the triple number series using iteration.

   This solution, relies on iteratively computing the results of all values, storing the result in a table and
   simply returning the very last item in the table, which is the value for the target number.

   Parameters:
   n (int): The Nth term of the triple_number series

   Returns:
   int: Returns the value at Nth position in the triple_number series
   """

    triple_numbers_table = [2, 2, 3]

    if n <= 0:
        print("Invalid input: Please enter a positive integer.")
        return None
    elif n == 1:
        return triple_numbers_table[0]
    elif n == 2:
        return triple_numbers_table[1]
    elif n == 3:
        return triple_numbers_table[2]

    for i in range(3, n):
        tmp = triple_numbers_table[i - 1] \
              + triple_numbers_table[i - 2] \
              + triple_numbers_table[i - 3]
        triple_numbers_table.append(tmp)

    return triple_numbers_table[n - 1]


#################


def triple_numbers_memoized(n):
    """
    Computes the triple number series using memoization.

    This solution, relies on the technique of memoization which caches the results of previous
    computations and calls the function only if it is invoked with a new argument else returns the
    previously cached value.

    Parameters:
    n (int): The Nth term of the triple_number series

    Returns:
    int: Returns the value at Nth position in the triple_number series
    """

    triple_numbers_memo = [2, 2, 3]

    if n <= 0:
        print("Invalid input: Please enter a positive integer.")
    elif n <= len(triple_numbers_memo):
        return triple_numbers_memo[n - 1]
    else:
        tmp = triple_numbers_memoized(n - 1) \
              + triple_numbers_memoized(n - 2) \
              + triple_numbers_memoized(n - 3)
        triple_numbers_memo.append(tmp)
        return tmp


def triple_numbers_recursive(n):
    """
    Computes the triple number series recursively.

    This solution, relies on the technique of recursion which computes function for every argument.
    It's definition corresponds to the mathematical function description.

    Parameters:
    n (int): The Nth term of the triple_number series

    Returns:
    int: Returns the value at Nth position in the triple_number series
    """

    if n <= 0:
        print("Invalid input: Please enter a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return triple_numbers_recursive(n - 1) \
               + triple_numbers_recursive(n - 2) \
               + triple_numbers_recursive(n - 3)


# # ======================
# # Test cases
# # ======================
#
print(triple_numbers_iterative(0))
print(triple_numbers_iterative(1))
print(triple_numbers_iterative(2))
print(triple_numbers_iterative(3))
print(triple_numbers_iterative(4))
print(triple_numbers_iterative(10))
print(triple_numbers_iterative(20))

print(triple_numbers_memoized(0))
print(triple_numbers_memoized(1))
print(triple_numbers_memoized(2))
print(triple_numbers_memoized(3))
print(triple_numbers_memoized(4))
print(triple_numbers_memoized(10))
print(triple_numbers_memoized(20))

print(triple_numbers_recursive(0))
print(triple_numbers_recursive(1))
print(triple_numbers_recursive(2))
print(triple_numbers_recursive(3))
print(triple_numbers_recursive(4))
print(triple_numbers_recursive(10))
print(triple_numbers_recursive(20))
