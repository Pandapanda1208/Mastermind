import os
import random
import json

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

with open('Mastermind_Combinations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
with open("Feedback.txt", "w", encoding="utf-8") as file:
  file.write('/n')

def feedback():
  with open("Feedback.txt", "a", encoding="utf-8") as file:
    file.write(f'{Guess}   Correct: {Correct}| Semi: {Semi}/n')

clear()

intake = input('Do You want to include empty spaces(y/n) ')

if intake.lower() == 'y':
  combn = random.randint(1, 1296)
  options = ['R', 'G', 'B', 'Y', 'P', 'E']
else:
  combn = random.randint(1, 625)
  options = ['R', 'G', 'B', 'Y', 'P']
  

comb = data[f'combo_{combn}']


