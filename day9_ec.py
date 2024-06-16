# Write a function called zeros_last. This function takes a list as an
# argument. If a list has zeros (0), it will move them to the end of the
# list and maintain the order of the other numbers in the list. If there
# are no zeros in the list, the function should return the original list,
# sorted in ascending order. For example, if you pass [1, 4, 6, 0, 7,
# 0, 9] as an argument, your code should return [1, 4, 6, 9, 0, 0].
# If you pass [2, 1, 4, 7, 6] as your argument, your code should
# return [1, 2, 4, 6, 7].

def zeros_last(num_list: list):
    num_list = sorted(num_list)
    zero_count = num_list.count(0)
    num_list = [num for num in num_list if num != 0]
    i = 0
    while i < zero_count:
        num_list.append(0)
        i += 1
    return num_list

numbers = [2, 1, 4, 7, 6]

answer = zeros_last(numbers)
print(answer)