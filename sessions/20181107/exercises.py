import nltk


def vocabulary(sentences):
    # first collect all the tokens
    tokens = []
    for s in sentences:
        tokens.extend(nltk.word_tokenize(s))
    # now get the tokens, put them in lower case using set() and sort them
    return sorted(set([t.lower() for t in tokens]))


def vocabulary2(sentences):
    # shorter, but requires some level of comfort with reading list
    # comprehensions with two "for" keywords
    words = [w for s in sentences for w in nltk.word_tokenize(s) ]
    return sorted(set([w.lower() for w in words]))


def vocabulary3(sentences):
    # even shorter
    return sorted(set([w.lower() for s in sentences for w in nltk.word_tokenize(s)]))


def vocabulary4(sentences):
    # and you can even leave those square brackets out
    return sorted(set(w.lower() for s in sentences for w in nltk.word_tokenize(s)))


def vocabulary5(sentences):
    # same as vocabulary1(), but with a test added to filter out some tokens
    tokens = []
    for s in sentences:
        tokens.extend(nltk.word_tokenize(s))
    return sorted(set([t.lower() for t in tokens if t.isalpha()]))


def last_three_words(s):
    return nltk.word_tokenize(s)[-3:]


if __name__ == '__main__':

    sent1 = 'This is sentence 1.'
    sent2 = 'And this is sentence 2.'

    print(vocabulary([sent1, sent2]))
    print(vocabulary2([sent1, sent2]))
    print(vocabulary3([sent1, sent2]))
    print(vocabulary4([sent1, sent2]))
    print(vocabulary5([sent1, sent2]))

    print(last_three_words(sent2))
