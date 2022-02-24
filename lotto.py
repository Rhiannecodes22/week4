import random

start_game = input('Would you like to start the game? y/n  ')

while start_game == 'y':
    try:
        # Random set of numbers is generated. Set is used to overcome duplicates
        winning_numbers = set()
        while len(winning_numbers) < 7:
            winning_numbers.add(random.randint(1, 55))

        # User enters their numbers
        choice = input('Enter your 7 numbers here, separated by a comma')
        choice_set = set(map(int, choice.split(',')))

        # Count number of matches in lists/sets
        if len(choice_set) == 7 and 0 < min(choice_set) and max(choice_set) < 56:
            matches = 0
            for numbers in choice_set:
                if numbers in winning_numbers:
                    matches += 1
            print('Your lottery numbers are... {}.\n'
                  'The winning numbers are ... {}\n'
                  'You have matched {} numbers! Thank you for playing'
                  .format(sorted(choice_set), sorted(winning_numbers), matches))
        else:
            print('you must enter 7 unique numbers between 1 and 55')

        # sorted returns a sorted sequence or collection the form of a list

    except ValueError:
        print('Please enter a list of 7 valid numbers to continue')

    start_game = input('\nWould you like to play another game? y/n')

else:
    print('Thank you for playing')


