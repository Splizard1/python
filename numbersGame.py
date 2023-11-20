import random

def play_game():
    num = random.randint(1, 10)
    max_guesses = 3
    guesses = 0

    while guesses < max_guesses:
        try: 
            guess = int(input("Guess the number I am thinking of.. between 1 and 10: "))

            if guess <= 0 or guess > 10: 
                print("Please guess a number between 1 and 10")
            elif guess == num:
                print(f"Correct! I was thinking of {num}")
                return True  # Player won
            elif guess > num and guess <= 10:
                print("The number I am thinking of is lower.. ")
                guesses += 1
            elif guess < num and guess >= 1: 
                print("The number I am thinking of is higher..  ")
                guesses += 1
            
            
            print(f"You have {max_guesses - guesses} guesses left.")

        except ValueError:
            print("Invalid input - did you put a number between 1 and 10?")

    print(f"Sorry, you've run out of guesses! The number I was thinking of was {num}.")
    return False  # Player lost

def main():
    play_again = True
    while play_again:
        won = play_game()
        if won:
            play_again = input("Do you want to play again? (yes/no): ").lower() == 'yes'
        else:
            play_again = input("Do you want to try again? (yes/no): ").lower() == 'yes'

    print("Thanks for playing!")

if __name__ == "__main__":
    main()