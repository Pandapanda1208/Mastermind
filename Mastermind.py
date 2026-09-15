import os
import sys
import random
import json

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

with open('Mastermind_Combinations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
with open("Feedback.txt", "w", encoding="utf-8") as file:
  file.write('\n')

def feedback():
  global Guess, Correct, Semi
  with open("Feedback.txt", "a", encoding="utf-8") as file:
    file.write(f'{Guess}   Correct: {Correct}| Semi: {Semi}\n')

clear()

intake = input('Do You want to include empty spaces(y/n) ')

if intake.lower() == 'y':
  combn = random.randint(1, 1296)
  options = ['R', 'G', 'B', 'Y', 'P', 'E']
else:
  combn = random.randint(1, 625)
  options = ['R', 'G', 'B', 'Y', 'P']
  

comb = data[f'combo_{combn}']

run = True
score = 0

while run:
  clear()
  print(f'These are your options: {options}')
  Guess = input('What is your Guess? ').upper()
  while len([char for char in Guess]) != 4:
    Guess = input('That is not the Correct length of 4, What is your guess').upper()
  score += 1
  combi = list(comb)
  Correct = 0
  Semi = 0
  for i in range(4):
    if Guess[i] == combi[i]:
      Correct += 1
      combi[i] = 'O'
  for i in range(4):
    if Guess[i] != comb[i] and Guess[i] in combi:
      Semi += 1
      combi[comb.index(Guess[i])] = 'O'
  clear()
  feedback()
  if Correct == 4:
    input(f'You Guessed it Correctly in {score} tries. It was {comb}!')
    sys.exit()
  elif score >= 12:
    input(f"You Didn't get it right in time, the correct answer was {comb}")
    sys.exit()
  else:
    input(f"You didn't get it right, check 'Feedback.txt' to see you rating.")