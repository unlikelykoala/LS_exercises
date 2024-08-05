from datetime import datetime

age = int(input('What is your age? '))
retire = int(input('At what age would you like to retire? '))
diff = retire - age
year = datetime.now().year

print(f'It\'s {year}. You will retire in {year + (diff)}.\n'
      f'You havbe only {diff} years of work to go!'
      )
