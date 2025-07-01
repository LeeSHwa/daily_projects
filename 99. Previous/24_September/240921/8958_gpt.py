def calculate_score(ox_line): # ox_line을 인수로 받아서
    tem = 0
    sum1 = 0
    for ch in ox_line: 
        if ch == 'O':
            tem += 1
            sum1 += tem
        else:
            tem = 0
    return sum1

n = int(input()) 
for i in range(n):
    ox_line = input()
    print(calculate_score(ox_line))