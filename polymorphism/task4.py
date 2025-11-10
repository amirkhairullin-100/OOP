class MinStat:
    def __init__(self):
        self.min_val = None
    def add_number(self, number):
        if self.min_val is None or number < self.min_val:
            self.min_val = number
    def add_array(self, arr):
        for num in arr:
            self.add_number(num)
    def result(self):
        return self.min_val
class MaxStat:
    def __init__(self):
        self.max_val = None
    def add_number(self, number):
        if self.max_val is None or number > self.max_val:
            self.max_val = number
    def add_array(self, arr):
        for num in arr:
            self.add_number(num)
    def result(self):
        return self.max_val
class AverageStat:
    def __init__(self):
        self.sum = 0
        self.count = 0
    def add_number(self, number):
        self.sum += number
        self.count += 1
    def add_array(self, arr):
        for num in arr:
            self.add_number(num)
    def result(self):
        if self.count == 0:
            return None
        return self.sum / self.count
arr1 = [1, 2, 4, 5]
arr2=[]
arr3 = [1, 0, 0]
min_stat1 = MinStat()
max_stat1 = MaxStat()
avg_stat1 = AverageStat()
min_stat2 = MinStat()
max_stat2 = MaxStat()
avg_stat2 = AverageStat()
min_stat3 = MinStat()
max_stat3 = MaxStat()
avg_stat3 = AverageStat()
min_stat1.add_array(arr1)
max_stat1.add_array(arr1)
avg_stat1.add_array(arr1)
min_stat2.add_array(arr2)
max_stat2.add_array(arr2)
avg_stat2.add_array(arr2)
min_stat3.add_array(arr3)
max_stat3.add_array(arr3)
avg_stat3.add_array(arr3)
print(min_stat1.result(), max_stat1.result(), '{:<05.3}'.format(avg_stat1.result()))
print(min_stat2.result(), max_stat2.result(), avg_stat2.result())
print(min_stat3.result(), max_stat3.result(), '{:<05.3}'.format(avg_stat3.result()))
