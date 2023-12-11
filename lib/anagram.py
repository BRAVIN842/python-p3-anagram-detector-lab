# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [w for w in word_list if self.is_anagram(w)]

    def is_anagram(self, other_word):
        other_word_lower = other_word.lower()
        return other_word_lower != self.word and sorted(other_word_lower) == sorted(self.word)
