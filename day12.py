# Write a function called count_dots. This function takes a string
# separated by dots as a parameter and counts how many dots are in
# the string. For example, "h.e.l.p." should return 4 dots, and
# "he.lp." should return 2 dots.

def count_dots(string: str):
    num_dots = string.count('.')
    return num_dots

string = "h.e.l.p."
answer = count_dots(string)
print(answer)