import string


def set_lower_style_and_erase_punctuation(input_text):
    input_text = input_text.lower()
    for ch in input_text:
        if ch in string.punctuation:
            input_text = input_text.replace(ch, "")
    return input_text


def count_words(input_text):
    print(f"Количество слов в тексте: {len(input_text.split(" "))}")


def find_longest_word(input_text):
    longest_word = ""
    for word in input_text:
        if len(word) > len(longest_word):
            longest_word = word

    print(f"Самое длинное слово: {longest_word}")


def count_vowel(input_text):
    vowel_count = 0
    for ch in input_text:
        if ch in "аеёиоуыэюя":
            vowel_count += 1

    print(f"Количество гласных в тексте: {vowel_count}")


def count_word_repetitions(input_text):
    dict_words = {}
    for word in input_text:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1

    print("Количество повторений каждого слова:")
    for key, value in dict_words.items():
        print(f"{key}: {value}")


def analyze_the_text(input_text):
    count_words(input_text)
    find_longest_word(input_text.split(" "))
    count_vowel(input_text)
    count_word_repetitions(input_text.split(" "))


user_text = set_lower_style_and_erase_punctuation(input("Введите текст:\n"))

analyze_the_text(user_text)
