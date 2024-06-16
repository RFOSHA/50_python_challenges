# Create a function called biggest_odd that takes a string of
# numbers as an argument and returns the biggest odd number in
# the string. For example, if you pass "23569" as an argument, your
# function should return 9. Use list comprehension.

def biggest_odd(string: str):
    list = [int(num) for num in string]
    largest_num = max(list)
    return largest_num

string = "23569"
answer = biggest_odd(string)
print(answer)