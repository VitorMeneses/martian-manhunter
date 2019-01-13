import metamorphosis
import nltk


classifier = nltk.NaiveBayesClassifier.train(metamorphosis.base_completed)
print(classifier.show_most_informative_features(5))