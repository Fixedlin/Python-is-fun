rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

# Write code below
import random
from replit import clear

def play_game():
  print("Game rock paper scissors")
  print("Rules of game 0 for rock, 1 for paper, 2 for scissors")
  print("---------------------------------")
  users = int(input("Input your choice : "))
  
  if users > 2 or users < 0:
    print("Invalid input")
  else:
    computer = random.randint(0, 2)
    print(f"Your choice is : {game_images[users]}")
    print(f"Computer choice is : {game_images[computer]}")
  
    if users == 0 and computer == 1:
      print("You lose")
    elif users == 0 and computer == 2:
      print("You win")
    elif users == 1 and computer == 0:
      print("You win")
    elif users == 1 and computer == 2:
      print("You lose")
    elif users == 2 and computer == 0:
      print("You lose")
    elif users == 2 and computer == 1:
      print("You win")
    elif users == computer:
      print("Draw !")

def try_again():
  answer = input("Did you want to play again Y/N ? : ").lower()
  
  if answer == "n":
    clear()
    print("Thank you, you've played this game !!!")
  else:
    clear()
    while answer == "y":
      play_game()
      answer = input("Did you want to play again Y/N ? : ")
      clear()
      if answer == "n":
        clear()
        print("Thank you, you've played this game !!!")

play_game()
try_again()
