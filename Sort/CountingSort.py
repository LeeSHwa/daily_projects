def bing(max_value, li): # counting sort / max_value = 최대 값, li = 리스트
    counting = [0 for _ in range(max_value)]
    
    for i in range(len(li)):
        counting[li[i]] += 1
    
    return counting

ans_li = bing(30, [0, 28, 25, 15, 2, 12, 17, 11, 29, 29, 29])

print(ans_li)

temp = []
for i in range(len(ans_li)):
    if ans_li[i] != 0:
        for _ in range(ans_li[i]):
            temp.append(i)
    else:
        pass
print(temp)