from random import choice


CR_count = 0
CP_count = 0
CS_count = 0

human_win_comments = ["Blind squirrel found a nut",
                    "Computer lost to dumb human",
                    "Enjoy it while you can",
                    "Dumb human got lucky",
                    ":)",
                    "Fuck me . . . lost to humanoid?"]

comp_win_comments = ["Wah, wah, wah",
                    "Computer beats the dipshit human.",
                    "Computer wins, hahaha.",
                    "Inferior human lost that one.",
                    "Sausages, Sausages. Barely even human!",
                    ":("]

match_length = input("How many games wins the match? \n> ")
if match_length.isdigit():
    match_length = int(match_length)

else:
    match_length = int(
        input("Enter nothing but digits! How many games wins the match?? "))

player_wins = 0
computer_wins = 0

while player_wins < match_length and computer_wins < match_length:
    human_won = choice(human_win_comments)

    comp_won = choice(comp_win_comments)

    human = input("Make your selection: r/p/s or q (quit)\n> ").lower()

    if human == "r" or human == "rock":
        human = "rock"

    elif human == "s" or human == "scissors":
        human = "scissors"

    elif human == "p" or human == "paper":
        human = "paper"

    elif human == "q" or human == "Q" or human == "Q":
        break

    else:
        print("Make a valid selection, dumbass!")

    computer = choice(["rock", "paper", "scissors"])
    print(f"Computer's choice is {computer}.\n")
    if computer == "rock":
        CR_count += 1
    elif computer == "paper":
        CP_count += 1
    else:
        CS_count += 1

    if computer == human:
        print("Tie game. Shoot again.")

    elif computer == "scissors" and human == "paper":
        print(f"{computer.capitalize()} cuts {human}. {comp_won}")
        computer_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    elif computer == "paper" and human == "rock":
        print(f"{computer.capitalize()} covers {human}. {comp_won}")
        computer_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    elif computer == "rock" and human == "scissors":
        print(f"{computer.capitalize()} smashes {human}. {comp_won}")
        computer_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    elif human == "scissors" and computer == "paper":
        print(f"{human.capitalize()} cuts {computer}. {human_won}.")
        player_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    elif human == "paper" and computer == "rock":
        print(f"{human.capitalize()} covers {computer}. {human_won}.")
        player_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    elif human == "rock" and computer == "scissors":
        print(f"{human.capitalize()} smashes {computer}. {human_won}.")
        player_wins += 1
        print(f"Human: {player_wins}, Computer: {computer_wins}")

    else:
        print("You suck at this game!")

if human == "q" or human == "Q" or human == "Q":
    print("Human forfeits")

elif player_wins > computer_wins:
    print("Human wins the match.\n\n" * 100000)

else:
    print("Computer wins the match.")
CRper = round(100 * CR_count / (CR_count + CP_count + CS_count), 1)
CSper = round(100 * CS_count / (CR_count + CP_count + CS_count), 1)
CPper = round(100 * CP_count / (CR_count + CP_count + CS_count), 1)
print(f"Computer's 'random' choices:\nRock: {CRper}%")
print(f"Paper: {CPper}%\nScissors: {CSper}%")
