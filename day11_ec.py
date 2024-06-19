# Write a function called swap_values. This function takes
# a list of numbers and swaps the first element with the last
# element. For example, if you pass [2, 4, 67, 7] as a
# argument, your function should return.
# [7, 4, 67, 2].

def swap_values(num_list: list):
    last_index = (len(num_list)-1)
    first_value = num_list[0]
    last_value =num_list[last_index]
    num_list[0] = last_value
    num_list[last_index] = first_value
    return num_list

numbers = [2, 4, 67, 7]
answer = swap_values(numbers)
print(answer)