class Balance:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0
    def add_left(self, weight):
        self.left_weight += weight
    def add_right(self, weight):
        self.right_weight += weight
    def result(self):
        if self.left_weight == self.right_weight:
            return '='
        elif self.left_weight > self.right_weight:
            return 'L'
        else:
            return 'R'
balance1 = Balance()
balance1.add_right(10)
balance1.add_left(9)
balance1.add_left(2)
print(balance1.result())
print()
balance2 = Balance()
balance2.add_right(10)
balance2.add_left(5)
balance2.add_left(5)
print(balance2.result())
balance2.add_right(1)
print(balance2.result())