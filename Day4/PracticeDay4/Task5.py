def fibonacci_series(terms):
    first = 0
    second = 1

    for _ in range(terms):
        print(first, end=" ")
        first, second = second, first + second

count = int(input("Enter number of terms: "))
fibonacci_series(count)