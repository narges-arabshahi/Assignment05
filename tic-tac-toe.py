import imp


import random
from colorama import Fore
import time


def show_game_board():
    for i in range(3):
        for j in range(3):
            print(Fore.GREEN + game[i][j],end=" ")
        print()
def check():
    if game[0][0]=='X' and game[0][1]=='X' and game[0][2]=='X':
        print(Fore.YELLOW + "Player 1 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][0]=='O' and game[0][1]=='O' and game[0][2]=='O':
        print(Fore.YELLOW + "Player 2 wins and Time is: " + str(time.time() - start_t))
        exit()
    if game[1][0]=='X' and game[1][1]=='X' and game[1][2]=='X':
        print(Fore.YELLOW + "Player 1 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[1][0]=='O' and game[1][1]=='O' and game[1][2]=='O':
        print(Fore.YELLOW + "Player 2 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[2][0]=='X' and game[2][1]=='X' and game[2][2]=='X':
        print(Fore.YELLOW + "Player 1 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[2][0]=='O' and game[2][1]=='O' and game[2][2]=='O':
        print(Fore.YELLOW + "Player 2 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][0]=='X' and game[1][0]=='X' and game[2][0]=='X':
        print(Fore.YELLOW + "Player 1 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][0]=='O' and game[1][0]=='O' and game[2][0]=='O':
        print(Fore.YELLOW + "Player 2 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][1]=='X' and game[1][1]=='X' and game[2][1]=='X':
        print(Fore.YELLOW + "Player 1 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][1]=='O' and game[1][1]=='O' and game[2][1]=='O':
        print(Fore.YELLOW + "Player 2 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][2]=='X' and game[1][2]=='X' and game[2][2]=='X':
        print(Fore.YELLOW + "Player 1 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][2]=='O' and game[1][2]=='O' and game[2][2]=='O':
        print(Fore.YELLOW + "Player 2 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][0]=='X' and game[1][1]=='X' and game[2][2]=='X':
        print(Fore.YELLOW + "Player 1 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][0]=='O' and game[1][1]=='O' and game[2][2]=='O':
        print(Fore.YELLOW + "Player 2 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][2]=='X' and game[1][1]=='X' and game[2][0]=='X':
        print(Fore.YELLOW + "Player 1 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][2]=='O' and game[1][1]=='O' and game[2][0]=='O':
        print(Fore.YELLOW + "Player 2 wins and time is: " + str(time.time() - start_t))
        exit()
    if game[0][0]!='-' and game[0][1]!='-'and game[0][2]!='-' and game[1][0]!='-' and game[1][1]!='-'and game[1][2]!='-' and game[2][0]!='-' and game[2][1]!='-'and game[2][2]!='-' :
        print(Fore.YELLOW + "Mosavi shodid and time is: " + str(time.time() - start_t)) 
        exit()  
    
   

game=[['-','-','-'],
      ['-','-','-'],
      ['-','-','-']]

show_game_board()
while True:
    x=int(input('Please enter 2 persons or 1 persons: '))
    if x ==2 or x==1:
        break
show_game_board()
while True:
    start_t=time.time()
    print(Fore.RED + "Player 1: ")
    while True:
        row=int(input("Please enter row: "))
        col=int(input("Please enter column: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col]=='-':
                game[row][col]= 'X'
                break
            else:
                print("cell is not empty")
        else:
            print("Index out of range,Try again!")
    show_game_board()
    check()
    print(Fore.BLUE + "Player 2")
    while True:
        if x==2:
            row=int(input("Please enter row: "))
            col=int(input("Please enter column: "))
        if x==1:
            print("system")
            row=random.randint(0,3)
            col=random.randint(0,3)
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col]=='-':
                game[row][col]='O'
                break
            else:
                print("cell is not empty")
        else:
            print("Index out of range,Try again!")
    show_game_board()
    check()
