import random

winning_numbers = set()
while winning_numbers <
for i in range(1,8):
    randno = random.randint(1,55)
    winning_numbers.add(randno)
print(winning_numbers)

matches = 0

players_choice = (input('Enter 7 numbers here separated by a comma. '
                       'You can choose any number between 1 and 55... '))
players_choice_list_string = players_choice.split(',')

players_choice_list_int = list(map(int, players_choice_list_string))
print(players_choice_list_int)

if len(players_choice_list_int) == 7:
    for numbers in players_choice_list_int:
        if numbers in winning_numbers:
            matches += 1
    print('Your numbers are ... {}.\n'
          'The winning numbers are ... {}\n'
          'You have matched {} numbers! Thank you for playing'
          .format(sorted(players_choice_list_int), sorted(winning_numbers), matches))
else:
    print('You must choose 7 numbers to play')

