from random import randint, randrange

import pyrhyme



class RandomWordGenerator:
    def __init__(self):
        self.nouns = {}
        self.verbs = {}
        self.adjectives = {}
        self.adverbs = {}
        self.subjects = ["I", "He", "She", "They", "We", "You"]
        self.rhymer = pyrhyme.RhymeBrain()

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

    def make_rhyme(self, word):

        rhymes = [x.word for x in self.rhymer.rhyming(word, lang='en')]
        if len(rhymes) == 0:
            return word
        else:
            return rhymes[0]

    def print_sample(self):

        for i in range(1, 5):
            print(self.adjectives[i][:10], self.adverbs[i][:10], self.nouns[i][:10], self.verbs[i][:10])

    def generate_word(self, word):
        if word == "Noun":
            return self.random_noun()
        elif word == "Adjective":
            return self.random_adjective()
        elif word == "Adverb":
            return self.random_adverb()
        elif word == "Verb":
            return self.random_verb()
        elif word == "Subject":
            result = self.random_subject()
            return result


    def random_subject(self):
        return self.subjects[randint(0, 5)]

    def random_verb(self):
        syllable = randint(1,4)
        return self.verbs[syllable][randrange(0, len(self.verbs[syllable])-1)]

    def random_adjective(self):
        syllable = randint(1,4)
        return self.adjectives[syllable][randrange(0, len(self.adjectives[syllable])-1)]

    def random_adverb(self):
        syllable = randint(1,4)
        return self.adverbs[syllable][randrange(0, len(self.adverbs[syllable])-1)]

    def random_noun(self):
        syllable = randint(1,4)
        return self.nouns[syllable][randrange(0, len(self.nouns[syllable])-1)]

class RandomSentenceGenerator:
    def __init__(self):
        self.word_generator = RandomWordGenerator()
        self.sentence_structures = {
            0: ["Subject", "Verb"],
            1: ["Subject", "Verb", "Noun"],
            2: ["Subject", "Verb", "Adjective"],
            3: ["Subject", "Verb", "Adverb"],
            4: ["Noun", "Verb", "Noun"],
        }

    def generate_sentence(self):
        sentence_structure = self.sentence_structures[randint(0, 4)]
        first_line = ""
        second_line = ""
        rhyme_index = randint(0, len(sentence_structure)-1)
        for index, word in enumerate(sentence_structure):
            new_word = self.word_generator.generate_word(word)
            new_word2 = self.word_generator.generate_word(word)
            if index == rhyme_index:
                new_word2 = self.word_generator.make_rhyme(new_word)
            first_line += new_word + " "
            second_line += new_word2 + " "
        return first_line + "\n" + second_line


sentence_generator = RandomSentenceGenerator()

poem = ""
for i in range(1, 4):
    sentence = sentence_generator.generate_sentence()
    poem += sentence + "\n"

import os

os.system(f"say -v Alex '{poem}'")