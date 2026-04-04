print("WELCOME TO ROCK . PAPER . SCISSORS . GAME!")
print("🎮 Rock–Paper–Scissors Rules (First to 5 Points)\n" # RULES ARE AI GENERATED 
"The game is played between Player and Computer.\n"
"Choices: Rock, Paper, Scissors.\n"
"Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n"
"Winner of each round gets 1 point.\n"
"First to reach 5 points wins the game and it ends. 🏆\n")



import random

computer_points = 0
user_points = 0
for i in range(6):
    if computer_points <= 6 or user_points <= 6:
        user_choice = input("Choose rock , paper or scissors: ")
        choices = ['rock','paper','scissors']
        comp_choice = random.choice(choices)
        comp = "computer"
        user = "User"

        if user_choice == "rock" and comp_choice == "paper":
            print(f"You choose {user_choice} and computer choose {comp_choice}, so {comp} wins!.")
            computer_points += 1
        if user_choice == "rock" and comp_choice == "scissors":
            print(f"You choose {user_choice} and computer choose {comp_choice}, so {user} wins!.")
            user_points += 1
        if user_choice == "paper" and comp_choice == "rock":
            print(f"You choose {user_choice} and computer choose {comp_choice}, so {user} wins!.")
            user_points += 1
        if user_choice == "paper" and comp_choice == "scissors":
            print(f"You choose {user_choice} and computer choose {comp_choice}, so {comp} wins!.")
            computer_points += 1
        if user_choice == "scissors" and comp_choice == "rock":
            print(f"You choose {user_choice} and computer choose {comp_choice}, so {comp} wins!.")
            computer_points += 1
        if user_choice == "scissors" and comp_choice == "paper":
            print(f"You choose {user_choice} and computer choose {comp_choice}, so {user} wins!.")
            user_points += 1
        if user_choice == comp_choice:
            print(f"You choose {user_choice} and computer choose {comp_choice}, so its a tie!")

        if computer_points > user_points:
            print(f"You score {user_points} points and {comp} score {computer_points}, so {comp} wins!")

        if computer_points < user_points:
            print(f"You score {user_points} points and {comp} score {computer_points}, so You win!")

        if computer_points == user_points:
            print(f"You score {user_points} points and {comp} score {computer_points}, so Its a tie!")


        print(f" Your points -  {user_points}")
        print(f"computer points -  {computer_points}")
        break









