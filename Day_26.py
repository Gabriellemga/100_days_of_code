import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  pygame.mixer.unpause()
  while True:
    stop_playback = int(input("Press 2 to pause playback and go back to the main menu:"))
    if stop_playback == 2:
      pause()
      return
    else:
      continue


while True:
  os.system("clear")
  print("🎵 MyPOD Music Player\n")
  print("Please select a song option:\n")
  time.sleep(1)
  print("Press 1 to Play\n")
  print("Press 2 to Exit\n")
  print("Press any key to return the main menu\n")
  user_input = int(input())
  if user_input == 1:
     print("Playing some proper tunes!")
     play()
  elif user_input == 2:
    print("Goodbye!!!")
    exit()
  else:
    print("Invalid input. Please try again.")
    continue
