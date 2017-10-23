
import os


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            words_in_doc = []
            for line in open(os.path.join(self.dirname, fname)):
                words_in_doc = words_in_doc + line.split()
            yield words_in_doc
