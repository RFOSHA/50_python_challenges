def check_duplicates(list):
    seen = set()
    duplicates = set()
    for item in list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

fruits = ['apple', 'orange', 'banana', 'apple', 'banana']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

answer = check_duplicates(fruits)
answer2 = check_duplicates(names)

print(answer)
print(answer2)