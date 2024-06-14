#Write a function that zeros out the first and last name in a list

def zeroed(list: list):
    last_indx = len(list) - 1
    list[0] = 0
    list[last_indx] = 0
    return list

sample_list = [1,2,3,4,5]
answer = zeroed(sample_list)
print(answer)