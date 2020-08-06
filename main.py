import random
import os

set = ['rock', 'paper', 'scissors']


def cpu_choose():
    cpu_choice = random.choice(set)
    print("CPU chose: {}".format(cpu_choice))
    return cpu_choice


def player_choose():
    player_choice = input("Choose rock, paper or scissors: ")
    print("You chose: {}".format(player_choice))
    return player_choice


def check_win(p_choice, cpu_choice):
    if p_choice == cpu_choice:
        print("It's a draw!")
    elif p_choice == 'rock':
        if cpu_choice == 'scissors':
            print("Player has won!")
        else:
            print("CPU has won!")
    elif p_choice == 'paper':
        if cpu_choice == 'rock':
            print("Player has won!")
        else:
            print("CPU has won!")
    elif p_choice == 'scissors':
        if cpu_choice == 'paper':
            print("Player has won!")
        else:
            print("CPU has won!")
    else:
        print("Invalid input!")


def main():
    while True:
        check_win(player_choose(), cpu_choose())


if __name__ == '__main__':
    main()
