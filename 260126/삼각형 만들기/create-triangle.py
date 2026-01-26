n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort(key = lambda x : (x[0], x[1]))

x = [p[0] for p in points]
y = [p[1] for p in points]

max_extent = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if x[i] != x[j] and y[i] == y[j] and x[j] == x[k] and y[j] != y[k] and x[i] != x[k] and y[i] != y[k]:
                extent = abs(x[k] - x[i]) * abs(y[k] - y[i])
                max_extent = max(max_extent, extent)
            
            elif x[i] == x[j] and y[i] != y[j] and x[j] != x[k] and y[j] == y[k] and x[i] != x[k] and y[i] != y[k]:
                extent = abs(x[k] - x[i]) * abs(y[k] - y[i])
                max_extent = max(max_extent, extent)
            
            elif x[i] != x[k] and y[i] != y[k] and x[j] == x[k] and y[j] != y[k] and x[i] != x[j] and y[i] != y[j]:
                extent = abs(x[j] - x[i]) * abs(y[j] - y[i])
                max_extent = max(max_extent, extent)
            
            elif x[i] != x[j] and y[i] == y[j] and x[j] != x[k] and y[j] != y[k] and x[i] == x[k] and y[i] != y[k]:
                extent = abs(x[j] - x[k]) * abs(y[j] - y[k])
                max_extent = max(max_extent, extent)
            


print(max_extent)
            