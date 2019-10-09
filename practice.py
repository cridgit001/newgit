#user_input = str.lower(input("Who's better? Roger or Bugs?"))

#if user_input == 'roger':
#    print('Shave and a haircut')
#elif user_input == 'bugs':
#    print("What's up doc?")
#else:
#    print('Run away! Run away!')

#choice = str.lower(input('What kind of meat would you like?'))

#print({'beef': 1.50, 'chicken': 1.00, 'pork': 1.25}[choice])

choice = str.lower(input('What kind of meat would you like? '))

branch = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99}

if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')

L = ['Good,'
     'Bad,'
     'Ugly']
