def fibonacci(a):
    if a <= 1:
        return a
    else :
        return fibonacci(a-1) + fibonacci(a-2)

for i in range(10):
    print(fibonacci(i))