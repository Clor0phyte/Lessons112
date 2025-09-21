def filter_words_by_lenght(words, min_length=3):
    return [word for word in words if len(word)> min_length]

print(filter_words_by_lenght(["Words", "something", "password"], 5))