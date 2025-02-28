# https://www.acmicpc.net/problem/28702

first = input()
second = input()
third = input()
flag = False

def FB(num):
    if num % 5 == 0 and num % 3 == 0:
        return 'FizzBuzz'
    
    elif num % 3 == 0 and num % 5 != 0:
        return 'Fizz'

    elif num % 3 != 0 and num % 5 == 0:
        return 'Buzz'
    
    else:
        return num
    

if first.isdigit() == True:
    print(FB(int(first)+3))
    flag = True

if second.isdigit() == True and flag == False:
    print(FB(int(second)+2))
    flag = True

if third.isdigit() == True and flag == False:
    print(FB(int(third)+1))