triple_numbers_memo = [2, 2, 3]

def triple_numbers_iterative(n):
    """
    Computes the triple number series iteratively, using Dynamic programming technique

    This solution, relies on the technique of memoization which caches the results of previous
    computations and calls the function only if it is invoked with a new argument else returns the
    previously cached value.

    Parameters:
    n (int): The Nth term of the triple_number series

    Returns:
    int: Returns the value at Nth position in the triple_number series
    """
    if n < 0:
        print("Invalid input: Please enter a positive integer.")
    elif n <= len(triple_numbers_memo):
        return triple_numbers_memo[n - 1]
    else:
        temp_fib = triple_numbers_iterative(n - 1) \
                   + triple_numbers_iterative(n - 2) \
                   + triple_numbers_iterative(n - 3)
        triple_numbers_memo.append(temp_fib)
        return temp_fib


def triple_numbers_recursive(n):
    """
    Computes the triple number series recursively.

    This solution, relies on the technique of recursion which computes function for every argument.
    It's definition corresponds to the mathematical function description

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


# ======================
# Test cases
# ======================


print(triple_numbers_iterative(10))
print(triple_numbers_iterative(20))

print(triple_numbers_recursive(10))
print(triple_numbers_recursive(20))
