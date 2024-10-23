SIZE = 5
linear_list = ["ON" for _ in range(SIZE)]

# linear_list = []

def add_data(word):
    
    linear_list.append(None)
    list_len = len(linear_list)
    linear_list[list_len-1] = word
            

def insert_data(word, position):

    end = len(linear_list) - 1

    if position >= end:
        raise ValueError("It's impossible because the position exceeds the length of the list.")
    
    linear_list.append(None)
    
    for i in range(end,position,-1):
        linear_list[i] = linear_list[i-1]
        linear_list[i-1] = None

    linear_list[position] = word
        


print(linear_list)

insert_data("1번",1)
insert_data("2번",2)

print(linear_list)

    