import math

class Calculator:
    def __init__(self):
        self.operations = {
            '1': self.addition,
            '2': self.substraction,
            '3': self.multiplication,
            '4': self.division,
            '5': self.square_root,
            '6': self.logarithm,
            '7': self.trigonometric_functions
        }

    def start(self):
        print("Welcome to the Calculator !")

        while True:
            print("\nChoose one of the operations: ")
            for key, value in self.operations.items():
                print(f"{key}. {value.__doc__}")
            print("8. Quit")

            choice = input("Enter your choice (1 - 8): ")

            if choice == '8':
                print("Exiting the system....")
                break
            elif choice in self.operations:
                self.operations[choice]()
            else:
                print("Invalid choice. Please enter valid choice!")

    def addition(self):
        """Addition"""
        number1 = float(input("Enter the first number : "))
        number2 = float(input("Enter the second number : "))
        result = number1 + number2
        print(f"Result: {number1} + {number2} = {result}")

    def substraction(self):
        """Substraction"""
        number1 = float(input("Enter the first number : "))
        number2 = float(input("Enter the second number : "))
        result = number1 - number2
        print(f"Result: {number1} - {number2} = {result}")

    def multiplication(self):
        """Multiplication"""
        number1 = float(input("Enter the first number : "))
        number2 = float(input("Enter the second number : "))
        result = number1 * number2
        print(f"Result: {number1} * {number2} = {result}")

    def division(self):
        """Division"""
        number1 = float(input("Enter the first number : "))
        number2 = float(input("Enter the second number : "))
        if number2 == 0:
            print("Error. Division by zero")
        else:
            result = number1 / number2
            print(f"Result: {number1} / {number2} = {result}")

    def square_root(self):
        """Square root"""
        number = float(input("Enter the number : "))
        result = math.sqrt(number)
        print(f"Square root of {number} is {result}")

    def logarithm(self):
        """Logarithm"""
        number = float(input("Enter the number : "))
        result = math.log(number)
        print(f"Logarithm of {number} is {result}")

    def trigonometric_functions(self):
        """Trigonometric functions"""
        number = float(input("Enter the number : "))
        angle_radian = math.radians(number)

        trig_elements = {
            '1': ('Sine', math.sin),
            '2': ('Cosine', math.cos),
            '3': ('Tangent', math.tan)
        }
        print("\nChoose a trigonometric elements : ")
        for key, value in trig_elements.items():
            print(f"{key}. {value[0]}")
        trig_choice = input("Enter your choice please : ")

        if trig_choice in trig_elements:
            result = trig_elements[trig_choice][1](angle_radian)
            print(f"{trig_elements[trig_choice][0]} of {number}° is {result}")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.start()
