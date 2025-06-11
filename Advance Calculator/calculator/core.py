import math

history = []

def evaluate_expression(expr):
    try:
        result = eval(expr, {"__builtins__": {}}, math.__dict__)
        history.append(f"{expr} = {result}")
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception:
        return "Error: Invalid expression"

def show_history():
    return history if history else ["No calculations yet."]

def help_menu():
    return """
Available Operations:
  ➕  Addition           → 2 + 3
  ➖  Subtraction        → 10 - 4
  ✖️  Multiplication      → 5 * 6
  ➗  Division           → 8 / 2
  🔢  Power              → pow(2, 3)
  🌀  Square Root        → sqrt(16)
  🔁  Modulo             → 10 % 3

Other Commands:
  history   → Show all previous calculations
  help      → Show this help menu
  exit      → Exit the calculator
"""