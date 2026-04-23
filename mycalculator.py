import math
import sys


class UserInteractions:
    def __init__(self, math_operations):
        self.numbers = []
        self.math = math_operations

    def gather_user_input(self):
        while True:
            try:
                n = float(input("Please enter a number: "))
                self.numbers.append(n)
                break
            except ValueError:
                print("Invalid Entry")

    def quit(self):
        print("Exiting Program")
        sys.exit()

    def menu(self):
        second_input_responses = ["1", "2", "3", "4", "5"]

        while True:
            self.numbers.clear()
            self.gather_user_input()
            print("""\nPlease select an option: 
                    1. Addition
                    2. Subtraction
                    3. Multiplicaiton
                    4. Division
                    5. Exponents
                    6. Square
                    7. Square Root
                    8. Start Over
                    9. Exit Program
            """)

            user_option = input()

            if user_option in second_input_responses:
                self.gather_user_input()

            actions = {
                "1": self.math.addition,
                "2": self.math.subtraction,
                "3": self.math.multiplication,
                "4": self.math.division,
                "5": self.math.exponents,
                "6": self.math.square_value,
                "7": self.math.square_root,
                "9": self.quit,
            }

            if user_option == "8":
                continue
            elif user_option == "9":
                self.quit()
            elif user_option in actions:
                actions[user_option](self.numbers)
            else:
                print("Invalid Selection")
            print(f"Result: {self.math.final_value}")


class MathOperations:
    def __init__(self):
        self.final_value = 0

    def addition(self, numbers):
        self.final_value = numbers[0] + numbers[1]
        return self.final_value

    def subtraction(self, numbers):
        self.final_value = numbers[0] - numbers[1]
        return self.final_value

    def multiplication(self, numbers):
        self.final_value = numbers[0] * numbers[1]
        return self.final_value

    def division(self, numbers):
        if numbers[1] != 0:
            self.final_value = numbers[0] / numbers[1]
            return self.final_value
        else:
            raise ZeroDivisionError("Cannot divide by zero")

    def exponents(self, numbers):
        self.final_value = numbers[0] ** numbers[1]
        return self.final_value

    def square_value(self, number):
        self.final_value = number[0] * number[0]
        return self.final_value

    def square_root(self, number):
        if number[0] >= 0:
            self.final_value = math.sqrt(number[0])
            return self.final_value
        else:
            raise ValueError("Cannot take the square root of a negative number")


def main(): # pragma: no cover
    math = MathOperations()
    ui = UserInteractions(math)

    ui.menu()


if __name__ == "__main__": # pragma: no cover
    main()
