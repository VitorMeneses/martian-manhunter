import nltk
from database import basedatas
import coaching


# module responsible for all processing of data that is available in the database

# using the stopwords to remove dirt in the sentences

def remove_stop_words(text):
    phrases = []
    for (words, emotions) in text:
        nostop = [w for w in words.split() if w not in basedatas.stopwordsnltk]
        phrases.append((nostop, emotions))
    return phrases


# implementing stem radical extraction with stemming

def apply_stemmer(text):
    stemmer = nltk.stem.RSLPStemmer()
    phrases_stemming = []
    for (words, emotions) in text:
        with_stemming = [str(stemmer.stem(w)) for w in words.split() if w not in basedatas.stopwordsnltk]
        phrases_stemming.append((with_stemming, emotions))
    return phrases_stemming


phrases_with_stemming_coaching = apply_stemmer(coaching.training.base_training)

# listing all words in the database

def search_words(phrases):
    all_words = []
    for (words, emotions) in phrases:
        all_words.extend(words)
    return all_words


words = search_words(phrases_with_stemming_coaching)


# implementing frequency word search

def search_frequency(words):
    words = nltk.FreqDist(words)
    return words


frequency = search_frequency(words)


# single word extraction

def search_words_single(frequency):
    freq = frequency.keys()
    return freq


single_words = search_words_single(frequency)


# word extractor of each sentence

def extractor_words(document):
    doc = set(document)
    features = {}
    for words in single_words:
        features['%s' % words] = (words in doc)
    return features


base_completed = nltk.classify.apply_features(extractor_words, phrases_with_stemming_coaching)
