#stone paper seasior
import random
def play_game():
    choices = ['stone', 'paper', 'scissor']
    user_choice = input("Enter your choice (stone, paper, scissor): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please choose from stone, paper, or scissor.")
        return
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'stone' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")
if __name__ == "__main__":
    play_game()
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            play_game()
        elif play_again == 'no':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input! Please enter yes or no.")
            print("Invalid input! Please enter yes or no.")
            continue
            