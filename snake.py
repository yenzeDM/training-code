lines, columns = map(int, input().split())
li = [[0] * columns for _ in range(lines)]
count = 0

for i in range(lines):
    for j in range(columns):
        li[i][j] = count
        count += 1
    if i % 2 != 0:
        li[i] = li[i][::-1]


for i in range(lines):
    for j in range(columns):
        if li[i][j] < 10:
            print(li[i][j], end='  ')
        else:
            print(li[i][j], end=' ')
    print()