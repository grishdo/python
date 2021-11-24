def int_func(word):
    list_word = list(word)
    list_word[0] = list_word[0].upper()
    return ''.join(list_word)


words = input('Введите слова состоящие из маленьких латинских букв: ')

list_words = words.split()
words_upper = []
for word in list_words:
    words_upper.append(int_func(word))

print(' '.join(words_upper))
