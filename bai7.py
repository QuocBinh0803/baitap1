def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
result = factorial(5)
print(f"Giai thừa của 5 là: {result}")