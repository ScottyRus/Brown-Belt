import random

from classes.Player import Player
from classes.Enemy import Enemy
from classes.Weapon import Weapon
from functions.skillchoosing import skillChoose
from functions.fight import fight

player = Player('placeholder', 10, 1, 1, 1)

skills = {'strength', 'agility', 'luck'}

weapons = {'knife':Weapon('knife', 0.5, 2), 'shortsword':Weapon('shortsword', 1, 1), 'longsword':Weapon('longsword', 2, 0.5)}

enemies = [Enemy('spider', 5, 1), Enemy('zombie', 10, 3), Enemy('slaad', 15, 3)]

def startGame():
    player.username = input('What is your name? ')

    while True:
        skillChoose(player, skills)
        fight(player, enemies, weapons)

startGame()