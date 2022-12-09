from copy import copy

puzzle_input = """L 1
R 1
L 1
U 1
R 2
U 1
D 2
R 2
U 1
D 2
U 2
L 2
D 1
U 1
D 2
L 2
D 1
L 2
D 2
L 1
U 2
R 2
L 1
D 2
L 2
R 2
D 2
L 1
U 1
R 1
U 1
L 1
D 1
R 1
U 2
D 2
R 1
U 1
R 1
L 1
U 1
R 1
D 1
L 1
U 1
R 1
D 1
U 1
D 1
U 1
R 2
L 2
D 2
L 2
R 1
U 2
L 2
R 1
U 1
R 2
D 2
R 2
L 2
U 2
R 2
D 2
R 1
U 1
L 2
R 1
U 1
D 2
U 2
D 1
R 2
L 2
D 2
L 2
R 2
U 1
R 2
L 2
D 2
L 1
D 1
R 2
L 1
U 2
R 1
U 2
D 1
U 2
D 1
L 1
R 2
D 2
R 2
U 2
R 1
U 2
R 2
U 1
R 1
D 2
U 2
R 2
U 1
R 2
D 2
R 1
L 1
U 3
L 2
U 1
L 2
U 1
D 1
U 2
D 1
U 2
R 2
L 1
U 3
R 1
U 1
R 3
L 3
D 3
L 2
U 1
D 3
U 1
R 1
L 1
R 2
L 1
R 3
L 3
D 1
R 2
L 3
U 3
D 1
L 2
U 2
D 2
L 2
U 1
R 1
L 2
R 3
L 3
D 3
R 2
D 3
U 1
L 3
R 1
U 2
L 1
D 3
L 1
U 1
D 3
L 3
U 2
D 1
U 2
L 3
R 1
U 2
D 2
R 3
D 3
U 2
D 3
L 3
R 3
L 1
U 3
L 1
D 1
L 2
D 2
R 1
L 3
R 2
L 3
R 3
L 1
D 1
U 3
L 2
R 2
L 2
D 3
U 3
L 3
U 3
D 1
U 2
R 2
U 1
D 3
L 3
R 1
L 3
U 3
D 1
L 3
D 2
R 1
U 1
R 1
D 2
L 2
U 1
L 2
R 2
L 2
D 3
U 3
D 4
L 3
D 4
R 3
L 2
U 3
R 3
U 1
R 4
U 2
D 1
R 3
L 1
R 1
D 3
R 2
D 1
R 2
L 2
U 2
D 1
R 1
U 2
R 3
L 2
D 1
U 3
R 2
D 4
L 3
U 1
R 1
D 2
U 1
R 3
L 4
D 2
L 1
U 3
L 2
U 3
R 1
D 1
L 2
R 4
D 4
U 1
R 3
U 3
R 1
U 3
L 2
U 3
L 2
D 4
U 1
R 1
L 2
R 2
D 2
L 2
D 2
U 4
D 4
L 2
U 2
D 3
L 4
U 4
D 4
R 1
D 4
R 1
D 1
L 1
R 1
L 1
D 2
L 4
D 2
R 3
L 1
D 2
U 3
L 2
U 3
R 4
D 4
U 1
L 1
U 4
L 4
U 3
D 2
R 3
L 1
D 3
U 3
R 1
L 3
U 1
D 1
R 1
U 3
R 2
L 1
D 1
L 3
U 1
D 1
L 2
R 3
U 4
L 5
D 5
R 5
D 3
U 3
D 1
L 5
R 2
U 1
L 2
D 1
L 1
D 4
R 1
U 1
L 1
U 1
D 3
L 4
D 1
U 5
L 1
R 5
L 2
R 4
D 5
U 2
D 3
U 4
L 1
R 2
U 4
L 4
D 3
R 1
U 1
R 3
D 3
U 5
L 3
D 3
U 5
R 4
L 1
D 4
U 1
L 1
R 4
D 5
L 5
D 3
R 5
U 3
R 2
D 2
U 2
D 5
R 5
D 5
R 2
D 5
U 2
D 2
R 1
L 5
D 2
U 2
R 5
U 1
D 5
U 5
L 2
D 5
L 1
R 4
U 4
D 1
L 5
U 4
L 1
R 3
L 3
R 3
L 3
D 3
R 4
U 5
L 2
D 3
U 2
L 1
R 5
U 1
L 3
U 4
L 4
D 4
R 1
D 4
R 5
D 5
U 5
R 5
L 3
D 3
U 2
R 5
U 5
R 2
D 5
R 1
U 2
D 5
L 3
R 5
U 5
R 4
D 6
L 4
U 4
L 6
R 2
L 4
U 5
L 1
U 6
D 4
R 3
U 2
R 1
D 5
L 4
U 2
R 6
U 1
L 2
D 6
U 1
R 2
L 3
R 2
L 5
U 1
R 3
D 3
L 4
R 5
U 1
D 3
R 6
D 5
R 4
D 3
U 2
D 4
R 5
U 4
R 2
L 2
U 5
D 5
U 6
D 4
U 5
L 5
R 1
D 3
R 3
L 3
D 3
L 3
U 6
R 5
D 6
U 5
L 1
R 4
L 1
U 4
L 5
D 5
U 4
D 3
R 3
L 4
R 4
U 6
L 5
D 2
U 3
R 4
U 5
L 5
D 6
R 5
D 5
L 3
U 6
L 3
U 5
D 2
U 4
R 4
U 3
D 1
R 2
L 6
R 2
L 3
U 5
L 1
R 4
D 2
U 5
D 2
R 4
U 6
R 6
L 6
U 6
L 4
R 5
D 3
U 1
D 6
L 1
D 3
L 4
D 6
U 3
D 2
L 2
U 5
D 2
U 5
D 6
R 4
D 1
U 1
D 5
U 1
L 7
U 3
R 3
U 5
D 2
R 7
D 6
L 7
R 6
L 3
R 3
U 1
L 4
D 4
L 6
R 1
U 4
L 3
R 3
D 3
L 2
D 7
U 7
D 7
R 2
L 6
D 2
R 6
D 6
U 5
L 4
U 3
D 6
U 3
D 1
L 7
U 7
L 4
R 3
D 6
U 2
L 6
D 3
U 7
D 2
R 7
D 4
L 4
R 4
U 2
D 3
U 2
L 4
R 4
L 4
D 6
R 4
U 1
R 7
D 7
U 7
R 6
D 4
U 2
D 4
L 5
U 4
D 6
R 4
U 2
R 1
U 4
D 5
R 1
D 7
R 4
U 1
D 4
U 6
L 6
R 1
D 1
R 1
D 6
R 6
D 3
U 1
D 5
R 4
L 1
D 6
R 6
L 8
U 1
D 7
R 4
L 2
R 6
U 7
L 2
D 5
R 6
D 3
L 4
R 5
U 7
L 3
U 8
L 1
U 6
L 8
R 7
D 2
U 3
R 4
L 8
D 4
L 1
U 1
D 7
U 8
R 7
D 2
L 5
U 6
D 7
R 4
L 1
R 3
U 1
R 2
U 1
D 7
R 6
U 7
D 6
L 2
D 8
U 4
R 8
L 5
D 6
L 7
U 7
R 8
L 5
D 5
R 4
L 5
U 8
D 4
U 6
D 2
U 5
R 7
L 8
U 7
R 3
L 8
R 6
D 4
R 2
D 6
R 5
D 2
U 6
L 4
U 8
R 3
U 1
L 6
R 1
L 3
R 1
U 3
L 8
D 5
U 6
L 8
D 6
R 2
U 6
R 4
L 8
D 1
R 6
D 8
U 6
D 6
L 3
U 4
D 2
L 2
D 7
L 5
U 3
R 8
D 6
R 5
L 8
U 5
L 9
R 7
D 5
R 2
U 5
L 3
D 9
R 4
U 1
L 3
R 5
L 7
R 8
D 1
U 4
L 4
R 3
U 8
L 8
D 8
U 9
R 6
U 3
R 2
U 8
D 9
R 3
L 2
U 9
R 9
L 8
D 2
R 1
L 8
U 7
R 3
L 1
R 9
L 4
R 2
U 3
D 8
R 5
U 9
L 9
R 1
D 5
R 5
U 4
L 9
R 6
D 5
L 2
R 6
U 1
D 5
L 3
R 1
U 5
R 4
D 4
U 8
D 2
U 6
R 6
U 5
R 3
U 5
R 5
L 8
D 9
L 7
R 1
U 7
R 5
U 6
R 8
U 2
R 2
U 8
R 7
D 3
R 6
L 8
R 4
L 8
R 8
U 8
R 3
L 3
U 1
L 9
D 9
R 9
U 4
R 1
L 3
D 4
U 5
R 7
D 6
L 9
U 7
L 4
R 8
U 8
D 4
L 5
D 9
U 2
D 9
R 4
D 8
R 8
D 8
U 9
L 6
R 6
L 2
U 9
L 4
U 10
L 1
R 10
D 3
U 6
R 5
D 3
R 4
L 4
U 7
D 9
R 2
D 10
U 9
L 7
D 4
R 2
L 10
D 5
R 5
U 9
R 4
L 7
R 5
D 3
R 6
D 8
R 6
D 10
R 7
U 4
D 5
U 6
L 3
D 3
U 10
R 10
U 10
D 9
R 6
D 2
R 9
D 8
R 7
U 10
R 4
U 6
R 7
U 2
R 5
U 6
L 4
U 8
L 6
D 8
R 2
U 2
L 4
U 4
R 5
U 10
D 8
U 7
R 5
D 3
L 2
R 9
U 10
L 1
U 5
L 1
D 3
L 9
R 9
U 2
D 3
U 8
R 10
L 2
U 9
D 4
U 4
D 10
L 4
D 3
R 3
L 2
U 8
L 4
D 6
R 2
L 3
D 6
L 4
D 5
L 7
U 9
L 3
D 4
R 6
L 10
U 5
L 3
R 3
D 6
U 1
L 3
R 5
D 8
R 11
U 2
L 11
R 7
U 8
R 4
D 4
U 6
D 4
U 9
D 5
R 9
D 9
U 6
D 1
U 3
L 4
U 3
D 11
U 11
R 4
L 3
U 5
D 1
R 4
U 6
D 4
U 3
D 8
L 7
R 8
L 9
R 3
D 4
U 6
L 2
U 6
R 3
D 8
R 1
L 5
U 8
D 3
R 8
L 8
U 3
R 2
U 11
L 9
U 4
D 10
L 7
D 1
U 2
D 7
R 4
L 2
U 8
L 5
U 5
D 1
L 11
R 4
L 7
U 2
D 9
L 4
U 11
R 8
L 1
D 10
U 5
R 4
L 8
U 8
D 11
U 8
D 3
R 4
U 8
R 2
U 3
R 9
D 4
L 2
D 4
L 4
U 4
R 5
U 4
L 10
U 4
L 4
R 8
D 5
L 2
U 5
D 9
U 10
D 6
R 9
D 4
R 10
U 4
D 12
R 7
L 12
R 8
L 11
U 1
D 4
L 1
D 7
R 1
L 5
R 9
L 3
D 7
L 2
R 6
U 2
D 2
U 9
L 4
U 11
D 4
R 7
D 7
L 11
U 11
L 1
D 9
U 6
R 3
D 3
L 9
R 7
L 6
D 6
R 11
D 10
U 11
R 1
U 2
R 9
L 6
U 7
D 5
U 7
R 4
U 12
R 2
D 1
L 7
R 5
D 6
R 1
D 11
R 9
L 6
U 11
D 7
L 7
R 9
L 7
D 12
U 7
D 12
R 3
L 2
R 10
D 1
L 9
R 3
D 6
R 11
U 2
L 2
U 3
R 3
L 6
U 3
R 1
L 5
R 7
U 2
D 8
L 9
U 7
L 9
D 12
U 3
D 9
U 1
L 10
D 9
L 11
U 6
R 9
U 10
L 5
R 11
U 3
R 9
D 12
U 1
D 11
R 12
U 1
D 7
L 1
U 7
L 5
U 8
L 2
R 6
U 13
R 3
D 8
U 2
L 5
U 7
L 7
U 13
L 3
R 5
D 1
L 9
U 2
L 7
R 9
U 12
R 9
L 13
R 1
U 11
R 4
U 6
D 6
R 13
D 13
U 5
L 9
U 2
D 9
R 12
D 13
U 9
D 10
U 11
R 11
U 12
D 5
L 1
R 2
U 2
D 5
U 1
D 8
R 8
L 1
U 9
L 11
D 10
R 1
D 6
U 5
D 11
L 13
D 2
R 1
L 1
R 7
L 1
U 2
D 6
U 4
L 7
U 8
D 7
L 11
U 5
D 5
R 1
D 6
R 1
U 9
L 11
D 6
U 10
D 10
R 2
U 13
L 5
U 9
L 13
U 7
L 3
D 9
L 13
R 5
L 5
U 5
L 13
U 10
L 1
R 10
L 8
R 13
U 13
R 7
D 6
R 4
L 5
U 3
D 6
R 13
U 9
L 10
U 13
R 3
D 8
L 8
U 5
L 9
U 4
D 11
L 14
U 11
R 1
D 7
U 4
R 11
U 3
R 2
U 11
L 6
R 2
D 5
L 1
U 1
L 11
R 5
U 10
D 12
R 3
L 6
R 3
D 9
L 4
D 11
L 11
D 4
R 10
D 3
L 12
D 8
U 7
R 2
D 1
L 5
U 11
L 9
R 4
U 4
D 11
R 9
D 3
U 6
L 4
U 4
L 8
U 6
L 14
R 13
D 5
R 5
U 5
R 2
U 8
L 12
R 2
U 12
D 4
R 3
L 5
D 11
R 7
U 9
D 10
L 1
D 4
U 4
D 1
R 9
L 10
R 11
L 8
D 10
R 10
L 3
R 1
L 9
D 4
L 8
R 7
U 12
R 5
L 10
R 7
U 6
R 7
U 8
D 1
U 1
L 1
R 2
D 14
U 4
D 5
R 2
D 1
R 5
D 6
R 3
L 12
U 11
D 1
L 7
R 10
U 2
R 6
U 11
R 12
U 2
R 4
L 1
D 7
U 2
D 9
U 12
D 11
U 2
L 4
R 10
U 13
R 2
L 8
R 13
L 11
R 13
L 13
R 5
D 2
U 10
D 14
L 8
U 11
R 1
L 15
U 13
L 4
D 9
L 1
U 14
R 10
D 2
R 15
L 12
R 15
U 15
L 3
U 1
L 1
R 9
D 11
L 9
D 3
U 12
R 1
D 7
L 8
R 10
D 2
L 4
D 2
U 12
D 12
L 15
U 3
D 13
U 13
D 3
R 4
L 7
D 6
U 7
D 7
R 2
D 2
R 10
L 12
U 14
D 1
U 5
L 8
R 1
U 5
D 8
U 1
D 15
U 13
L 15
R 1
L 10
U 14
D 15
R 10
L 13
D 8
L 7
U 11
R 7
U 10
D 15
L 1
U 5
L 2
R 6
L 4
U 15
R 13
U 4
R 7
U 4
R 10
L 3
U 10
R 10
D 13
R 11
L 12
D 12
U 7
R 8
D 14
L 4
R 4
L 8
D 6
R 8
L 5
U 6
L 7
U 14
D 14
R 14
L 9
D 5
U 14
R 16
L 4
R 14
U 3
D 10
L 5
R 9
D 4
R 14
L 16
D 13
L 4
R 13
D 5
R 5
U 1
R 6
L 15
D 16
R 15
D 11
R 11
D 6
U 7
L 10
D 7
U 12
R 6
L 2
U 7
L 8
U 14
L 5
U 6
L 10
R 16
L 13
D 13
U 7
R 9
L 8
U 3
D 6
R 2
L 4
R 15
D 12
U 7
D 4
U 2
L 10
D 4
L 11
D 12
R 5
L 13
U 16
L 12
R 3
L 16
R 14
L 8
R 7
U 7
L 7
D 12
R 2
D 5
R 14
U 9
D 15
U 2
L 10
D 1
U 13
L 2
R 13
D 5
U 1
D 2
L 7
D 14
U 12
D 8
U 10
L 3
R 1
U 14
R 8
L 12
R 8
U 2
R 1
D 14
U 5
D 11
R 16
U 1
R 13
D 2
U 14
R 11
D 12
U 17
R 12
L 6
U 4
R 16
D 4
R 2
D 1
U 6
D 11
R 8
L 7
R 3
U 3
L 14
R 11
L 9
U 9
L 2
R 6
U 11
R 9
L 15
U 7
R 6
D 15
U 11
L 5
U 2
R 8
D 13
L 5
U 6
R 13
D 15
U 11
L 10
R 16
L 14
U 15
R 3
L 9
U 11
L 6
R 7
L 6
D 16
U 8
R 2
U 14
D 14
R 15
D 2
L 16
D 14
U 17
D 6
L 16
D 7
R 2
U 17
D 2
U 2
D 15
U 5
R 9
L 10
D 16
U 1
L 5
U 6
R 10
D 11
R 1
U 7
R 13
U 6
R 2
L 11
D 13
U 8
D 4
R 15
U 8
R 14
L 17
U 5
L 12
U 11
L 14
R 12
L 2
D 10
L 14
D 10
L 11
U 15
D 7
U 5
R 10
U 4
R 14
U 3
D 9
L 6
D 10
L 1
U 4
L 15
R 4
U 13
D 18
R 15
L 3
U 17
R 5
L 3
D 3
L 1
U 10
L 3
R 5
U 13
D 2
R 17
D 3
U 4
L 15
D 5
L 18
U 7
D 7
U 10
L 18
D 14
U 18
L 11
D 3
L 15
D 14
L 16
R 2
D 8
L 12
U 11
R 12
D 2
L 3
R 12
U 7
L 9
D 8
U 7
L 10
D 2
U 10
D 16
L 17
R 13
L 12
R 18
L 6
U 2
D 6
L 15
D 8
U 14
R 12
L 8
R 6
L 17
U 5
D 4
L 8
U 16
R 8
U 12
L 1
R 6
D 11
L 10
U 13
R 4
L 9
R 7
D 1
L 17
R 4
L 13
R 8
D 14
U 3
R 10
L 18
R 11
U 3
D 5
U 2
L 14
R 12
D 12
R 11
U 5
D 17
R 2
D 6
L 13
D 4
L 5
R 7
U 7
L 12
D 16
U 6
L 1
R 18
D 4
R 11
D 10
L 11
D 2
L 1
D 5
U 2
R 19
D 10
U 14
R 1
U 11
R 15
D 2
L 15
U 19
R 3
L 2
D 12
R 2
L 15
R 8
D 3
R 8
D 11
R 17
D 5
R 16
L 8
R 12
L 5
R 14
D 3
R 19
D 4
R 18
L 4
U 12
D 7
L 8
R 11
U 14
L 12
U 17
L 1
D 5
R 8
L 18
U 16
L 15
D 13
U 18
R 11
L 7
R 19
L 15
U 10
L 4
R 9
U 7
R 8
L 16
R 8
L 17
D 8
L 17
D 18
U 9
D 2
L 6
U 6
L 7
D 18
R 1
U 13
L 2
U 1
R 8
U 11
D 14
R 6
U 13
R 2
D 11
L 5
U 12
D 7
U 4
R 4
D 19
R 17
L 10
U 5
L 1
U 4
L 6
D 11
L 16
D 9
R 16
L 3
R 1
D 3
L 5
U 18
D 13
R 10
U 5
D 4
U 17
R 4
D 18
U 1"""

test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test_input_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def main():
    first_question()
    second_question()


def touching(head_position, tail_position):
    return abs(head_position[0] - tail_position[0]) <= 1 and abs(
        head_position[1] - tail_position[1]) <= 1


def move_with_direction(direction: str, position: list) -> list:
    if direction == "R":
        position[0] += 1
    elif direction == "L":
        position[0] -= 1
    elif direction == "U":
        position[1] += 1
    elif direction == "D":
        position[1] -= 1
    else:
        raise ValueError("Unknown direction: {}".format(direction))
    return position


def put_tail_behind_head(head_position, previous_direction):
    if previous_direction == "R":
        tail_position = [head_position[0] - 1, head_position[1]]
    elif previous_direction == "L":
        tail_position = [head_position[0] + 1, head_position[1]]
    elif previous_direction == "U":
        tail_position = [head_position[0], head_position[1] - 1]
    elif previous_direction == "D":
        tail_position = [head_position[0], head_position[1] + 1]
    else:
        raise ValueError("Unknown direction: {}".format(previous_direction))
    return tail_position


def first_question():
    current_input = puzzle_input
    # system of coordinates centered at 0,0, the starting point
    s = [0, 0]
    head_position = s.copy()
    tail_position = s.copy()
    # set of all the points visited by the tail
    visited = {tuple(s)}
    # process all the moves
    for move in current_input.split("\n"):
        if not move:
            continue
        direction = move[0]
        distance = int(move[1:])
        for _ in range(distance):
            head_position = move_with_direction(direction, head_position)
            # check if the tail moves
            if not touching(head_position, tail_position):
                # move the tail
                tail_position = put_tail_behind_head(head_position, direction)
                # add the new position to the visited set
                visited.add(tuple(tail_position))
    print(len(visited))


def reconnect_tail(leading_segment, trailing_segment):
    # check that the segments lie in the same line or column
    if leading_segment == trailing_segment:
        return leading_segment
    if leading_segment[0] == trailing_segment[0]:
        # they are in the same column
        if leading_segment[1] > trailing_segment[1]:
            # the leading segment is above the trailing segment
            return [leading_segment[0], trailing_segment[1] + 1]
        else:
            # the leading segment is below the trailing segment
            return [leading_segment[0], trailing_segment[1] - 1]
    elif leading_segment[1] == trailing_segment[1]:
        # they are in the same row
        if leading_segment[0] > trailing_segment[0]:
            # the leading segment is to the right of the trailing segment
            return [trailing_segment[0] + 1, leading_segment[1]]
        else:
            # the leading segment is to the left of the trailing segment
            return [trailing_segment[0] - 1, leading_segment[1]]
    else:
        # diagonally connected segments
        # look for the axis on which the distance is the greatest
        if abs(leading_segment[0] - trailing_segment[0]) > abs(
                leading_segment[1] - trailing_segment[1]):
            # the segments are closer vertically; connect them horizontally
            if leading_segment[0] > trailing_segment[0]:
                # the leading segment is to the right of the trailing segment
                return [trailing_segment[0] + 1, leading_segment[1]]
            else:
                # the leading segment is to the left of the trailing segment
                return [trailing_segment[0] - 1, leading_segment[1]]
        elif abs(leading_segment[0] - trailing_segment[0]) < abs(
                leading_segment[1] - trailing_segment[1]):
            # the segments are closer horizontally; connect them vertically
            if leading_segment[1] > trailing_segment[1]:
                # the leading segment is above the trailing segment
                return [leading_segment[0], trailing_segment[1] + 1]
            else:
                # the leading segment is below the trailing segment
                return [leading_segment[0], trailing_segment[1] - 1]
        else:
            # the segments are equally close in both directions
            # connect them diagonally
            if leading_segment[0] > trailing_segment[0]:
                # the leading segment is to the right of the trailing segment
                if leading_segment[1] > trailing_segment[1]:
                    # the leading segment is above the trailing segment
                    return [trailing_segment[0] + 1, trailing_segment[1] + 1]
                else:
                    # the leading segment is below the trailing segment
                    return [trailing_segment[0] + 1, trailing_segment[1] - 1]
            else:
                # the leading segment is to the left of the trailing segment
                if leading_segment[1] > trailing_segment[1]:
                    # the leading segment is above the trailing segment
                    return [trailing_segment[0] - 1, trailing_segment[1] + 1]
                else:
                    # the leading segment is below the trailing segment
                    return [trailing_segment[0] - 1, trailing_segment[1] - 1]


def second_question():
    current_input = puzzle_input
    # system of coordinates centered at 0,0, the starting point
    s = [0, 0]
    head_position = s.copy()
    tail_length = 9
    tail_position = [s.copy() for _ in range(tail_length)]
    # set of all the points visited by the tail
    visited = {tuple(s)}
    # process all the moves
    for move in current_input.split("\n"):
        if not move:
            continue
        direction = move[0]
        distance = int(move[1:])
        for _ in range(distance):
            head_position = move_with_direction(direction, head_position)
            full_rope = [head_position] + tail_position
            for i in range(1, len(full_rope)):
                # check if the tail segment moves
                if not touching(full_rope[i - 1], full_rope[i]):
                    # move the tail segment
                    full_rope[i] = reconnect_tail(full_rope[i - 1], full_rope[i])
            tail_position = full_rope[1:]
            # add the tail position to the visited set
            visited.add(tuple(tail_position[-1]))
    print(len(visited))


if __name__ == '__main__':
    main()