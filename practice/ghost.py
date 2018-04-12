class Vocabulary:

    def __init__(self, words, minlength = 3):
        self.words = {word for word in words if len(word) >= minlength}
        self.fragments = {word[:i] for word in self.words for i in range(len(word) + 1)}

    def legal_plays(self, fragment):
        return {fragment + L for L in alphabet} & self.fragments

alphabet = 'abcdefghijklmnopqrstuvwxyz'

words = str.split


enable1 = Vocabulary(words(open('enable1.txt').read()))
