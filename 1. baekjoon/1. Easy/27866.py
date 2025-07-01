S = input()
i = int(input())


if i > len(S):
    raise
else:
    print(S[i-1])