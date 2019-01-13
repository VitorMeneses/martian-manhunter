import metamorphosis
import nltk


classifier = nltk.NaiveBayesClassifier.train(metamorphosis.base_completed)
print(classifier.labels())