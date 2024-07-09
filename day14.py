# Write a function called flat_list that takes one argument, a nested
# list. The function converts the nested list into a one-dimensional
# list. For example, [[2, 4, 5, 6]] should return [2, 4, 5, 6].

def flat_list(nest_list: list):
    flattened_list = [item for sublist in nest_list for item in sublist]
    return flattened_list


input = [[2, 4, 5, 6], [3, 4, 5, 6]]
answer = flat_list(input)
print(answer)
