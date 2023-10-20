import math
n = int(input())
length = int(input())
area = (n * length ** 2) / (4 * math.tan(math.pi / n))
print(int(area))