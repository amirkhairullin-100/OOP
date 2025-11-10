class Table:
    def __init__(self, rows, cols):
        self._table = [[0] * cols for _ in range(rows)]
    def n_rows(self):
        return len(self._table)
    def n_cols(self):
        if not self._table:
            return 0
        return len(self._table[0])
    def get_value(self, row, col):
        if 0 <= row < self.n_rows() and 0 <= col < self.n_cols():
            return self._table[row][col]
        return None
    def set_value(self, row, col, value):
        self._table[row][col] = value
    def delete_row(self, row):
        del self._table[row]
    def delete_col(self, col):
        for row_list in self._table:
            del row_list[col]
    def add_row(self, row):
        new_row = [0] * self.n_cols()
        self._table.insert(row, new_row)
    def add_col(self, col):
        n_rows_current = self.n_rows()
        for i in range(n_rows_current):
            self._table[i].insert(col, 0)
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
tab.add_row(1)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
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
tab2.add_row(0)
tab2.add_col(1)
for i in range(-1, tab2.n_rows() + 1):
    for j in range(-1, tab2.n_cols() + 1):
        print(tab2.get_value(i, j), end=' ')
    print()
print()
tab3 = Table(1, 1)
for i in range(tab3.n_rows()):
    for j in range(tab3.n_cols()):
        print(tab3.get_value(i, j), end=' ')
    print()
print()
tab3.set_value(0, 0, 1000)
for i in range(tab3.n_rows()):
    for j in range(tab3.n_cols()):
        print(tab3.get_value(i, j), end=' ')
    print()
print()
for i in range(-1, tab3.n_rows() + 1):
    for j in range(-1, tab3.n_cols() + 1):
        print(tab3.get_value(i, j), end=' ')
    print()
print()
tab3.add_row(0)
tab3.add_row(2)
tab3.add_col(0)
tab3.add_col(2)
tab3.set_value(0, 0, 2000)
tab3.set_value(0, 2, 3000)
tab3.set_value(2, 0, 4000)
tab3.set_value(2, 2, 5000)
for i in range(-1, tab3.n_rows() + 1):
    for j in range(-1, tab3.n_cols() + 1):
        print(tab3.get_value(i, j), end=' ')
    print()
print()