T = int(input())

for test_case in range(1, T + 1):
    sum = 0
    li = list(map(int , input().split()))
    for x in li:
        sum = x + sum
    avg = round(sum/10)

    print(f'#{test_case} {avg}')
    li.clear()
