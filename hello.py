import itertools
from gensim.models.word2vec import Text8Corpus
from glove import Corpus, Glove
from mysentences import MySentences


sentences = MySentences('./input')
corpus = Corpus()
corpus.fit(sentences, window=5)
print(corpus.dictionary)
glove = Glove(no_components=100, learning_rate=0.05)
glove.fit(corpus.matrix, epochs=30, no_threads=4, verbose=True)
glove.add_dictionary(corpus.dictionary)


# glove.most_similar('Alendronate')
print('Alendronate', glove.most_similar('Alendronate', number=10))
print('Pet', glove.most_similar('Pet', number=10))
print('1-(419)684-7366', glove.most_similar('1-(419)684-7366', number=10))
