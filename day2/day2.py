import pathlib
import re
from functools import reduce

COLOR_THRESHOLD = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def count_max_by_color(message: str) -> dict:
    """Count for a game the maximum value of a color
    For example the message `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green`
    will return a dict with {blue: 6, red: 4, green: 2}
    """
    # Get the colors and the number of balls
    colors = re.findall(r"(\d+) (\w+)", message)
    # Create a dict with the colors and the number of balls
    colors_dict = {}
    for number, color in colors:
        if colors_dict.get(color) is not None and colors_dict[color] < int(number):
            colors_dict[color] = int(number)
        elif colors_dict.get(color) is None:
            colors_dict[color] = int(number)

    return colors_dict


def check_all_color_threshold(dict_color: dict) -> bool:
    """Check if all the colors are above the threshold"""
    return all(number <= COLOR_THRESHOLD[color] for color, number in dict_color.items())


def compute_product_from_dict(dict_color: dict) -> int:
    """Compute the product of all the values of the dict"""
    n_ball_1, n_ball_2, n_ball_3 = dict_color.values()
    return n_ball_1 * n_ball_2 * n_ball_3


if __name__ == "__main__":
    # First Challenge

    # Get the input of first challenge
    with (pathlib.Path(__file__).parent / "input.txt").open("r") as input1:
        first_input = input1.readlines()

    summary = list(map(count_max_by_color, first_input))
    check = list(map(check_all_color_threshold, summary))
    print(f"Games OK : {[i for i, v in enumerate(check, start=1) if v]}")
    print(f"Sum is : {sum([i for i, v in enumerate(check, start=1) if v])}")

    # Second challenge

    print("The sum of powers is :", sum(list(map(compute_product_from_dict, summary))))
