##We want to get a goat, man, cabbage and wolf across a river 
# wolf eats goat, goat eats cabbage so they cant be left alone 

# Initial positions
wolf = "W"
man = "W"
goat = "W"
cabbage = "W"

initial_positions = (man, wolf, goat, cabbage)

while True:
    # Display current positions
    positions = f"Man | Wolf | Goat | Cabbage |\n {man}     {wolf}      {goat}        {cabbage}"
    print(f"Current positions:\n{positions}")

    # Get user choice
    choice = input("Which would you like to take across? W/C/G/M: ").upper()

    # Store initial positions before updating
    prev_positions = (man, wolf, goat, cabbage)

    # Update positions based on user choice
    if choice == "W":
        man = "E" if man == "W" else "W"
        wolf = "E" if wolf == "W" else "W"
    elif choice == "G":
        man = "E" if man == "W" else "W"
        goat = "E" if goat == "W" else "W"
    elif choice == "C":
        man = "E" if man == "W" else "W"
        cabbage = "E" if cabbage == "W" else "W"
    elif choice == "M":
        man = "E" if man == "W" else "W"
    else:
        print("Invalid choice. Please enter W, C, or G.")
        # Reset to initial positions
        man, wolf, goat, cabbage = initial_positions
        continue  # Skip the rest of the loop and start a new iteration

    # Check if the wolf and goat are left alone or the goat and cabbage are left alone
    if (wolf == goat and man != wolf) or (goat == cabbage and man != goat):
        print("Oops! The wolf would eat the goat or the goat would eat the cabbage. Try again.")
        # Reset to initial positions
        man, wolf, goat, cabbage = initial_positions
    elif man == "E" and wolf == "E" and goat == "E" and cabbage == "E":
        print("Congratulations! You successfully transported everyone across the river.")
        break
