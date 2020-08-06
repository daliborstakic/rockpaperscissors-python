import random
import os
from colorama import init
from termcolor import colored

init()

set = ['rock', 'paper', 'scissors']


def cpu_choose():
    cpu_choice = random.choice(set)
    print("CPU chose: {}".format(cpu_choice))
    return cpu_choice


def player_choose():
    player_choice = input("Choose rock, paper or scissors: ")
    print("You chose: {}".format(player_choice))
    return player_choice


def player_won():
    print(colored('Player has won!', 'green'))


def cpu_won():
    print(colored('CPU has won!', 'red'))


def check_win(p_choice, cpu_choice):
    if p_choice == cpu_choice:
        print(colored("It's a draw!", 'yellow'))
    elif p_choice == 'rock':
        if cpu_choice == 'scissors':
            player_won()
        else:
            cpu_won()
    elif p_choice == 'paper':
        if cpu_choice == 'rock':
            player_won()
        else:
            cpu_won()
    elif p_choice == 'scissors':
        if cpu_choice == 'paper':
            player_won()
        else:
            cpu_won()
    else:
        print("Invalid input!")


def main():
    while True:
        check_win(player_choose(), cpu_choose())


if __name__ == '__main__':
    main()
