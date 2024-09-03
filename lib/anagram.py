# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word 

    def match(self, anagrams):
        matches = []
        for name in anagrams:
            if sorted(name) == sorted(self.word):
                matches.append(name)
        return matches

