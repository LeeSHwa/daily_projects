from collections import defaultdict

n = int(input())
googoo = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())

    googoo[a].append(b)

ans = 0
for _, pos in googoo.items():
    
    last_pos = pos[0]
    curr_cnt = 0
    for i in pos:
        if i != last_pos:
            curr_cnt += 1
        last_pos = i
    
    ans += curr_cnt

print(ans)
