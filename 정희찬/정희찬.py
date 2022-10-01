class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, value):
        self.value += value

class MaxLimitCalculator(Calculator):
    def __init__(self):
        self.value = 0

    def add(self, value):
        super().add(value)

        if self.value >= 100:
            self.value = 100




cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

