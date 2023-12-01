import pathlib
import re
from pprint import pprint


def get_first_and_last_digit_sum(message: str):
    # 1. Make a regex that finds digits
    search_digit = r"(\d)"
    search = re.compile(search_digit)
    numbers = search.findall(message)
    # 2. Check if there is more than one number to repeat if necessary
    if len(numbers) > 1:
        # 3. Return First and Last Number
        return int(numbers[0] + numbers[-1])
    elif len(numbers) == 1:
        # 3. Return Number twice
        return int(numbers[0] * 2)
    else:
        return 0


def replace_letters_by_digits(message: str):
    # 1. define the dictionary to replace digits
    translation = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    # 2. We only have to find the first and last to change
    len_split_first = []
    len_split_last = []
    for letters in translation.keys():
        message_split = message.split(letters)
        len_split_first.append(len(message_split[0]))
        len_split_last.append(len(message_split[-1]))

    values_to_replace = [
        list(translation.keys())[i]
        for i in (
            len_split_first.index(min(len_split_first)),
            len_split_last.index(min(len_split_last)),
        )
    ]

    # 3. Replacement (Be careful of this kind of input 'eightow' that should have an 8 and a 2)
    for val in values_to_replace:
        message = message.replace(
            val, translation[val] + val
        )  # adding value after replacement permit to have both numbers in case of collapsed letters

    return message


if __name__ == "__main__":
    # First Challenge

    # Get the input of first challenge
    with (pathlib.Path(__file__).parent / "input1.txt").open("r") as input1:
        first_input = input1.readlines()

    # Apply the function to each element of the list
    first_result = map(get_first_and_last_digit_sum, first_input.copy())

    # Sum and print result
    print("The sum of all the configuration values is :", sum(first_result))

    # Second Challenge - same input

    # First we apply a change on each line of the list
    second_input = first_input.copy()
    temp_result = map(replace_letters_by_digits, second_input)

    # Then we apply the first function on the newer list
    second_result = map(get_first_and_last_digit_sum, temp_result)

    # Then we print the sum as part 1
    print("The sum of all the configuration values in part 2 is :", sum(second_result))
