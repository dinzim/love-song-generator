import random as rand

class WordState:
    """
    Helper class representing a word and all its next words and frequencies.
    """
    def __init__(self):
        self._next_words = {} # A dict with all the next words and their frequencies.
        
    def add_next_word(self, next_word):
        """Introduces a new next word to the current word.
        If the word already exists in the dict, its count is incremented."""
        self._next_words[next_word] = self._next_words.get(next_word, 0) + 1
            
    def has_next(self):
        """True if there are any more words following this one."""
        return bool(self._next_words)
        
    def get_next(self):
        """Returns a random next word based on probability."""
        #weighted random sampling
        next_word = rand.choices(
            list(self._next_words.keys()), #population is the words
            weights = list(self._next_words.values()), #weights are the number of times they are counted
            k = 1)[0] #only get one word as return
        return next_word
            