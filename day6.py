#Write a function called use_name that generates a username from the user's emai. Ask the user to input an email
#and the function should trim off the @ and beyond to make the user name

def user_name(email: str):
    user_name = email.split('@')[0]
    return user_name

email = 'ben@gmail.com'
answer = user_name(email)
print(answer)