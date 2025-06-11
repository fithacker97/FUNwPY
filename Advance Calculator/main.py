from calculator.core import evaluate_expression, show_history, help_menu

def main():
    print("🔢 Welcome to Advanced Python Calculator")
    print("Type 'help' to see available operations\n")

    while True:
        user_input = input(">>> ")

        if user_input.lower() in ['exit', 'quit']:
            print("👋 Exiting calculator. Goodbye!")
            break
        elif user_input.lower() == "help":
            print(help_menu())
        elif user_input.lower() == "history":
            for entry in show_history():
                print(entry)
        else:
            result = evaluate_expression(user_input)
            print(f"= {result}")

if __name__ == "__main__":
    main()