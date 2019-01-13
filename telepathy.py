import metamorphosis
import nltk


classifier = nltk.NaiveBayesClassifier.train(metamorphosis.base_completed)


test = '.net'
tests_temming = []
stemmer = nltk.stem.RSLPStemmer()
for (words_training) in test.split():
    comstem = [p for p in words_training.split()]
    tests_temming.append(str(stemmer.stem(comstem[0])))
#print(tests_temming)

new = metamorphosis.extractor_words(tests_temming)
#print(new)

print(classifier.classify(new))
result = classifier.prob_classify(new)
for emotions in result.samples():
    print("%s: %f" % (emotions, result.prob(emotions)))
