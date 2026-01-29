from collections import defaultdict

N, M, D, S = map(int, input().split())

timeline1 = defaultdict(list)

timeline2 = [0] * 102

eat_mushroom = defaultdict(set)
who_eat = defaultdict(set)

for _ in range(D):
    p, m, t = map(int, input().split())
    timeline1[t].append((p, m))
    eat_mushroom[m].add(p)
    who_eat[p].add(m)

for _ in range(S):
    p, t = map(int, input().split())
    timeline2[t] = p

candidates = set([i for i in range(1, M + 1)])
# print(candidates)

for time in range(1, 101):
    if timeline2[time]: # 만약 아팠다면 그 전의 먹은 사람과 머쉬룸을 조사
        person = timeline2[time] 

        current_cand = set()
        
        for in_time in range(1, time):

            if timeline1[in_time]:

                for p, m in timeline1[in_time]:

                    if p == person:
                        current_cand.add(m)

        if len(current_cand):
            # print(current_cand)

            candidates = candidates & current_cand

# print(*candidates)
max_med = 0

for candidate in candidates:
    curr_med = len(eat_mushroom[candidate])
    max_med = max(max_med, curr_med)
    # print(candidate, *eat_mushroom[candidate], " len: ", curr_med)

print(max_med)