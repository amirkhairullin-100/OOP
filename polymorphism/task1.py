class Selector:
    def __init__(self, numbers):
        self.numbers = numbers
    def get_odds(self):
        return [x for x in self.numbers if x % 2 != 0]
    def get_evens(self):
        return [x for x in self.numbers if x % 2 == 0]
values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))
print()
values2 = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
selector2 = Selector(values2)
odds = selector2.get_odds()
evens = selector2.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))
print()
values3 = []
selector3 = Selector(values3)
odds = selector3.get_odds()
evens = selector3.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))