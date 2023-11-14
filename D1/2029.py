import math

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print(f"#{test_case}",math.floor(a/b), a%b)