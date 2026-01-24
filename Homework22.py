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


def count_vowel(input_text, count):
    for ch in input_text:
        if ch in "аеёиоуыэюя":
            count += 1


def analyze_the_text(input_text):
    longest_word = ""
    vowel_count = 0
    dict_words = {}

    for word in input_text.split(" "):
        count_word_repetitions(word, dict_words)

        longest_word = find_longest_word(word, longest_word)

    count_vowel(input_text, vowel_count)

    print(f"Количество слов в тексте: {len(input_text.split(" "))}")
    print(f"Самое длинное слово: {longest_word}")
    print(f"Количество гласных в тексте: {vowel_count}")
    print("Количество повторений каждого слова:")

    for key, value in dict_words.items():
        print(f"{key}: {value}")


user_text = set_lower_style_and_erase_punctuation(input("Введите текст:\n"))

analyze_the_text(user_text)
