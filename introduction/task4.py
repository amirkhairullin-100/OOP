class OddEvenSeparator:
    def __init__(self):
        self.evens = []
        self.odds = []
    def add_number(self, number):
        if number % 2 == 0:
            self.evens.append(number)
        else:
            self.odds.append(number)
    def even(self):
        return self.evens
    def odd(self):
        return self.odds
separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))
