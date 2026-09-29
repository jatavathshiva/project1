import random
user_choice = int(input("Enter your choice (0 for rock, 1 for paper, 2 for scissors): "))
computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice>computer_choice:
    print("You win!")
elif user_choice<computer_choice:
    print("Computer wins!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins!")