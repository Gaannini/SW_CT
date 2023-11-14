import math
N = int(input())

li = list(map(int , input().split()))

li.sort()
print(f'{li[math.floor(N/2)]}')