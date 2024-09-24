a = []
b = []

count = 1

for i in range(0,3):
    b = []
    for j in range(0,3):
        b.append(count)
        count += 1
    a.append(b)


for i in range(0,3):
    for j in range(0,3):
        print(a[i][j], end = " ")
    print("\n")