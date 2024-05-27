#Write a function that counts the number of students that have registered ("yes") from the register dictionary
def register_check(student_dict: dict):
    count = sum(1 for value in student_dict.values() if value == "yes")
    return count

register = {'Michael': 'yes',
            'John': 'no',
            'Peter': 'yes',
            'Mary': 'yes'}

answer = register_check(register)
print(answer)