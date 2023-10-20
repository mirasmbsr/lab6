def eve(N):
    for i in range(N):
        if(i % 2 == 0):
            yield i

N = int(input())
event = eve(N)
for i in event:
    print(i)