T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, T + 1):
    N = input()
    li = list(map(int, [N[i:i + 2] for i in range(0, len(N), 2)]))

    if li[0] == 0 and li[1] == 0:
        print(f'#{test_case} -1')
    elif li[2] > 12 or li[2] == 0:
        print(f'#{test_case} -1')
    elif li[3] > days[li[2] - 1]:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {str(li[0]).zfill(2)}{str(li[1]).zfill(2)}/{str(li[2]).zfill(2)}/{str(li[3]).zfill(2)}')
    li.clear()
