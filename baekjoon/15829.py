# https://www.acmicpc.net/problem/15829

L = int(input())
word = list(input())

if L != len(word): # 길이가 안맞으면 raise
    raise 

M = 1234567891 # mod
r = 31 # 곱해 줄 특정숫자 (보통 M과 서로소임)
hap = 0 # 더한건 여기로

# alphabet = {} # 이건 간단하게 반복문 통해서 하는 방법
# for i in range(26):
#     alphabet[chr(97+i)] = i+1

alphabet = { # 그냥 하나하나 다 등록해버려
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 
    's': 19, 't': 20, 'u': 21, 'v': 22, 
    'w': 23, 'x': 24, 'y': 25, 'z': 26
}


for i in range(0,L):
    hap += alphabet.get(word.pop(0))*r**i%M

print(hap)

