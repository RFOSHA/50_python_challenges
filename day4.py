#Write a function called only_floats that takes two parameters and returns 2 if both arguements are floats and 1 if
# only one is a float and 0 if neither arguement is a float

def only_floats(arg1, arg2):
    if isinstance(arg1, float) and isinstance(arg2, float):
        return 2
    elif not isinstance(arg1, float) and not isinstance(arg2, float):
        return 0
    else:
        return 1

var1 = 12.1
var2 = 23.1
var3 = 12
var4 = 23
var5 = 12.1
var6 = 23

answer1 = only_floats(var1, var2)
answer2 = only_floats(var3, var4)
answer3 = only_floats(var5, var6)
print(answer1, answer2, answer3)