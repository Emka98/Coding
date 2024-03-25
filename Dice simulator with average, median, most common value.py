import random
import numpy as np
from collections import Counter

def roll_dice(amount: int = 2) -> list[int]:
    """
    Rolls some dice and returns the results as a list.

    :param amount: The amount of dice to roll.
    :return: A list of dice rolls.
    """
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def most_frequent(List):
    """
    Most_frequent searches for the most frequently repeated place in the list

    :param amount: List of numbers
    :return: Most often a repeating number
    """

    unique, counts = np.unique(List, return_counts=True)
    index = np.argmax(counts)
    return unique[index]

def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll? ')

            # To exit the game
            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break

            # Try to parse the user_input to int
            List = roll_dice(int(user_input))
            print(str(List)[1:-1])
            print("Average of your draw: ",round(np.average(List),2))
            print("Median of your draw: ", np.median(List))
            print("Most common value of your draw: ", most_frequent(List))
        except ValueError:
            print('(Please enter a valid number)')


if __name__ == '__main__':
    main()