import es1 as calc

class NewCalculator:

    def __init__(self):
        pass

    def sum(self, m, n):
        return calc.sum(m,n)

    def divide(self, m, n):
        return calc.divide(m,n)

    def multiply(self, m, n):
        return calc.multiply(m,n)

    def MCD(self, m, n):
        return calc.MCD(m,n)


obj = NewCalculator()
print("EXPECTED: 5 - OBTAINED: ", obj.sum(2,3))
print("EXPECTED: -7 - OBTAINED: ", obj.sum(-10,3))
print("EXPECTED: -4 - OBTAINED: ", obj.divide(-12, 2))
print("EXPECTED: 6 - OBTAINED: ", obj.divide(30, 5))
print("EXPECTED: 8 - OBTAINED: ", obj.multiply(2,4))
print("EXPECTED: 16 - OBTAINED: ", obj.multiply(-4,-4))
print("EXPECTED: 8 - OBTAINED: ", obj.MCD(3562464, 859432))
