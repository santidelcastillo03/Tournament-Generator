from app import *


def main():
    participant_list = []
    while True:
        option = input('Choose an option:\n1 - Add a participant\n2 - Generate tournament\n3 - Exit\n\n-->')
        if option == '1':
            add_participant(participant_list)

        elif option == '2':
            generate_tournament(participant_list)

        elif option == '3':
            break

        else:
            print('Invalid option')


main()
