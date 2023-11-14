alp = input()

li = [alp[i:i + 1] for i in range(0, len(alp), 1)]

for x in li:
    x = x.upper()
    print(x, end='')