import random

stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]


def roll_3d6(stat_min) -> dict:
    """
    Roll 3 six-sided dice six times and return a dictionary containing the results.

    Returns:
    - A dictionary mapping each roll to its corresponding result.
    """
    sets = []
    has_large_number = False
    while len(sets) < 6:
        roll = sum(random.randint(1, 6) for _ in range(3))
        if roll >= stat_min:
            has_large_number = True
        sets.append(roll)
    if not has_large_number:
        min_index = sets.index(min(sets))
        sets[min_index] = random.randint(14, 18)
    return dict(zip(stats, sets))


def roll_4d6(stat_min) -> dict:
    """
    Roll 4 six-sided dice, discard the lowest roll, and return the sum of the remaining rolls.

    Returns:
    - The sum of the highest 3 dice rolls.
    """
    numbers = []
    has_large_number = False
    while len(numbers) < 6:
        rolls = sorted([random.randint(1, 6) for _ in range(4)])[1:]
        roll_sum = sum(rolls)
        if roll_sum >= stat_min:
            has_large_number = True
        numbers.append(roll_sum)
    if not has_large_number:
        min_index = numbers.index(min(numbers))
        numbers[min_index] = random.randint(14, 18)
    return dict(zip(stats, numbers))


def roll_24d6(stat_min) -> dict:
    """
    Roll 24 six-sided dice, discard the 4 lowest and 2 highest rolls, combine the remaining rolls
    into sets of three, and assign the first six sums to the stats in the order of STR, DEX, CON, INT, WIS, CHA.

    Returns:
    - A dictionary mapping each stat to its corresponding sum.
    """
    while True:
        # Generate 24 six-sided dice rolls
        rolls = [random.randint(1, 6) for _ in range(24)]
        # Sort the rolls and discard the 4 lowest and 2 highest
        sorted_rolls = sorted(rolls)[4:-2]
        # Combine the remaining rolls into sets of three
        sets = [sum(sorted_rolls[i: i + 3]) for i in range(0, 18, 3)]

        if any(roll >= stat_min for roll in sets):
            break

    random.shuffle(sets)
    return {stats[i]: sets[i] for i in range(6)}


def roll_d16_plus_2() -> dict:
    """
    Roll a 16-sided die with an added value of 2 six times and return a dictionary containing the results.

    Returns:
    - A dictionary mapping each roll to its corresponding result.
    """
    results = []
    for _ in range(6):
        roll = random.randint(1, 16) + 2
        results.append(roll)

    return dict(zip(stats, results))


while True:
    # Get user input for which option to roll
    print("Do you wish to re-roll if no stats are 14 or greater?")
    option = input("Enter your choice (yes/no): ")
    if option.lower() not in ["yes", "y"]:
        stat_min = 0
    else:
        stat_min = 14

    print("Enter 1 to roll 3d6")
    print("Enter 2 to roll 4d6 (dropping the lowest value)")
    print("Enter 3 to roll 24d6 (discarding the 4 lowest and 2 highest die rolls) and randomly assign")
    print("Enter 4 to roll d16+2 (six times)")

    # Get user input for which option to roll
    option = input("Enter your choice: ")

    # Roll the chosen option and assign to stats
    if option == "1":
        result = roll_3d6(stat_min)
    elif option == "2":
        result = roll_4d6(stat_min)
    elif option == "3":
        result = roll_24d6(stat_min)
    elif option == "4":
        result = roll_d16_plus_2()
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4.")
        continue

    # Display the results
    for stat, value in result.items():
        print(f"{stat}: {value}")

    # Ask the user if they want to run the program again
    run_again = input("Do you want to roll more stats? (yes/no): ")
    if run_again.lower() not in ["yes", "y"]:
        break
