def sqrtee(N):
    for i in range(N):
        yield i**2

N = int(input())
sqrt1 = sqrtee(N)
for i in sqrt1:
    print(i)