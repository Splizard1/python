#imports
import tkinter as tk
import random


#game running
GameOn = True
# Initialize NEW_CHOICE to a value that won't match any valid choice
NEW_CHOICE = -1

# Initialize global variables
rounds = 1
player_wins = 0
computer_wins = 0

#main
def main():
    game()

#cool border
def border_msg(msg):
    row = len(msg)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+msg+"|"'\n' + h
    print(result)

#winner functions
def player_win():
    global player_wins, rounds
    border_msg("You won!")
    player_wins += 1
    border_msg(f"Your wins: {player_wins}   Round: {rounds}    Computer wins: {computer_wins}")

    
def comp_win():
    global computer_wins, rounds
    border_msg("You lost!")
    computer_wins +=1
    border_msg(f"Your wins: {player_wins}  Round: {rounds}     Computer wins: {computer_wins}")
    
def draw():
    border_msg("Draw!")
    border_msg(f"Your wins: {player_wins}  Round: {rounds}     Computer wins: {computer_wins}")

def  game():
    global GameOn, rounds, player_wins, computer_wins, NEW_CHOICE
    
    while GameOn:
        #player choice
        choice = input("Rock, paper or scissors? (input R/P/S)").upper()
        
        #define their choice
        valid_choice = False
        if choice == "R" or choice == "P" or choice == "S":
            valid_choice = True
            if choice == "R":
                choice_msg = "Rock"
                NEW_CHOICE = 0
            elif choice == "P":
                choice_msg = "Paper"
                NEW_CHOICE = 1
            else:
                choice_msg = "Scissors"
                NEW_CHOICE = 2
            
        #random choice of computer
        
            COMP_CHOICE = random.randint(0, 2)
            
        #assisgn choice
            if COMP_CHOICE == 0:
                comp_msg = "Rock"
            elif COMP_CHOICE == 1:
                comp_msg = "Paper"
            else:
                comp_msg = "Scissors"

            border_msg(f"Your choice: {choice_msg}       Computer choice: {comp_msg}")
            


            #logic time
            if NEW_CHOICE == 0 and COMP_CHOICE == 1:
                comp_win()
            elif NEW_CHOICE == 1 and COMP_CHOICE == 2:
                comp_win()
            elif NEW_CHOICE == 2 and COMP_CHOICE == 0:
                comp_win()
            elif NEW_CHOICE == 1 and COMP_CHOICE == 0:
                player_win()
            elif NEW_CHOICE == 2 and COMP_CHOICE == 1:
                player_win()
            elif NEW_CHOICE == 0 and COMP_CHOICE == 2:
                player_win()
            else:
                draw()

        # Invalid check
        if not valid_choice:
            print("Invalid choice, please pick Rock, paper, or scissors: ")
        else:
            rounds += 1
           
            
        if rounds == 6 or player_wins == 3 or computer_wins == 3:
            GameOn = False
            if player_wins > computer_wins:
                border_msg(f"Game Over: You win!")
            else:
                border_msg(f"Game over: You lose!")
                

main()
    
