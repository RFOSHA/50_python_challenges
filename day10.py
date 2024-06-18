# Write a function called hide_password that takes no
# parameters. The function takes an input (a password) from a user
# and returns a hidden password. For example, if the user enters
# "hello" as a password, the function should return "****" as a
# password and tell the user that the password is 4 characters
# long.

def hide_password(password: str):
    length = len(password)
    print(f"There are {length} characters in the password")
    return ''.join(['*' for char in password])



user_password = "hello)"
answer = hide_password(user_password)
print(answer)