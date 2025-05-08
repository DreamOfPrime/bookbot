def get_num_words(contents):
    words = contents.split()
    word_count = len(words)
    return word_count

def get_num_cha(contents):
    contents = contents.lower()
    counts = {}
    for cha in contents:
        if cha not in counts:
            counts[cha] = 1    
        else:
            counts[cha] += 1
    return counts

def chars_to_sorted_list(char_dict):
    result = []
    for char, count in char_dict.items():
        result.append({"char": char, "num": count})
    # Now sort the list using the sort_on function
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(dict):
    return dict["num"]
