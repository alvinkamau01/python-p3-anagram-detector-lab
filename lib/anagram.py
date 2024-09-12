# anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        def are_anagrams(word1, word2):
            return sorted(word1) == sorted(word2)
        
        return [word for word in word_list if are_anagrams(self.word, word)]
