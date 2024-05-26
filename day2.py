def convert_add(list: list):
    numbers = []
    for string in list:
        number = int(string)
        numbers.append(number)
    sum_of_nums = sum(numbers)
    return numbers, sum_of_nums

list_of_strings = ["1", "3", "5"]
answer, answer2 = convert_add(list_of_strings)
print(answer, answer2)