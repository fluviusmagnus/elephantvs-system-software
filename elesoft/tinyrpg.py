#!/usr/bin/env python
#coding: UTF-8
from __future__ import print_function
from random import random

COL = 20
ROW = 10
world = [\
    ['.','H','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','H','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','H','.'],\
    ['.','H','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','F']\
    ]
world_showed = [[False for col in range(COL)] for row in range(ROW)] 
p_row = 3
p_col = 3
p_type = 'H'
hp = 2

def reset():
    global COL, ROW, p_row, p_col, p_type, hp, world, world_showed
    COL = 20
    ROW = 10
    world = [\
    ['.','H','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','H','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','H','.'],\
    ['.','H','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','H','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','H','.','.','.','.','.','.'],\
    ['.','.','.','.','.','.','.','.','H','.','.','.','.','.','.','.','.','.','.','F']\
    ]
    world_showed = [[False for col in range(COL)] for row in range(ROW)] 
    p_row = 3
    p_col = 3
    p_type = 'H'
    hp = 2

def print_world():
    for w_row in range(ROW):
        for w_col in range(COL):
            if p_row == w_row and p_col == w_col:
                print('@', end='')
            elif world_showed[w_row][w_col]:
                print(world[w_row][w_col], end='')
            else:
                print('?', end='')
        print()
        
def print_world_debug():
    for w_row in range(ROW):
        for w_col in range(COL):
#            if p_row == w_row and p_col == w_col:
#                print('@', end='')
#            elif world_showed[w_row][w_col]:
                print(world[w_row][w_col], end='')
#            else:
#                print('?', end='')
        print()
        
def move(direction):
    global p_col, p_row, hp
    if direction == 'h':
        p_col = p_col - 1
    elif direction == 'l':
        p_col = p_col + 1
    elif direction == 'j':
        p_row = p_row + 1
    else:
        p_row = p_row - 1
    p_col = p_col % COL
    p_row = p_row % ROW
    hp = hp - 0.1
    refresh()
    do_pos()
    
def do_pos():
    global hp
    if p_type == 'H':
        print('Oasis! HP +2. ')
        hp = hp + 2
        if hp >= 5:
            hp = 5
            print('HP max reached. ')
        print('HP: ' + str(hp))
        world[p_row][p_col] = 'O'
    elif p_type == 'O':
        print('Nothing left here. \nBut free from monster attack. ')
    elif random() < 0.02:
        print('Bomb. HP -3. ')
        hp = hp - 3
        print('HP: ' + str(hp))
    elif random() < 0.35:
        print('Monster appears. HP -1. ')
        hp = hp - 1
        print('HP: ' + str(hp))

def make_sight():
    for w_row in range(ROW):
        for w_col in range(COL):
            if abs(w_row - p_row) + abs(w_col - p_col) <=2:
                world_showed[w_row][w_col] = True
def refresh():
    global p_type
    p_type = world[p_row][p_col]
    make_sight()
    print_world()
    print('POS: ' + p_type + '\t' + 'HP: ' + str(hp))

def check_input(input_string):
    valid_input = ['h', 'j', 'k', 'l', 'q', 'c']
    if input_string == '':
        return False
    elif input_string[0] in valid_input:
        return True
    else:
        return False


# Main loop starts here
def run():
    reset()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('TinyRPG\n\n\
by Tianhu Zhang <zszth@126.com>\n\
Commands: h, j, k, l to move;\n\
          q to quit.\n\
Goal:     to find the flag F\n')
    refresh()
    cmd = 'EMPTY'
    while cmd[0] != 'q' and p_type != 'F' and hp > 0:
        cmd = raw_input('Enter command: ')
        print()
        if check_input(cmd):
            if cmd[0] in ['h', 'j', 'k', 'l']:
                move(cmd[0])
            if cmd == 'cheat':
                print_world_debug()
        else:
            print("Invalid command!")
            cmd = 'EMPTY'

    # Quit status check
    if cmd[0] == 'q':
        print('Give up. Exit. ')
    elif p_type == 'F':
        print('End. You WIN. ')
    elif hp <= 0: 
        print('You DIE. Game over. ')
