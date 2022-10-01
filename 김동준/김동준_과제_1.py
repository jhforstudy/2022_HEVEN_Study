from logging.config import valid_ident


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val

        if self.value >= 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)