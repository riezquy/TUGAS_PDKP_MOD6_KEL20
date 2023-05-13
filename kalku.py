import math
#parent class kalkulator
class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate(self):
        pass

    def clear(self):
        self.numbers = None

    def get_numbers(self):
        return self.numbers

    def set_numbers(self, numbers):
        self.numbers = numbers

#child class kalkulator biasa
class BasicCalculator(Calculator):
    def __init__(self, numbers):
        super().__init__(numbers)

    def calculate(self, operator):
        result = 0
        if operator == "+":
            result = self.add()
        elif operator == "-":
            result = self.subtract()
        elif operator == "*":
            result = self.multiply()
        elif operator == "/":
            result = self.divide()
        else:
            print("Operator tidak dikenal")
        return result

    def add(self):
        result = 0
        for number in self.numbers:
            result += number
        return result

    def subtract(self):
        result = self.numbers[0]
        for i in range(1, len(self.numbers)):
            result -= self.numbers[i]
        return result

    def multiply(self):
        result = 1
        for number in self.numbers:
            result *= number
        return result

    def divide(self):
        result = self.numbers[0]
        for i in range(1, len(self.numbers)):
            if self.numbers[i] != 0:
                result /= self.numbers[i]
            else:
                print("Tidak dapat melakukan pembagian dengan nol")
                result = 0
                break
        return result

#child class kalkulator scientific
class ScientificCalculator(Calculator):
    def __init__(self, numbers):
        super().__init__(numbers)

    def calculate(self, operator):
        result = 0
        if operator == "+":
            result = self.add()
        elif operator == "-":
            result = self.subtract()
        elif operator == "*":
            result = self.multiply()
        elif operator == "/":
            result = self.divide()
        elif operator == "sqrt":
            result = self.square_root()
        elif operator == "^":
            result = self.power()
        elif operator == "!":
            result = self.factorial()
        else:
            print("Operator tidak dikenal")
        return result

    def square_root(self):
        return math.sqrt(self.numbers[0])

    def power(self):
        return math.pow(self.numbers[0], self.numbers[1])

    def factorial(self):
        num = int(self.numbers[0])
        result = 1
        for i in range(1, num+1):
            result *= i
        return result

# penggunaan kalkulator
print("=== Kalkulator Sederhana ===")
print("Pilih jenis kalkulator:")
print("1. Basic Calculator")
print("2. Scientific Calculator")
calculator_type = input("Jenis kalkulator yang dipilih (1/2): ")

if calculator_type == "1":
    numbers = list(map(float, input("Masukkan bilangan yang akan dihitung (pisahkan dengan spasi): ").split()))
    operator = input("Masukkan operator (+, -, *, /): ")
    basic_calculator = BasicCalculator(numbers)
    result = basic_calculator.calculate(operator)
    print("Hasil : ", result)

elif calculator_type == "2":
    numbers = list(map(float, input("Masukkan bilangan yang akan dihitung (pisahkan dengan spasi): ").split()))
    operator = input("Masukkan operator (sqrt,^,!) :")
    ScientificCalculator = ScientificCalculator(numbers)
    result = ScientificCalculator.calculate(operator)
    print("Hasil : ", result)