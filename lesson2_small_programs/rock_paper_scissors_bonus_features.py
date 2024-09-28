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
import os

def prompt(message):
    '''
    Distinguish computer messages from user input in terminal.
    '''
    print(f'==> {message}')

def display_welcome_message():
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

# Constants
TOTAL_ROUNDS = 5
WINNING_SCORE = 3

# INPUTS
def get_player_choice():
    prompt('Choose one: (r)ock, (p)aper, (sc)issors, (l)izard, (sp)ock')
    choice = input().lower()

    while not is_choice_valid(choice):
        prompt("That's not a valid choice.")
        choice = input().lower()

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
    player_win_outcome = player_wins_round(player_choice, computer_choice)
    if player_win_outcome:
        player_score += 1
    elif not player_win_outcome:
        computer_score += 1
    return player_score, computer_score

def display_score(player_score, computer_score):
    prompt(f"SCORE: You: {player_score} | Computer: {computer_score}")

def display_turns(turns):
    prompt(f"ROUND: {turns}/{TOTAL_ROUNDS}")


# GAME OUTCOME
def has_game_ended(player_score, computer_score, turns):
    '''
    Checks whether either agent has the minimum winning score,
    and if no. of turns is less than or equal to max (5).
    '''
    return( not agent_wins_game(player_score)
              and not agent_wins_game(computer_score)
              and turns <= TOTAL_ROUNDS)

def agent_wins_game(score):
    '''
    True if agent has won, False if not.
    '''
    return score >= WINNING_SCORE

def display_winner(player_score, computer_score):
    '''
    Display game's final outcome.
    '''
    if agent_wins_game(computer_score) or computer_score > player_score:
        prompt("Computer won! Better luck next time.")
    elif agent_wins_game(player_score) or player_score > computer_score:
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
    display_welcome_message()

    while continue_game:
        turns = 1
        player_score = 0
        computer_score = 0
        

        while(has_game_ended()):
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
        
        os.system('clear')

    prompt("Thanks for playing!")

game()
