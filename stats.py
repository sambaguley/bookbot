def count_words(text_content):
    word_list = text_content.split()
    word_count = len(word_list)
    return word_count

def count_characters(text_content):
    lower_case_text = text_content.lower()
    char_dict = {}
    for char in lower_case_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["count"]

def sort_results(char_dict):
    dict_list = []
    for key in char_dict:
        if key.isalpha():
            dict_list.append({"char": key, "count": char_dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
