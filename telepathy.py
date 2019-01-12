import nltk
from data import basedatas


# nltk.download()


def remove_stop_words(text):
    phrases = []
    for (words, emotions) in text:
        nostop = [p for p in words.split() if p not in basedatas.stopwords]
        phrases.append((nostop, emotions))
    return phrases


print(remove_stop_words(basedatas.texts))
