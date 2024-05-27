#Write a function that orders all of the names in a list that start with a lowercase in reverse alphabetical order

def lowercase_sort(name_list: list):
    tuple_list = ()
    for name in name_list:
        first_letter = name[0]
        if first_letter.islower():
            tuple_list = tuple_list + (name,)
    list_rep = list(tuple_list)
    list_rep.sort(reverse=True)
    tuple_list = tuple(list_rep)
    return tuple_list


names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

answer = lowercase_sort(names)
print(answer)