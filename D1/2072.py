
i=1

t = int(input())

while i <= t:
    sum = 0
    li = list(map(int,input().split()))
    for x in li:
        if x % 2 == 1:
            sum = x + sum
        else:
            continue

    print(f'#{i} {sum}')
    i = i + 1
    li.clear()

