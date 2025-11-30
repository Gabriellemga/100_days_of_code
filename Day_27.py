import os
import random
import time

print('Character Builder\n')


side6 = random.randint(1,6)
side12 = random.randint(1,12)

  
def character_health():
  health = (side6 * side12 / 2) + 10
  return health
  
def character_strength():
    strength = (side6 * side12 / 2) + 12
    return strength


def character_creation():
  character = input('\nName Your Legend:')
  character_type = input('Character Type (Human, Elf, Wizard, Orc, Fairy, Dwarf):')
        
  time.sleep(3)
  print('\n')    
  print('*' * 20)
  print(f'Character name : {character}')
  print(f'Character type : {character_type}')
  print('HEALTH:', character_health())
  print('STERNGTH:', character_strength())
  print('\nMay your name go down in Legend...')
  

while True:
  character_creation()
  again = input('\n\nDo you want create another character? (yes/no):')
  if  again == 'yes':
    os.system('clear')
    character_creation()
  else:
     print('Goodbye')
     break
