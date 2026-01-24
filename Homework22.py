import string


def set_lower_style_and_erase_punctuation(input_text):
    input_text = input_text.lower()
    for ch in input_text:
        if ch in string.punctuation:
            input_text = input_text.replace(ch, "")
    return input_text


def find_longest_word(current_word, max_longest_word):
    if len(current_word) > len(max_longest_word):
        return current_word
    else:
        return max_longest_word


def count_word_repetitions(current_word, dict_type):
    if current_word in dict_type:
        dict_type[current_word] += 1
    else:
        dict_type[current_word] = 1


word_count = 0
longest_word = ""
vowel_count = 0

dict_words = {}

text = set_lower_style_and_erase_punctuation(input("Введите текст:\n"))

for word in text.split(" "):
    count_word_repetitions(word, dict_words)

    longest_word = find_longest_word(word, longest_word)

    word_count += 1

for char in text:
    if char in "аеёиоуыэюя":
        vowel_count += 1

print(f"Количество слов в тексте: {word_count}")
print(f"Самое длинное слово: {longest_word}")
print(f"Количество гласных в тексте: {vowel_count}")
print("Количество повторений каждого слова:")

for key, value in dict_words.items():
    print(f"{key}: {value}")
