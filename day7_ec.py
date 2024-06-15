#Write a function that takes a list of names and returns only those that start with S and how many times that
#name appears
from collections import Counter

def s_count(list: list):
    filtered_list = [item for item in list if item.startswith('S')]
    counter = Counter(filtered_list)
    return counter.items()

names = ["Joseph", "Nathan", "Sasha", "Kelly",
"Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

answer = s_count(names)
print(answer)