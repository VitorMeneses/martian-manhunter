import nltk
from data import basedatas


# nltk.download()


def remove_stop_words(text):
    phrases = []
    for (words, emotions) in text:
        nostop = [w for w in words.split() if w not in basedatas.stopwordsnltk]
        phrases.append((nostop, emotions))
    return phrases


print(remove_stop_words(basedatas.texts))


def apply_stemmer(text):
    stemmer = nltk.stem.RSLPStemmer()
    phrases_stemming = []
    for (words, emotions) in text:
        with_stemming = [str(stemmer.stem(w)) for w in words.split() if w not in basedatas.stopwordsnltk]
        phrases_stemming.append((with_stemming, emotions))
    return phrases_stemming

phrases_with_stemming = apply_stemmer(basedatas.texts)
print(phrases_with_stemming)

def search_words(phrases):
    all_words = []
    for (words, emotions) in phrases:
        all_words.extend(words)
    return all_words

words = search_words(phrases_with_stemming)
print(words)
