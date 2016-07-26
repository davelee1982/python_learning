# Age Calculator - by David Lee - 2016

import datetime

current_time = datetime.datetime.now()

print('What year were you born?')
birth_year = input()

print('Enter a year (past or future) to see how old you were or will be.')
variable_year = input()

difference = int(variable_year) - int(current_time.year)

current_age = int(current_time.year) - int(birth_year)

print('In the year ', variable_year, ' your age is ', int(current_age) + int(difference), ' years old!')

input('Enter to Quit.')
