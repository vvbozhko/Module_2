def single_root_words (root_word, *other_words):
    same_words = []
    for i in range(0, len(other_words)):
        a = root_word.lower()
        b = other_words[i].lower()
        if a in b or b in a:
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
