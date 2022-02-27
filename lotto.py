import random

start_game = input('Would you like to start the game? y/n  ')

while start_game == 'y':
    try:
        # Random set of numbers is generated. Set is used to overcome duplicate values
        winning_numbers = set()
        while len(winning_numbers) < 6:
            winning_numbers.add(random.randint(1, 50))

        # User enters their numbers
        choice = input('Enter your 6 numbers here, separated by a comma   ')
        choice_set = set(map(int, choice.split(',')))

        # Count number of matches in two sets
        if len(choice_set) == 6 and 0 < min(choice_set) and max(choice_set) <= 50:
            matches = 0
            for numbers in choice_set:
                if numbers in winning_numbers:
                    matches += 1
            print('Your lottery numbers are... {}.\nThe winning numbers are ... {}\n'
                  'You have matched {} numbers! Thank you for playing'
                  .format(sorted(choice_set), sorted(winning_numbers), matches))
                    # sorted returns a sorted sequence or collection the form of a list

        else:
            print('you must enter 6 unique numbers from 1 to 50')

    except ValueError:
        print('Please enter a list of 6 valid numbers to continue')

    start_game = input('\nWould you like to play another game? y/n   ')

else:
    print('Thank you for playing')


# -----------------------------------------------------------------------------------
#
#
#
#
# import random
#
# start_game = input('Would you like to start the game? y/n')
#
# while start_game == 'y':
#
#     # Random set of numbers is generated
#     winning_numbers = set()
#     while len(winning_numbers) < 6:
#         winning_numbers.add(random.randint(1, 50))
#
#     # User enters their numbers
#     players_numbers = set()
#     while len(players_numbers) < 6:
#         # try/except moved to the inside of the while loop to enable for loop to maintain the correct positions
#         try:
#             position = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
#             k = len(players_numbers)
#             choice = int(input('Please enter your {} number'.format(position[len(players_numbers)])))
#             if choice in range(1, 50) and choice not in players_numbers:
#                 players_numbers.add(choice)
#             else:
#                 print('Please enter a unique number between 0 and 50. Your {} numbers so far are {}'.format(len(players_numbers), players_numbers))
#         except ValueError:
#             print('Please enter a valid number to continue')
#     # Count number of matches in lists/sets
#     matches = 0
#     for number in players_numbers:
#         if number in winning_numbers:
#             matches += 1
#     print('Your lottery numbers are... {}.\n'
#           'The winning numbers are ... {}\n'
#           'You have matched {} numbers! Thank you for playing'
#           .format(sorted(players_numbers), sorted(winning_numbers), matches))
#     # sorted returns a sorted sequence or collection the form of a list
#     start_game = input('\nWould you like to start another game? y/n')
#
# else:
#     print('Thank you for playing')
#
