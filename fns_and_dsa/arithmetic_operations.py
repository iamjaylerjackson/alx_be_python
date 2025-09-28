

num1 = 0.0
num2 = 0.0
operation = ""


def perform_operation(num1, num2, operation):

    match operation:
        case "add":
            return num1 + num1

        case "subtract":
            return num1 - num2

        case "multiply":
            return num1 * num2

        case "divide":
            if num2 == 0:
                return "Cannot be divded by zero"

            else:
                return num1 / num2
