# PAIR: MELISSA LOKOROMA $ CLAIRE NAMAGALA

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     elif n < 0:
#         raise ValueError("Factorial is not defined for negative numbers")
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
