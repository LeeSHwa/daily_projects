from collections import defaultdict

N, M, D, S = map(int, input().split())

timeline1 = defaultdict(list)

timeline2 = [0] * 102

eat_mushroom = defaultdict(set)

for _ in range(D):
    p, m, t = map(int, input().split())
    timeline1[t].append((p, m))
    eat_mushroom[m].add(p)

for _ in range(S):
    p, t = map(int, input().split())
    timeline2[t] = p

candidates = set()

for time in range(1, 101):
    if timeline2[time]: # 만약 아팠다면 그 전의 먹은 사람과 머쉬룸을 조사
        person = timeline2[time] 
        
        for in_time in range(1, time):
            
            if timeline1[in_time]:
                for p, m in timeline1[in_time]:
                    candidates.add(m)
        
        break

max_med = 0
for candidate in candidates:
    max_med = max(max_med, len(eat_mushroom[candidate]))

print(max_med)