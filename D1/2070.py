T = int(input())

for test_case in range(1, T + 1):
    num = 0
    li = list(map(int , input().split()))

    for a in li:
        if(num<a):
            num = a
        else:
            continue

    print(f'#{test_case} {num}')