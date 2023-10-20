def sqrtee(a,b):
    for i in range(a,b):
        yield i**2

a = int(input())
b = int(input())
sqrt1 = sqrtee(a,b)
for i in sqrt1:
    print(i)