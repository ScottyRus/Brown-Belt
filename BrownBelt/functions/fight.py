# import sys

# sys.path.append(r'C:\Users\scott\Desktop\BrownBelt')

# from index import *

from copy import copy

import random

def fight(player, enemies, weapons):
    encounter = copy(random.choice(enemies))
    currentWeapon = weapons['shortsword']

    choice = ""

    print(f'You encountered a {encounter.name}!')

    while(player.health > 0 and encounter.health > 0):
        
        print('It\'s your turn!')
        print(f'Health: {player.health}')
        print('Options:')
        print(f'1. Choose weapon (Current: {currentWeapon.name})')
        print(f'2. Attack enemy')
        print('---')
        print(f'Enemy health: {encounter.health}')

        choice = input('')

        if(choice == '1'):
            print('What weapon would you like to choose?')
            print('(knife, shortsword, longsword)')
            choice = input('')
            if(not choice in weapons):
                print('Not a valid weapon')
            else:
                currentWeapon = weapons[choice]
        elif(choice == '2'):
            if(random.random() < 0.5 + (player.luck * 0.05)):
                totalDamage = currentWeapon.damage * (1 + player.strength * 0.1)
                encounter.health -= totalDamage
                print(f'Attack hit! {totalDamage} damage done')
                print(f'The enemy has {encounter.health} health left!')
            else:
                print('The attack missed!')
                    
    if(encounter.health > 0):
        print('The enemy attacked you!')
        if(random.random() < 0.5 - player.agility * 0.01):
            print('The attack missed!')
        else:
            print('The attack hit!')
            print(f'The enemy delt {encounter.damage} damage!')
            player.health -= encounter.damage
    else:
        print('Enemy defeated! You gained 2 skill points.')
        player.skillPoints += 2