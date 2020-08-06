import random

set = ['rock', 'paper', 'scissors']


def cpu_choose():
    return random.choice(set)


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
