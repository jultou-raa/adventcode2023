import pathlib
import re

def get_first_and_last_digit_sum(message:str):
    # 1. Make a regex that finds digits
    search_digit = r"(\d)"
    search = re.compile(search_digit)
    numbers = search.findall(message)
    # 2. Check if there is more than one number to repeat if necessary
    if len(numbers)>1:
        # 3. Return First and Last Number
        return int(numbers[0] + numbers[-1])
    else:
        # 3. Return Number twice
        return int(numbers[0]*2)

if __name__ == "__main__":

    # First Challenge
    
    # Get the input of first challenge
    with (pathlib.Path(__file__).parent / "input1.txt").open("r") as input1:
        first_input = input1.readlines()

    # Apply the function to each element of the list
    result = map(get_first_and_last_digit_sum, first_input)

    # Sum and print result
    print("The sum of all the configuration values is :", sum(result))

