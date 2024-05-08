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

game_images = [rock, paper, scissors]

user_choice = input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n ")
if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number,You lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer Choose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")

    elif computer_choice == 0 and user_choice ==2:
        print("You Lose!")

    elif computer_choice>user_choice:
        print("You Lose!")

    elif computer_choice == user_choice:
        print("It's a draw")


