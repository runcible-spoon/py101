import random

def prompt(message):
    print(f'==> {message}')

VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard', 
    'sp': 'spock'
}


def get_player_choice():
    prompt('Choose one: (r)ock, (p)aper, (sc)issors, (l)izard, (sp)ock')
    choice = input()

    while not is_choice_valid(choice):
        prompt("That's not a valid choice.")
        choice = input()
   
   # Return the value to input's key
    return VALID_CHOICES[choice]

def is_choice_valid(choice):
    if choice in VALID_CHOICES.keys():
        return True
    
    return False


def get_computer_choice():
    computer_choice = random.choice(list(VALID_CHOICES.values()))
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

    while not answer or answer[0] not in ['y', 'n']:
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
