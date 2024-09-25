import random

def prompt(message):
    print(f'==> {message}')

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def get_player_choice():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        choice = input()

    return choice

def get_computer_choice():
    computer_choice = random.choice(VALID_CHOICES)
    return computer_choice

def display_choices(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

def display_game_outcome(player, computer):
    if ((player == "rock" and computer == "scissors") or
        (player == "rock" and computer == "lizard") or
        (player == "paper" and computer == "rock") or
        (player == "paper" and computer == "spock") or
        (player == "scissors" and computer == "paper") or
        (player == "scissors" and computer == "lizard") or
        (player == "lizard" and computer == "spock") or
        (player == "spock" and computer == "rock") or
        (player == "lizard" and computer == "paper") or
        (player == "spock" and computer == "scissors")):
        prompt("You win!")
    elif((player == "rock" and computer == "paper") or
        (player == "rock" and computer == "spock") or
        (player == "paper" and computer == "scissors") or
        (player == "paper" and computer == "lizard") or
        (player == "scissors" and computer == "rock") or
        (player == "scissors" and computer == "spock") or
        (player == "lizard" and computer == "scissors") or
        (player == "lizard" and computer == "rock") or
        (player == "spock" and computer == "lizard") or
        (player == "spock" and computer == "paper")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def get_play_again_choice():
    prompt("Do you want to play again? (y/n)")
    answer = input().lower()

    while answer and answer[0] not in ['y', 'n']:
        prompt("That's not a valid choice.")
        answer = input().lower()

    match answer:
        case 'y':
            return True
        case 'n':
            return False


def game():
    continue_game = True
    while continue_game == True:
        player = get_player_choice()
        computer = get_computer_choice()

        display_choices(player, computer)
        display_game_outcome(player, computer)

        continue_game = get_play_again_choice()
    
game()
