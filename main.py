import random

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

#Write your code below this line 👇

game_images = [rock, paper, scissors]

you = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors:\n "))
if you >= 3 or you < 0:
  print("Wrong number!")
else:
  print(game_images[you])

comp1 = random.randint(0, 2)
print(game_images[comp1])

if you == 0 and comp1 == 2:
  print("You win!")
elif comp1 == 0 and you == 2:
  print("You lose!")
elif comp1 > you:
  print("You lose!")
elif you > comp1:
  print("You win!")
elif comp1 == you:
  print("It's a tie!")
