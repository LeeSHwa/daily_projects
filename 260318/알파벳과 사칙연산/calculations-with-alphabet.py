expression = list(input())
N = len(expression)
# Please write your code here.

mapping_table = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5}
alphas = [0, 0, 0, 0, 0, 0]

def cal_exp(exp):
    if len(exp) == 1:
        return 4

    idx = 1
    num = exp[0]
    oper = None
    
    while idx < len(exp):
        oper = exp[idx]
        next_num = exp[idx + 1]

        if oper == '+':
            num += next_num

        elif oper == '-':
            num -= next_num
        
        elif oper == '*':
            num *= next_num
        
        idx += 2

    return num

max_result = 0

def recurr(alphas, idx):
    global max_result

    if idx == 6:
        temp = expression.copy()

        for i in range(0, N, 2):
            temp[i] = alphas[mapping_table[temp[i]]]

        curr_result = cal_exp(temp)
        max_result = max(max_result, curr_result)
    
        return
    
    alphas[idx] = 4

    recurr(alphas, idx + 1)
    
    alphas[idx] = 1

    recurr(alphas, idx + 1)

recurr(alphas, 0)

print(max_result)