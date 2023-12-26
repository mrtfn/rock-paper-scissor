import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
user_choice = int(input("welcome to the RPS just choose between rock 0, paper 1 ans scissors 2 : "))
computer_choice = random.randint(0,2)

print(f"You chose {user_choice}{choices[user_choice]}")
print(f"computer chose {computer_choice}{choices[computer_choice]}")

if user_choice == 0 and computer_choice == 2:
    print("user wins")
elif computer_choice > user_choice:
    print("computer wins")
elif user_choice > computer_choice:
    print("user wins")
elif user_choice == computer_choice:
    print("draw")