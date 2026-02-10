N = int(input())
string = input()

min_length = float('inf')

for length in range(1, N + 1):
    
    for idx in range(N - length + 1):
        temp = string[idx : idx + length]
        
        if string.count(temp) > 1:
            break
        else:
            min_length = min(min_length, len(temp))            

print(min_length)