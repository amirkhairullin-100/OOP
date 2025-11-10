import re
class MinMaxWordFinder:
    def __init__(self):
        self.min_length = float('inf')
        self.min_words = []
        self.max_length = float('-inf')
        self.max_words = set()
    def add_sentence(self, sentence):
        words = re.findall(r'\b\w+\b', sentence)
        for word in words:
            length = len(word)
            if length < self.min_length:
                self.min_length = length
                self.min_words = [word]
            elif length == self.min_length:
                self.min_words.append(word)
            if length > self.max_length:
                self.max_length = length
                self.max_words = {word}
            elif length == self.max_length:
                self.max_words.add(word)
    def shortest_words(self):
        return sorted(self.min_words)
    def longest_words(self):
        return sorted(list(self.max_words))
finder1 = MinMaxWordFinder()
finder1.add_sentence('hello abc world')
finder1.add_sentence('def asdf qwert')
print(' '.join(finder1.shortest_words()))
print(' '.join(finder1.longest_words()))
print()
finder2 = MinMaxWordFinder()
finder2.add_sentence('hello')
finder2.add_sentence('abc')
finder2.add_sentence('world')
finder2.add_sentence('def')
finder2.add_sentence('asdf')
finder2.add_sentence('qwert')
print(' '.join(finder2.shortest_words()))
print(' '.join(finder2.longest_words()))
print()
finder3 = MinMaxWordFinder()
finder3.add_sentence('hello')
finder3.add_sentence('  abc     def    ')
finder3.add_sentence('world')
finder3.add_sentence('            abc          ')
finder3.add_sentence('asdf')
finder3.add_sentence('qwert')
print(' '.join(finder3.shortest_words()))
print(' '.join(finder3.longest_words()))