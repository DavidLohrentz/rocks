from random import choice


CR_count = 0
CP_count = 0
CS_count = 0

HR_count = 0
HP_count = 0
HS_count = 0

human_win_comments = ["Blind squirrel found a nut",
                    "Computer lost to dumb human",
                    "Enjoy it while you can",
                    "Dumb human got lucky",
                    ":)",
                    "Fuck me . . . lost to humanoid"]

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

    if human == "r":
        HR_count += 1

    elif human == "p":
        HP_count += 1

    elif human == "s":
        HS_count += 1

    else:
        print("Tsk, Tsk, Tsk")

    if human == "r" or human == "rock":
        human = "rock"

    elif human == "s" or human == "scissors":
        human = "scissors"

    elif human == "p" or human == "paper":
        human = "paper"

    elif human == "q" or human == "Q" or human == "quit":
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
    print("Human wins the match.\n" * 10)

else:
    print("Computer wins the match.\n" *10)
CRper = round(100 * CR_count / (CR_count + CP_count + CS_count), 1)
CSper = round(100 * CS_count / (CR_count + CP_count + CS_count), 1)
CPper = round(100 * CP_count / (CR_count + CP_count + CS_count), 1)

HRper = round(100 * HR_count / (HR_count + HP_count + HS_count), 1)
HSper = round(100 * HS_count / (HR_count + HP_count + HS_count), 1)
HPper = round(100 * HP_count / (HR_count + HP_count + HS_count), 1)

#print(f"\nComputer:\nRock: {CRper}%")
#print(f"Paper: {CPper}%\nScissors: {CSper}%\n-----------------\n")

#print(f"Human:\nRock: {HRper}%")
#print(f"Paper: {HPper}%\nScissors: {HSper}%")
print("\n            CHOICE FREQUENCIES")
print(f"\n            Computer:    Human:")
print(f"Rock:       {CRper}%        {HRper}%")
print(f"Paper:      {CPper}%        {HPper}%")
print(f"Scissors:   {CSper}%        {HSper}%")

if HSper >= 50:
    print("You chose scissors way the fuck too often!")

elif HPper >= 50:
    print("You chose paper too damn often!")

elif HRper >= 50:
    print("You chose rock too fucking often!")

else:
    print("Nice distribution of choices.")
