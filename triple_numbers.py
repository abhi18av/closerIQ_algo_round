# TODO add exception and error handling
# TODO add documentation


def triple_numbers_recursive(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 2
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return triple_numbers_recursive(n - 1) + triple_numbers_recursive(n - 2) + triple_numbers_recursive(n - 3)


print(triple_numbers_recursive(10))

triple_numbers_memo = [2, 2, 3]


def triple_numbers_iterative(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(triple_numbers_memo):
        return triple_numbers_memo[n - 1]
    else:
        temp_fib = triple_numbers_iterative(n - 1) + triple_numbers_iterative(n - 2) + triple_numbers_iterative(n - 3)
        triple_numbers_memo.append(temp_fib)
        return temp_fib


print(triple_numbers_iterative(10))
