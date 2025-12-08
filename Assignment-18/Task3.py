def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function
print("Factorial =", factorial(5))
print("Factorial =", factorial(0))
