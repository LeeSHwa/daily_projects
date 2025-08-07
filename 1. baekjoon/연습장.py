size = int(input())
temp = []
for i in range(size):
    temp.append(list(map(int,input().split())))

temp2 = [row[ : size//2] for row in temp[ : size//2]] # 2사분면
temp3 = [row[size//2 : size] for row in temp[ : size//2]] # 1사분면
temp4 = [row[ : size//2] for row in temp[size//2 : size]] # 3사분면
temp5 = [row[size//2 : size] for row in temp[size//2 : size]] # 4사분면

# print(temp2)

print("temp2")
for i in range(size//2):
    for j in range(size//2):
        print(temp2[i][j], end=" ")
    print()
print()


print("temp3")
for i in range(size//2):
    for j in range(size//2):
        print(temp3[i][j], end=" ")
    print()
print()

print("temp4")
for i in range(size//2):
    for j in range(size//2):
        print(temp4[i][j], end=" ")
    print()
print()

print("temp5")
for i in range(size//2):
    for j in range(size//2):
        print(temp5[i][j], end=" ")
    print()
print()
