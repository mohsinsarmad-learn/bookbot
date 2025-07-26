def sort_on(items):
    return items["num"]


def get_number_of_words(words):

    list_of_words = words.split()
    return len(list_of_words)


def get_number_of_characters_repeated(content):
    dic = {}
    content = content.lower()
    print("Stared the counting of the characters ......")
    for c in range(0, len(content) - 1):
        if content[c] not in dic:
            dic[content[c]] = 1
        else:
            dic[content[c]] += 1

    return dic


def convert_to_sorted_list(dict):
    converted_list = []
    for d in dict:
        converted_list.append({"char": d, "num": dict[d]})
    converted_list.sort(reverse=True, key=sort_on)
    return converted_list
