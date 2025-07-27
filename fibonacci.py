# def fibonacci(n):
#     """Compute the nth Fibonacci number using recursion."""
#     if n < 0:
#         return "Fibonacci sequence is not defined for negative numbers."
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# Input and validation
# try:
#     user_input = int(input("Enter a non-negative integer: "))
#     result = fibonacci(user_input)
#     print(f"The {user_input}th Fibonacci number is: {result}")
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")

number = int(input("Enter a number: "))

# a, b = 0, 1

# print(f"{a} {b}", end=' ')
# for i in range(number-2):
#     c = a + b
#     print(c, end=" ")
#     a,b = b,c


def fib_iterative(number):
    a,b = 0,1
    for i in range(1,number+1):
        print(f'{i:02} => {a:02}', end=',\n')
        a,b = b , a+b
fib_iterative(number)


