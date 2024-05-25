import math

def divide_or_square(num):
    if num % 5 == 0:
        sqaure_root = math.sqrt(num)
        return sqaure_root
    else:
        return num % 5


number = 12
answer = divide_or_square(number)
print(answer)