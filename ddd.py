def fibonacci_generator(limit):
    """Yields Fibonacci numbers up to a specified limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# The generator object is created, but no numbers are computed yet
fib_seq = fibonacci_generator(1000)

# The values are computed one by one as the loop requests them
print("Fibonacci sequence up to 1000:")
for num in fib_seq:
    print(num, end=" ")
print()