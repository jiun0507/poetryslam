from random import randint

import pyrhyme

g = pyrhyme.RhymeBrain()
results = [x for x in g.rhyming('foo')]



sentence_structures = {""}


class RandomWordGenerator:
    def __init__(self):
        self.nouns = {}
        self.verbs = {}
        self.adjectives = {}
        self.adverbs = {}
        self.subjects = ["I", "He", "She", "They", "We", "You"]

        for i in range(1, 5):
            f = open(f"adjectives/{i}syllableadjectives.txt", "r")
            self.adjectives[i] = f.read().split()
            f.close()

            f = open(f"adverbs/{i}syllableadverbs.txt", "r")
            self.adverbs[i] = f.read().split()
            f.close()

            f = open(f"nouns/{i}syllablenouns.txt", "r")
            self.nouns[i] = f.read().split()
            f.close()

            f = open(f"verbs/{i}syllableverbs.txt", "r")
            self.verbs[i] = f.read().split()
            f.close()

    def print_sample(self):

        for i in range(1, 5):
            print(self.adjectives[i][:10], self.adverbs[i][:10], self.nouns[i][:10], self.verbs[i][:10])

    def generate_word(self, word):
        if word == "Noun":
            return self.random_noun():
        if word == "Adjective":
            return self.random_adjective():
        if word == "Adverb":
            return self.random_adverb():
        if word == "Verb":
            return self.random_verb():
        if word == "Subject":
            return self.random_subject():


    def random_subject(self):
        return self.subjects[randint(0, 5)]

    def random_verb(self):
        syllable = randint(1,4)
        return self.verbs[syllable][randint(0, len(self.verbs)-1)]

    def random_adjective(self):
        syllable = randint(1,4)
        return self.adjectives[syllable][randint(0, len(self.adjectives)-1)]

    def random_adverb(self):
        syllable = randint(1,4)
        return self.adverbs[syllable][randint(0, len(self.adverbs)-1)]

    def random_noun(self):
        syllable = randint(1,4)
        return self.nouns[syllable][randint(0, len(self.nouns)-1)]

class RandomSentenceGenerator:
    def __init__(self):
        self.word_generator = RandomWordGenerator()
        self.sentence_structures = {
            0: ["Subject", "Verb"],
            1: ["Subject", "Verb", "Noun"],
            2: ["Subject", "Verb", "adjective"],
            3: ["Subject", "Verb", "adverb"],
            4: ["Noun", "Verb", "Noun"],
        }

    def generate_sentence(self):
        sentence_structure = self.sentence_structures[randint(0, 4)]
        result = ""
        for word in sentence_structures:
            result += self.word_generator(word)
            result += " "

        return result[-1:]

