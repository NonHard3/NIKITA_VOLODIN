import string


def set_lower_style_and_erase_punctuation(input_text):
    input_text = input_text.lower()
    for ch in input_text:
        if ch in string.punctuation:
            input_text = input_text.replace(ch, "")
    return input_text


def count_word_repetitions(word, dict):
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1


word_count = 0
longest_word = ""
vowel_count = 0

dict_words = {}

text = set_lower_style_and_erase_punctuation(input("Введите текст:\n"))

for word in text:

    for char in word():
        if char in "аеёиоуыэюя":
            vowel_count += 1

    count_word_repetitions(word, dict_words)

    if len(word) > len(longest_word):
        longest_word = word

    word_count += 1

print(f"Количество слов в тексте: {word_count}")
print(f"Самое длинное слово: {longest_word}")
print(f"Количество гласных в тексте: {vowel_count}")
print("Количество повторений каждого слова:")

for key, value in dict_words.items():
    print(f"{key}: {value}")
