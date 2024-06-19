# Write a function called equal_strings. The function takes
# two strings as arguments and compares them. If the strings
# are equal (if they have the same characters and have equal
# length), it should return True; if they are not, it should
# return False. For example, "love" and "evol" should
# return True.

def equal_strings(string1: str, string2: str):
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        return True
    else:
        return False

str1 = "love"
str2 = "evol"
answer = equal_strings(str1, str2)
print(answer)
