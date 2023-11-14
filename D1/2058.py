import math
N = int(input())


a = math.floor(N/1000)
b = math.floor((N-a*1000)/100)
c = math.floor((N-a*1000-b*100)/10)
d = math.floor(N-a*1000-b*100-c*10)

print(f'{a+b+c+d}')