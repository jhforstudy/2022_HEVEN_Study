class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class MaxLimitCaculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCaculator()
cal.add(50)
cal.add(60)

print(cal.value)
