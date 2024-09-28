'''
This version of Rock, Paper, Scissors includes two additional choices:
Lizard and Spock.

ROCK crushes SCISSORS, LIZARD
PAPER covers ROCK, disproves SPOCK
SCISSORS cut PAPER, LIZARD
LIZARD chews on PAPER, poisons SPOCK
SPOCK vaporizes ROCK, smashes SCISSORS

User is prompted to enter a choice. Computer then randomly selects 
from one of the five options, and a winner for the round is determined.

User and computer play to best three out of five rounds. 

Ties count toward the turn total and a tie final result is possible. 
'''

import random

def prompt(message):
    '''
    Distinguish computer messages from user input in terminal.
    '''
    print(f'==> {message}')

# Valid user inputs
VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock'
}

# Game logic
WINNING_COMBINATIONS = {
    'rock':     ['scissors',    'lizard'],
    'paper':    ['rock',        'spock'],
    'scissors': ['paper',       'lizard'],
    'lizard':   ['paper',       'spock'],
    'spock':    ['rock',        'scissors']
}

# INPUTS
def get_player_choice():
    prompt('Choose one: (r)ock, (p)aper, (sc)issors, (l)izard, (sp)ock')
    choice = input()

    while not is_choice_valid(choice):
        prompt("That's not a valid choice.")
        choice = input()

    # Return the value that corresponds to user input's key
    return VALID_CHOICES[choice]

def is_choice_valid(choice):
    if choice in VALID_CHOICES:
        return True
    return False

def get_computer_choice():
    computer_choice = random.choice(list(VALID_CHOICES.values()))
    return computer_choice


# ROUND OUTCOME
def display_choices(player_choice, computer_choice):
    prompt(f"You chose {player_choice}. The computer chose {computer_choice}.")

def player_wins_round(player_choice, computer_choice):
    return computer_choice in WINNING_COMBINATIONS[player_choice]

def display_round_outcome(player_choice, computer_choice):
    if player_wins_round(player_choice, computer_choice):
        prompt("You win this round!")
    elif player_choice == computer_choice:
        prompt("This round's a tie!")
    else:
        prompt("Computer wins this round!")

def adjust_score(player_choice, computer_choice, player_score, computer_score):
    '''
    Increment the score variables
    '''
    if player_wins_round(player_choice, computer_choice):
        player_score += 1
    elif player_choice == computer_choice:
        pass
    else:
        computer_score += 1
    return player_score, computer_score

def display_score(player_score, computer_score):
    prompt(f"SCORE: You: {player_score} | Computer: {computer_score}")

def display_turns(turns):
    prompt(f"ROUND: {turns}/5")


# GAME OUTCOME
def player_wins_game(player_score):
    return player_score >= 3

def computer_wins_game(computer_score):
    return computer_score >= 3

def display_winner(player_score, computer_score):
    '''
    Display game's final outcome.
    '''
    if computer_wins_game(computer_score) or computer_score > player_score:
        prompt("Computer won! Better luck next time.")
    elif player_wins_game(player_score) or player_score > computer_score:
        prompt("You won! Way to go!")
    else:
        prompt("Tie! Try again.")


# PLAY AGAIN?
def get_play_again_choice():
    '''
    After final score, ask if player wants to go again.
    '''
    prompt("Do you want to play again? (y/n)")
    answer = input().lower()

    while not answer or answer not in ['y', 'n']:
        prompt("That's not a valid choice.")
        answer = input().lower()

    match answer:
        case 'y':
            return True
        case 'n':
            return False


# MAIN
def game():
    continue_game = True

    while continue_game is True:
        turns = 1
        player_score = 0
        computer_score = 0
        prompt("%====================================================%")
        prompt("|  WELCOME TO ROCK, PAPER, SCISSORS, LIZARD, SPOCK!  |")
        prompt("%====================================================%")

        prompt('''
                           RULES:
               ROCK crushes SCISSORS, LIZARD
               PAPER covers ROCK, disproves SPOCK
               SCISSORS cut PAPER, LIZARD
               LIZARD chews on PAPER, poisons SPOCK
               SPOCK vaporizes ROCK, smashes SCISSORS
               ''')

        while(not player_wins_game(player_score)
              and not computer_wins_game(computer_score)
              and turns <= 5):

            player_choice = get_player_choice()
            computer_choice = get_computer_choice()
            display_choices(player_choice, computer_choice)
            display_round_outcome(player_choice, computer_choice)

            player_score, computer_score = adjust_score(player_choice,
                                                        computer_choice,
                                                        player_score,
                                                        computer_score)

            display_score(player_score, computer_score)
            display_turns(turns)
            turns += 1

        display_winner(player_score, computer_score)
        continue_game = get_play_again_choice()

    prompt("Thanks for playing!")

game()
