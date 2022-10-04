class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value + val >= 100:
            self.value = 100
            return self.value
        else:
            self.value += val
            return self.value


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)