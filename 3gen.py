def eve(N):
    for i in range(N):
        if((i % 3 == 0) and (i % 4 == 0)):
            yield i

N = int(input())
event = eve(N)
for i in event:
    print(i)