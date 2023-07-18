import random
from participant import Participant


def show_participants(participant_list):
    for index, participant in enumerate(participant_list):
        print(f'{index + 1} - {participant.name}')


def add_participant(participant_list):
    while True:
        add = input('Enter the name of the participant:\n\n-->').title()
        participant_list.append(Participant(add))
        option = input('Do you want to add another participant? (y/n)').lower()
        if option == 'y':
            continue
        elif option == 'n':
            break
        else:
            print('Invalid option')
    show_participants(participant_list)


def generate_tournament(participant_list):
    if len(participant_list) < 4:
        print('Not enough participants to generate a tournament')
    else:
        random.shuffle(participant_list)
        print('Tournament generated!')
        for index in range(0, len(participant_list), 2):
            try:
                print(f'{participant_list[index].name} vs {participant_list[index + 1].name}')
            except IndexError:
                print(f'{participant_list[index].name} has no opponent')


