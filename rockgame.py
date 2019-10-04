
import random
from banner import banner
banner("Rock, Paper, Scissors"," Skyler")
def print_welcome_message():
    print("We are going to play Rock, Paper, Scissors. The first to win two out of three rounds is the winner.")


def get_players_choice():
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    choice = int(input("What is your choice? "))
    return choice

def scoreboard(p_score, c_score):
    print(f"Score: Player:{p_score} Computer:{c_score}")


print_welcome_message()
cpu_score = 0
player_score = 0
while player_score < 2 and cpu_score < 2:
    scoreboard(player_score, cpu_score)
    players_choice = get_players_choice()
    cpu_choice = random.randint(1,4)

    if players_choice == 1:
        if cpu_choice == 1:
            print("You Chose Rock, and the computer chose Rock. It is a tie.")
        if cpu_choice == 2:
            print("You chose Rock, and the computer chose Paper. You Lose this round.")
            cpu_score = cpu_score + 1
        if cpu_choice == 3:
            print("You chose Rock, and the computer chose Scissors. You Win this round.")
            player_score = player_score + 1
    if players_choice == 2:
        if cpu_choice == 1:
            print("You Chose Paper, and the computer chose Paper. It is a tie.")
        if cpu_choice == 2:
            print("You chose Paper, and the computer chose Scissors. You Lose this round.")
            cpu_score = cpu_score + 1
        if cpu_choice == 3:
            print("You chose Paper, and the computer chose Rock. You Win this round.")
            player_score = player_score + 1
    if players_choice == 3:
        if cpu_choice == 1:
            print("You Chose Scissors, and the computer chose Scissors. It is a tie.")
        if cpu_choice == 2:
            print("You chose Scissors, and the computer chose Rock. You Lose this round.")
            cpu_score = cpu_score + 1
        if cpu_choice == 3:
            print("You chose Scissors, and the computer chose Paper. You Win this round.")
            player_score = player_score + 1
            print("")
        if player_score > cpu_score:
            print("You Have Beaten The Computer In An Honorable Battle. Congrats!")
















