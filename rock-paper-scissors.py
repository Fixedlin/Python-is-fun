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

game_image = [rock , paper , scissors]

# Write code below
import random

print("Game rock paper scissors")
print("Cara bermainnya 0 untuk batu 1 untuk kertas 2 untuk gunting")
print("==============================")

users = int(input("Masukkan pilihan anda : "))

if users > 2 or users < 0:
  print("Invalid number, You lose")
else:
  print(f"Anda memilih : {game_image[users]}")
  computer = random.randint(0,2)
  print(f"Komputer memilih : {game_image[computer]}")


  if users == 0 and computer == 1:
    print("Computer win")
  elif users == 0 and computer == 2:
    print("You win")
  elif users == 1 and computer == 0:
    print("You win")
  elif users == 1 and computer == 2:
    print("Computer win")
  elif users == 2 and computer == 0:
    print("You win")
  elif users == 2 and computer == 1:
    print("You win")
  elif users == computer:
    print("Draw !")
