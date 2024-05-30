#Write a function that takes a list of strings and returns the index of the longest word in list. If all strings
#are of equal length the fucntion should return 0

def word_index(list: list):
    max_len = 0
    index = int()
    first_word_len = len(list[0])

    if all(len(word) == first_word_len for word in list):
        return 0
    else:
        for word in list:
            if len(word) > max_len:
                index = list.index(word)
                max_len = len(word)
        return(index)

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

answer1 = word_index(words1)
answer2 = word_index(words2)

print(answer1, answer2)