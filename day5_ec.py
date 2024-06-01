#Take a list of values and count their occurence and return a list of tuples that has the value the number of occurrences
from collections import Counter

def tuple_count(my_list: list):
    my_list = [string.title() for string in my_list]
    counter = Counter(my_list)
    print(counter)
    return list(counter.items())

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

answer = tuple_count(students)
print(answer)
