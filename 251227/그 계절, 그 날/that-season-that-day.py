def is_leafYear(Year):
    if Year % 4 != 0:
        return False
    if Year % 100 != 0:
        return True
    if Year % 100 == 0 and Year % 400 == 0:
        return True

    return True

def what_is_the_weather(Year, Month, Day):
    
    if is_leafYear(Year):
        #                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
        num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        #                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
        num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if 0 < Month < 13 and Day <= num_of_days[Month]:
        if 3 <= Month <= 5:
            return "Spring"
        elif 6 <= Month <= 8:
            return "Summer"
        elif 9 <= Month <= 11:
            return "Fall"
        else:
            return "Winter"

    else:
        return -1

Y, M, D = map(int, input().split())

answer = what_is_the_weather(Y, M, D)

print(answer)