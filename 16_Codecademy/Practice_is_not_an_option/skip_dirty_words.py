word = 'Fig.2'

def skip_dirty_words(single_word):
    if 'see Fig' in single_word  or 'Fig' in single_word or 'r . ' in single_word:
        return True
    else:
        return False

print(skip_dirty_words(word))