#Write a function that takes a number and returns a string of characters separated by a '.' for length of the
#number you pass in

def string_range(number: int):
    string = ''
    for i in range(number):
        string = string + str(i) + '.'
    return string

number = 6
answer = string_range(number)
print(answer)
