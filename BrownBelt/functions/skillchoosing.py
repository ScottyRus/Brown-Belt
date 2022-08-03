# import sys

# sys.path.append(r'C:\Users\scott\Desktop\BrownBelt')

# import index

def skillChoose(player, skills):
    choice = ""

    while choice != 'c':
        print("---")
        print(f'Skill points to spend: {player.skillPoints}')
        print('Skills:')
        print(f'Strength: {player.strength} (Strength of hit)')
        print(f'Agility: {player.agility} (Likelihood to dodge)')
        print(f'Luck: {player.luck} (Likelihood to hit)')

        choice = input('Choose category to add or remove skill point from, or input c to continue. ').lower()

        if(choice in skills):
            stat = getattr(player, choice)

            addRemove = input('Add or remove skill point? a/r ').lower()

            if(addRemove == 'a'):
                if(player.skillPoints >= 1):
                    setattr(player, choice, stat + 1)
                    player.skillPoints -= 1
                else:
                    print('No skills points available')
            elif(addRemove == 'r'):
                if(stat > 1):
                    setattr(player, choice, stat - 1)
                    player.skillPoints += 1
                else:
                    print('Already minimum stat')
        elif(choice == 'c'):
            print('')
        else:
            print('Not a valid option')