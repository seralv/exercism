def add_prefix_un(word):
    return 'un' + word


def make_word_groups(vocab_words):
    separator = ' :: ' + vocab_words[0]
    return separator.join(vocab_words)


def remove_suffix_ness(word):
    if word[:-4][-1] == 'i':
        return word[:-5] + 'y'
    else:
        return word[:-4]


def adjective_to_verb(sentence, index):
    return sentence.split()[index].rstrip('.') + 'en'

