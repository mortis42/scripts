import operator
import random
import re


def split_dice_string(dice_string):
    """Splits a dice string into its individual components.

    Args:
      dice_string: A string representing a dice roll, e.g. "2d6*5".

    Returns:
      A list of strings, where each string represents a single component of the
      dice roll, e.g. ["2", "d", "6", "*", "5"].
    """

    components = re.split(r"(\d+|\D)", dice_string)
    # Remove empty strings from the list.
    components = [component for component in components if component]
    return components


def generate_random_number(num_die, dice_size):
    """Generates a random number between index0 and index1, inclusive.

    Args:
      index0: The lower bound of the range.
      index1: The upper bound of the range.

    Returns:
      A random number between index0 and index1, inclusive.
    """

    return random.randint(num_die, dice_size)


def generate_random_dice_sum(num_die, dice_size):
    total = 0
    i = 0

    while i < num_die:
        random_number = random.randint(1, dice_size)
        total += random_number
        i += 1

    return total


def get_math_expression(components):
    # Check if the list has enough elements and if index 3 contains an arithmetic operator
    if len(components) >= 5 and components[3] in ('+', '-', '*', '/'):
        operator_symbol = components[3]
        operand = components[4]

        if operator_symbol in ('+', '-', '*', '/'):
            math_expression = f"{operator_symbol}{operand}"
            return math_expression
        else:
            return "Invalid operator."
    else:
        return "Invalid list or math expression."


def main():
    while True:
        dice_string = input(
            "Enter a dice roll (e.g., '2d6+5') or 'q' to quit: ")

        if dice_string.lower() in ['q', 'quit']:
            break

        components = split_dice_string(dice_string)
        num_die = int(components[0])
        dice_size = int(components[2])
        expression = components[3]
        modifier = components[4]
        random_sum = generate_random_dice_sum(num_die, dice_size)
        expression = get_math_expression(components)
        total = eval(str(random_sum) + expression)

        print(f"Result of the roll {dice_string}: {total}")


if __name__ == "__main__":
    main()
