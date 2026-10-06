def fibonacci(a,seuil):
    if a >= seuil:
        return a
    else :
        return fibonacci(a+(a-1),seuil)

print(fibonacci(1,9))