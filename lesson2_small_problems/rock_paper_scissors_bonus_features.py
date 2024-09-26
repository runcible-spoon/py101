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

    # Return corresponding value for input's key
    return VALID_CHOICES[choice]

def is_choice_valid(choice):
    if choice in VALID_CHOICES:
        return True

    return False

def get_computer_choice():
    computer_choice = random.choice(list(VALID_CHOICES.values()))
    return computer_choice

def display_choices(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

def determine_outcome(player, computer):
    '''
    Based on player and computer inputs, return round outcome as
    win, loss, or tie for player
    '''
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
        return 'win'

    if ((player == "rock" and computer == "paper") or
        (player == "rock" and computer == "spock") or
        (player == "paper" and computer == "scissors") or
        (player == "paper" and computer == "lizard") or
        (player == "scissors" and computer == "rock") or
        (player == "scissors" and computer == "spock") or
        (player == "lizard" and computer == "scissors") or
        (player == "lizard" and computer == "rock") or
        (player == "spock" and computer == "lizard") or
        (player == "spock" and computer == "paper")):
        return 'loss'

    return 'tie'

def display_outcome(outcome):
    match outcome:
        case 'win':
            prompt("You win this round!")
        case 'loss':
            prompt("Computer wins this round!")
        case 'tie':
            prompt("This round's a tie!")



def keep_score(outcome, player_score, computer_score):
    '''
    Increment the score variables
    '''
    match outcome:
        case 'win':
            player_score += 1

        case 'loss':
            computer_score += 1
        case 'tie':
            pass
    return player_score, computer_score


def display_score(player, computer):
    prompt(f"You: {player} | Computer: {computer}")


def player_wins(score):
    '''
    Check if player has won
    '''
    if score == 3:
        return True

    return False

def computer_wins(score):
    '''
    Check if computer has won
    '''
    if score == 3:
        return True

    return False


def display_winner(player, computer):
    '''
    Display game's final outcome
    '''
    if computer_wins(computer):
        prompt("Computer won! Better luck next time.")
    if player_wins(player):
        prompt("You won! Way to go!")


def get_play_again_choice():
    '''
    After final score, ask if player wants to go again
    '''
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


def main():
    continue_game = True


    while continue_game is True:
        player_score = 0
        computer_score = 0

        # While neither the player nor the computer have 3 points:
        while(not player_wins(player_score)
              and not computer_wins(computer_score)):

            player_choice = get_player_choice()
            computer_choice = get_computer_choice()
            display_choices(player_choice, computer_choice)

            round_outcome = determine_outcome(player_choice, computer_choice)
            display_outcome(round_outcome)

            player_score, computer_score = keep_score(round_outcome,
                                                      player_score,
                                                      computer_score)

            display_score(player_score, computer_score)

        display_winner(player_score, computer_score)
        continue_game = get_play_again_choice()

    prompt("Thanks for playing!")

main()
