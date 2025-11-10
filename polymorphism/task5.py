class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]
    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.table[row][col]
        else:
            return None
    def set_value(self, row, col, value):
        self.table[row][col] = value
    def n_rows(self):
        return self.rows
    def n_cols(self):
        return self.cols
tab1 = Table(3, 5)
tab1.set_value(0, 1, 10)
tab1.set_value(1, 2, 20)
tab1.set_value(2, 3, 30)
for i in range(tab1.n_rows()):
    for j in range(tab1.n_cols()):
        print(tab1.get_value(i, j), end=' ')
    print()
print()
tab2 = Table(2, 2)
for i in range(tab2.n_rows()):
    for j in range(tab2.n_cols()):
        print(tab2.get_value(i, j), end=' ')
    print()
print()
tab2.set_value(0, 0, 10)
tab2.set_value(0, 1, 20)
tab2.set_value(1, 0, 30)
tab2.set_value(1, 1, 40)
for i in range(tab2.n_rows()):
    for j in range(tab2.n_cols()):
        print(tab2.get_value(i, j), end=' ')
    print()
print()
for i in range(-1, tab2.n_rows() + 1):
    for j in range(-1, tab2.n_cols() + 1):
        print(tab2.get_value(i, j), end=' ')
    print()
print()
