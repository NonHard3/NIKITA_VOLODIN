import string

word_count = 0
longest_word = ""
vowel_count = 0

dict_words = {}
max_char_in_word = 0

text = input("Введите текст:\n")

for word in text.split(" "):
    char_count = 0
    current_word = ""

    for char in word.lower():
        if char in string.punctuation:
            continue
        if char in "аеёиоуыэюя":
            vowel_count += 1

        current_word += char
        char_count += 1

    if current_word in dict_words:
        dict_words[current_word] += 1
    else:
        dict_words[current_word] = 1

    if char_count > max_char_in_word:
        longest_word = current_word
        max_char_in_word = char_count

    word_count += 1

print(f"Количество слов в тексте: {word_count}")
print(f"Самое длинное слово: {longest_word}")
print(f"Количество гласных в тексте: {vowel_count}")
print("Количество повторений каждого слова:")

for key, value in dict_words.items():
    print(f"{key}: {value}")
