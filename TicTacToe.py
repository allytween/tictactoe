#! /usr/bin/env python3
# M. Tween
# 11/2/19
# This game lets you play tic-tac-toe!

# extra functions I would like to add:
# play against computer
# in bounds checking

import time
from random import randint
# from colorama import Fore, Back, Style

# want to add colours later!

# Here come the constants!
BANNER = '======================================================\n'
WELCOME = 'Welcome to the fabulous Tic-Tac-Toe Game!\n'
BOARD_LAYOUT_STR = 'The board layout is as follows:\n'
BOARD_LAYOUT_DESIGN = '-----\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n-----\n'
RULES = 'The first player to create a line of 3 Xs or Os wins!\nGood luck!\n'
NEW_GAME = 'New game!\n'
NOT_VALID = 'Your choice is invalid! Please choose a number between 1 and 9 to represent spaces on the board!'
OCCUPIED = 'This space is already occupied! Please choose another space:'
CONGRATULATIONS = 'Congrats! {} wins!'
MOVING = 'Moving...\n'
NO_WINNER = 'Sorry, no winner yet!\n======================================================\n'
PLAY_AGAIN = 'Would you like to play again? Type "y" to continue or "n" to exit'
PLAYING = 'Okay, playing again!\n======================================================\n'
GOODBYE = 'Okay, goodbye!'


# This module prints out the tic-tac-toe board
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print()


# end module


# This module spits out a welcome message
def welcome():
    print(BANNER + WELCOME + BANNER)
    print(BOARD_LAYOUT_STR + BOARD_LAYOUT_DESIGN)
    print(RULES + BANNER)
    print()


# end module


# This module is for playing against a computer
def computerMove():
    return str(randint(1, 9))


# end module


# This module checks to see if it's a valid move
def checkMove(board, move):
    if board[move] == ' ':
        print(MOVING)
        time.sleep(2)
        return True
    else:
        print(OCCUPIED)
        return False


# end module


# This module checks to see if you've won!
def checkWin(board, t):
    if ((board['7'] == t and board['8'] == t and board['9'] == t) or
            (board['4'] == t and board['5'] == t and board['6'] == t) or
            (board['1'] == t and board['2'] == t and board['3'] == t) or
            (board['8'] == t and board['5'] == t and board['2'] == t) or
            (board['9'] == t and board['6'] == t and board['3'] == t) or
            (board['7'] == t and board['4'] == t and board['1'] == t) or
            (board['7'] == t and board['5'] == t and board['3'] == t) or
            (board['9'] == t and board['5'] == t and board['1'] == t)):
        printBoard(board)
        print(CONGRATULATIONS.format(t))
        playAgain()
        play()
    else:
        print(NO_WINNER)
        return t


# end module


# This module asks you if you want to play again after a win
def playAgain():
    print(PLAY_AGAIN)
    choice = input()
    if choice == 'y':
        print(PLAYING)
        return True
    else:
        print(GOODBYE)
        exit()


# end module


# This module plays the game
def play():
    theBoard = {'1': ' ', '2': ' ', '3': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '7': ' ', '8': ' ', '9': ' '}
    # variable to set who's turn it is
    turn = 'X'
    # getting the greeting
    print(NEW_GAME)
    # actually playing the game
    while True:
        printBoard(theBoard)
        print('It\'s {}\'s turn. Please choose a space:'.format(turn))

        # getting move from the user or computer
        # depending on who's turn it is
        if turn == 'O':
            move = computerMove()
            print(move)
        else:
            move = input()

        # checking the input to see if it is valid
        while True:
            if not move.isdigit():
                print(NOT_VALID)
                move = input()
            elif int(move) < 1 or int(move) > 9:
                print(NOT_VALID)
                move = input()
            else:
                break

        # checking the board to see if the move is valid
        if not checkMove(theBoard, move):
            continue
        theBoard[move] = turn

        # checking for a winner
        checkWin(theBoard, turn)

        # next player's turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    # print("OH MY GOD! HELLO THIS IS OUTSIDE THE LOOP") # debug!


# end module


# This module is the main module
def main():
    welcome()
    play()


# end module


# This module is the main module check
if __name__ == "__main__":
    main()
# end program!
