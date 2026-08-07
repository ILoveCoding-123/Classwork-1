import math
import random

def calculate(operation: str, num1: float, num2: float = None) -> float:
    """
    Performs basic and advanced math operations with error handling.
    """
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return num1 / num2
        elif operation == "power":
            return math.pow(num1, num2)
        elif operation == "sqrt":
            if num1 < 0:
                raise ValueError("Cannot take square root of a negative number.")
            return math.sqrt(num1)
        elif operation == "random_range":
            return random.uniform(num1, num2)
        else:
            raise ValueError(f"Unknown operation: {operation}")

    except ZeroDivisionError as e:
        print(f"[Error] {e}")
        return None
    except ValueError as e:
        print(f"[Error] {e}")
        return None
    except TypeError:
        print("[Error] Missing required numbers for this operation.")
        return None
    except Exception as e:
        print(f"[Error] An unexpected error occurred: {e}")
        return None

# --- Interactive Terminal Loop ---
if __name__ == "__main__":
    print("=== Welcome to the Python Calculator ===")
    print("Available operations: add, subtract, multiply, divide, power, sqrt, random_range")
    print("Type 'exit' at any time to quit.")
    
    while True:
        try:
            print("\n" + "-"*30)
            op = input("Enter operation: ").strip().lower()
            if op == 'exit':
                print("Goodbye!")
                break
                
            if op not in ["add", "subtract", "multiply", "divide", "power", "sqrt", "random_range"]:
                print("[Error] Invalid operation. Please try again.")
                continue

            # Square root only needs one number
            if op == "sqrt":
                n1 = float(input("Enter number: "))
                result = calculate(op, n1)
            else:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))
                result = calculate(op, n1, n2)

            if result is not None:
                print(f"Result: {result}")

        except ValueError:
            print("[Error] Please enter valid numeric values.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break





