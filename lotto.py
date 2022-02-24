import random

start_game = input('Would you like to start the game? y/n')

while start_game == 'y':
    try:
        # Random set of numbers is generated
        winning_numbers = set()
        while len(winning_numbers) < 7:
            winning_numbers.add(random.randint(1, 55))

        # User enters their numbers
        players_numbers = set()
        while len(players_numbers) < 7:
            position = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
            k = len(players_numbers)
            choice = int(input('Please enter your {} number'.format(position[len(players_numbers)])))
            if choice in range(1, 56) and choice not in players_numbers:
                players_numbers.add(choice)
            else:
                print('Please enter a unique number between 0 and 55. Your {} numbers so far are {}'.format(len(players_numbers), players_numbers))

        # Count number of matches in lists/sets
        matches = 0
        for numbers in players_numbers:
            if numbers in winning_numbers:
                matches += 1
        print('Your lottery numbers are... {}.\n'
              'The winning numbers are ... {}\n'
              'You have matched {} numbers! Thank you for playing'
              .format(sorted(players_numbers), sorted(winning_numbers), matches))
        # sorted returns a sorted sequence or collection the form of a list
        start_game = input('\nWould you like to start another game? y/n')

    except ValueError:
        print('Please enter a valid number to continue')

else:
    print('Thank you for playing')


