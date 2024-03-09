import random

computer = 0
player = 0

def game(player_choice):
    global computer
    global player

    options = ['rock', 'paper', 'sci']
    computer_choice = random.choice(options)
    print(f'Computer chooses {computer_choice}.')

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'sci') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'sci' and computer_choice == 'paper'):
        player += 1
        return "You win!"
    else:
        computer += 1
        return "You lose!"

def main():
    global computer
    global player

    print("Let's play Rock, Paper, Scissors!")
    while True:
        player_choice = input("Enter your choice (rock, paper, sci) or 'quit' to exit: ").lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            print(f"Final score - Player: {player}, Computer: {computer}")
            break
        elif player_choice not in ['rock', 'paper', 'sci']:
            print("Invalid choice. Please try again.")
            continue

        result = game(player_choice)
        print(result)

if __name__== "__main__":
    True
