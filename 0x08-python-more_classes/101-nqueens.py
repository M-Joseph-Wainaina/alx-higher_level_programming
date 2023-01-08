#!/usr/bin/python3
import sys

check_args()
value = 0

def check_args():
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        value = int(sys.argv[1])
    except (ValueError, TypeError):
        print('N must be a number')
        exit(1)
    if value < 4:
        print('N must be at least 4')
        exit(1)
    kkkk

def main(board_size):

    create_board(board_size)


def create_board(size):




