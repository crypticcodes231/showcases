import math

def calc():
    print("== Simple Scientific Calculator ==")
    print("Type: +, -, *, /, ^, sin, cos, tan, log, sqrt, fact")
    print("Type 'exit' to quit")

    while True:
        op = input("\nEnter operation: ").lower().strip()

        if op == 'exit':
            print("Alright, peace out. Calculator shutting down.")
            break

        try:
            if op in ['+', '-', '*', '/', '^']:
                a = float(input("First number? "))
                b = float(input("Second number? "))

                if op == '+':
                    print("Result:", a + b)
                elif op == '-':
                    print("Result:", a - b)
                elif op == '*':
                    print("Result:", a * b)
                elif op == '/':
                    if b == 0:
                        print("Dude. Dividing by zero? Not today.")
                    else:
                        print("Result:", a / b)
                elif op == '^':
                    print("Result:", a ** b)

            elif op in ['sin', 'cos', 'tan']:
                angle = float(input("Angle in degrees, please: "))
                rad = math.radians(angle)
                if op == 'sin':
                    print("Result:", math.sin(rad))
                elif op == 'cos':
                    print("Result:", math.cos(rad))
                elif op == 'tan':
                    print("Result:", math.tan(rad))

            elif op == 'log':
                num = float(input("Gimme a positive number for log: "))
                if num <= 0:
                    print("Nope. Logarithms don't like zero or negatives.")
                else:
                    print("Result:", math.log10(num))

            elif op == 'sqrt':
                num = float(input("Non-negative number for square root: "))
                if num < 0:
                    print("Can't do square roots of negative numbers. Not in this universe.")
                else:
                    print("Result:", math.sqrt(num))

            elif op == 'fact':
                num = int(input("Non-negative integer for factorial: "))
                if num < 0:
                    print("Negative factorial? That's not a thing, sorry.")
                else:
                    print("Result:", math.factorial(num))

            else:
                print("I have no idea what that operation is. Wanna try again?")

        except ValueError:
            print("Whoa, something went wrong. Numbers only, alright?")

if __name__ == "__main__":
    calc()