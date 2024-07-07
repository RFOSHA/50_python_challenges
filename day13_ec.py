# Write a function called python_snakes that takes a number as
# an argument and creates the pyramid shape using the number’s
# range. (Hint: Use the loops and emoji libraries for snake emojis.)
# If you pass 7 as an argument, your code should print the
# following:

from emoji import emojize
def python_snakes(num: int):
    for i in range(num):
        for k in range (i+1):
            print(emojize(':snake:'), end=" ")
        print("\n")

python_snakes(7)