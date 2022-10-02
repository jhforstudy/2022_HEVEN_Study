class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val
        return self.value

class MaxLimitCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def add(self, val):
        self.value = super().add(val)
        if self.value >= 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)
