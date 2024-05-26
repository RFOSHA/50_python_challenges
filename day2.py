def convert_add(list: list):
    numbers = []
    for string in list:
        number = int(string)
        numbers.append(number)
    return numbers

list_of_strings = ["1", "3", "5"]
answer = convert_add(list_of_strings)
print(answer)