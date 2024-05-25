def longest_value(dict):
    first_value = list(dict.values())[0]
    return first_value

def longest_value2(dict):
    print(dict.values())
    for value in dict.values():
        print(len(value))
    longest = max(dict.values(), key=len)
    return longest

fruits = {'fruit': ['apple', 'bananas'], 'color': 'green'}
fruits2 = {'fruit': 'apple', 'color': 'green'}
answer = longest_value2(fruits2)
print(answer)