import nltk
from data import basedatas


# nltk.download()


def remove_stop_words(text):
    phrases = []
    for (phrases, emotions) in text:
        nostop = [p for p in phrases.split() if p not in basedatas.stopwords]
        phrases.append((nostop, emotions))
    return phrases


print(remove_stop_words(basedatas.texts))
