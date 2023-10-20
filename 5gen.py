def tozero(N):
    while N>=0:
        yield N
        N-=1

N = int(input())
tozere = tozero(N)
for i in tozere:
    print(i)