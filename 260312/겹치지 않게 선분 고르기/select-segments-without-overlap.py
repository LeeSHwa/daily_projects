n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
visited = [False] * n
array = [0] * 1001
ans = 0

def is_duplicated(a1, a2):
    for idx in range(a1, a2 + 1):
        if array[idx] > 1:
            return True
    
    return False

def apply_var(x1, x2, var):
    for idx in range(x1, x2 + 1):
        array[idx] += var

def recurr(dep, cnt):
    global ans
    if dep == n:
        ans = max(ans, cnt)
        return
    
    curr_x1, curr_x2 = lines[dep]

    # 1. 적용
    visited[dep] = True
    apply_var(curr_x1, curr_x2, 1)

    # 2. 재귀
    if is_duplicated(curr_x1, curr_x2):
        apply_var(curr_x1, curr_x2, -1)
        recurr(dep + 1, cnt)
    else:
        recurr(dep + 1, cnt + 1)

    # 3. 반환
    visited[dep] = False
    apply_var(curr_x1, curr_x2, -1)

for i in range(n):
    visited[i] = True
    recurr(i, 0)
    visited[i] = False


print(ans)