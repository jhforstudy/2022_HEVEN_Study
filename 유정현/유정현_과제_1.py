class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100

if __name__ == "__main__":
    cal = MaxLimitCalculator()
    cal.add(50)
    print(cal.value)
    cal.add(60)
    print(cal.value)