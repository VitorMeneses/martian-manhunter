import nltk
from data import basedatas


# nltk.download()

#using the stopwords to remove dirt in the sentences

def remove_stop_words(text):
    phrases = []
    for (words, emotions) in text:
        nostop = [w for w in words.split() if w not in basedatas.stopwordsnltk]
        phrases.append((nostop, emotions))
    return phrases


print(remove_stop_words(basedatas.texts))

#implementing stem radical extraction with stemming

def apply_stemmer(text):
    stemmer = nltk.stem.RSLPStemmer()
    phrases_stemming = []
    for (words, emotions) in text:
        with_stemming = [str(stemmer.stem(w)) for w in words.split() if w not in basedatas.stopwordsnltk]
        phrases_stemming.append((with_stemming, emotions))
    return phrases_stemming

phrases_with_stemming = apply_stemmer(basedatas.texts)
print(phrases_with_stemming)

#listing all words in the database

def search_words(phrases):
    all_words = []
    for (words, emotions) in phrases:
        all_words.extend(words)
    return all_words

words = search_words(phrases_with_stemming)
print(words)

#implementing frequency word search

def search_frequency(words):
    words = nltk.FreqDist(words)
    return words

frequency = search_frequency(words)
print(frequency.most_common(50))