"""
Jiun Kim
M6 Poetry Slam

This is Poetry Maker Punchline King made by Jiun Kim.
The libraries used are pyrhyme which makes rhyme words and word files from the internet.
"""

from random import randint, randrange

import pyrhyme


class RandomWordGenerator:
    """
    This class makes random noun, verb, adjective, adverb and subject.
    It also creates rhyme given a word.
    """
    def __init__(self):
        self.nouns = {}
        self.verbs = {}
        self.adjectives = {}
        self.adverbs = {}
        self.subjects = ["I", "He", "She", "They", "We", "You"]
        self.rhymer = pyrhyme.RhymeBrain()

        for i in range(1, 5):
            # Loops through the files to store all the words from the 
            # prepared word files.
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
        """
        Uses rhyming library to pick the first(best) rhyme for a given word.
        """
        rhymes = [x.word for x in self.rhymer.rhyming(word, lang='en')]
        if len(rhymes) == 0:
            # Edge Case: There might be no rhymes. Then just return the original word.
            return word
        else:
            return rhymes[0]

    def generate_word(self, word):
        """
        Generate random word given the type of the word.
        """
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

    """
    Random word generating functions.
    """

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
    """
    Uses random word generator in order to create random sentences.
    """
    def __init__(self):
        self.word_generator = RandomWordGenerator()
        #Basic sentence structures to provide structure to the poem.
        self.sentence_structures = {
            0: ["Subject", "Verb"],
            1: ["Subject", "Verb", "Noun"],
            2: ["Subject", "Verb", "Adjective"],
            3: ["Subject", "Verb", "Adverb"],
            4: ["Noun", "Verb", "Noun"],
        }

    def generate_sentence(self):
        """
        Create a pair of sentences. Second sentence has a word that
        rhymes with the word in the first sentence.
        """
        sentence_structure = self.sentence_structures[randint(0, 4)]
        first_line = ""
        second_line = ""
        rhyme_index = randint(0, len(sentence_structure)-1) # arbitrarily pick an index that will rhyme.
        for index, word in enumerate(sentence_structure):
            new_word = self.word_generator.generate_word(word)
            new_word2 = self.word_generator.generate_word(word)
            if index == rhyme_index:
                new_word2 = self.word_generator.make_rhyme(new_word)
            first_line += new_word + " "
            second_line += new_word2 + " "
        return first_line + "\n" + second_line


class Evaluator:
    """
    Evalate a poem.
    """
    def __init__(self):
        self.alphabets = []

    def evaluate(self, poem):
        """
        Check the diversity of the words used in the poem.
        The first letter of the words in the poem should be diverse and
        the number of different first letter used will be the score of the
        poem.
        """
        words = poem.split()
        result = 0
        for word in words:
            self.alphabets.append(word[0])
        result += len(list(set(self.alphabets)))
        return result

sentence_generator = RandomSentenceGenerator()
evaluator = Evaluator()

poem = ""
for i in range(1, 5):
    sentence = sentence_generator.generate_sentence()
    poem += sentence + "\n\n"

result = str(evaluator.evaluate(poem))
title = sentence_generator.word_generator.generate_word("Noun")
print(f"\nTitle: {title} \n\n")
print(poem)
print("The score is ", result)

import os

os.system(f"say -v Alex '{poem}'")
os.system(f"say -v Alex 'The score is {result}'")