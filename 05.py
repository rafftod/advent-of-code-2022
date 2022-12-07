import re
from collections import deque

puzzle_input = """
            [L] [M]         [M]    
        [D] [R] [Z]         [C] [L]
        [C] [S] [T] [G]     [V] [M]
[R]     [L] [Q] [B] [B]     [D] [F]
[H] [B] [G] [D] [Q] [Z]     [T] [J]
[M] [J] [H] [M] [P] [S] [V] [L] [N]
[P] [C] [N] [T] [S] [F] [R] [G] [Q]
[Z] [P] [S] [F] [F] [T] [N] [P] [W]
 1   2   3   4   5   6   7   8   9 

move 7 from 3 to 9
move 5 from 8 to 9
move 3 from 9 to 5
move 6 from 9 to 2
move 9 from 9 to 3
move 3 from 7 to 3
move 8 from 2 to 3
move 9 from 3 to 1
move 11 from 3 to 8
move 5 from 6 to 9
move 1 from 6 to 3
move 1 from 2 to 7
move 1 from 4 to 8
move 1 from 3 to 9
move 4 from 4 to 3
move 6 from 8 to 3
move 2 from 8 to 2
move 4 from 9 to 3
move 3 from 2 to 5
move 2 from 5 to 4
move 5 from 3 to 4
move 11 from 1 to 4
move 1 from 7 to 6
move 1 from 3 to 5
move 2 from 1 to 9
move 1 from 1 to 4
move 7 from 5 to 8
move 21 from 4 to 6
move 6 from 6 to 2
move 6 from 8 to 9
move 5 from 8 to 5
move 2 from 2 to 7
move 4 from 3 to 7
move 1 from 2 to 6
move 1 from 2 to 5
move 2 from 2 to 7
move 4 from 3 to 7
move 1 from 4 to 6
move 9 from 5 to 3
move 7 from 3 to 4
move 7 from 7 to 3
move 7 from 4 to 1
move 8 from 3 to 5
move 1 from 3 to 5
move 3 from 8 to 2
move 2 from 2 to 9
move 13 from 9 to 4
move 5 from 5 to 3
move 4 from 7 to 6
move 1 from 7 to 4
move 2 from 4 to 2
move 3 from 3 to 4
move 2 from 5 to 2
move 6 from 1 to 7
move 1 from 2 to 8
move 1 from 3 to 8
move 1 from 1 to 6
move 1 from 3 to 4
move 1 from 2 to 6
move 24 from 6 to 1
move 3 from 2 to 3
move 3 from 3 to 5
move 2 from 8 to 6
move 2 from 5 to 4
move 3 from 5 to 1
move 7 from 4 to 8
move 3 from 8 to 9
move 2 from 9 to 5
move 2 from 6 to 3
move 1 from 9 to 8
move 5 from 7 to 5
move 2 from 3 to 1
move 1 from 7 to 1
move 7 from 4 to 7
move 2 from 4 to 8
move 6 from 8 to 6
move 3 from 6 to 9
move 10 from 5 to 1
move 7 from 7 to 1
move 1 from 4 to 9
move 1 from 6 to 3
move 2 from 9 to 7
move 1 from 4 to 2
move 1 from 9 to 5
move 1 from 8 to 5
move 39 from 1 to 8
move 1 from 2 to 5
move 2 from 6 to 9
move 3 from 9 to 5
move 3 from 1 to 6
move 1 from 7 to 2
move 1 from 3 to 2
move 2 from 6 to 2
move 3 from 2 to 3
move 1 from 6 to 2
move 1 from 1 to 8
move 3 from 1 to 2
move 3 from 2 to 4
move 2 from 4 to 5
move 2 from 3 to 8
move 8 from 5 to 2
move 8 from 8 to 2
move 15 from 2 to 7
move 1 from 1 to 5
move 25 from 8 to 7
move 2 from 2 to 4
move 2 from 4 to 3
move 1 from 8 to 4
move 2 from 4 to 6
move 1 from 2 to 1
move 26 from 7 to 2
move 15 from 2 to 1
move 7 from 8 to 9
move 10 from 1 to 6
move 10 from 7 to 2
move 1 from 8 to 1
move 5 from 9 to 8
move 1 from 8 to 9
move 2 from 6 to 9
move 3 from 7 to 1
move 1 from 7 to 1
move 5 from 9 to 2
move 1 from 3 to 1
move 9 from 6 to 3
move 1 from 6 to 1
move 4 from 2 to 4
move 3 from 4 to 8
move 1 from 4 to 1
move 9 from 3 to 1
move 1 from 7 to 6
move 9 from 2 to 5
move 14 from 1 to 6
move 1 from 3 to 8
move 5 from 2 to 6
move 8 from 1 to 8
move 6 from 6 to 8
move 14 from 6 to 7
move 1 from 1 to 7
move 10 from 5 to 4
move 11 from 8 to 5
move 15 from 7 to 1
move 4 from 5 to 6
move 4 from 8 to 9
move 6 from 5 to 3
move 1 from 6 to 9
move 1 from 1 to 6
move 1 from 5 to 8
move 2 from 6 to 2
move 6 from 1 to 5
move 1 from 5 to 8
move 2 from 5 to 4
move 9 from 2 to 9
move 13 from 9 to 8
move 1 from 2 to 1
move 1 from 4 to 8
move 3 from 3 to 1
move 2 from 4 to 5
move 2 from 1 to 5
move 1 from 9 to 3
move 17 from 8 to 1
move 3 from 3 to 2
move 4 from 5 to 1
move 2 from 2 to 4
move 1 from 6 to 1
move 1 from 2 to 8
move 4 from 4 to 6
move 1 from 5 to 9
move 5 from 6 to 8
move 1 from 5 to 4
move 1 from 5 to 6
move 3 from 8 to 6
move 8 from 4 to 5
move 32 from 1 to 7
move 11 from 7 to 6
move 8 from 5 to 3
move 3 from 8 to 7
move 6 from 3 to 9
move 4 from 3 to 8
move 5 from 8 to 2
move 1 from 8 to 5
move 11 from 6 to 3
move 1 from 5 to 2
move 2 from 8 to 6
move 12 from 7 to 8
move 2 from 6 to 2
move 2 from 6 to 4
move 5 from 2 to 5
move 8 from 7 to 2
move 2 from 7 to 1
move 2 from 7 to 6
move 5 from 5 to 4
move 5 from 4 to 7
move 5 from 8 to 2
move 2 from 9 to 7
move 5 from 8 to 4
move 2 from 7 to 3
move 2 from 9 to 3
move 3 from 7 to 9
move 1 from 1 to 8
move 2 from 6 to 1
move 2 from 9 to 8
move 1 from 7 to 8
move 1 from 2 to 5
move 1 from 7 to 9
move 7 from 4 to 3
move 3 from 3 to 6
move 5 from 8 to 6
move 3 from 9 to 5
move 16 from 3 to 1
move 2 from 9 to 1
move 7 from 1 to 8
move 1 from 1 to 2
move 5 from 8 to 2
move 12 from 1 to 4
move 1 from 3 to 5
move 1 from 2 to 9
move 1 from 9 to 4
move 4 from 6 to 5
move 5 from 6 to 1
move 1 from 6 to 5
move 1 from 1 to 4
move 1 from 4 to 7
move 1 from 3 to 7
move 9 from 4 to 6
move 2 from 7 to 8
move 1 from 3 to 4
move 2 from 8 to 9
move 4 from 8 to 4
move 4 from 2 to 8
move 2 from 9 to 7
move 2 from 7 to 8
move 10 from 2 to 4
move 1 from 2 to 1
move 5 from 4 to 7
move 1 from 1 to 3
move 3 from 8 to 7
move 6 from 7 to 2
move 3 from 2 to 7
move 1 from 6 to 7
move 5 from 5 to 8
move 4 from 1 to 3
move 4 from 3 to 1
move 8 from 4 to 2
move 1 from 3 to 2
move 2 from 7 to 2
move 2 from 6 to 3
move 4 from 7 to 2
move 4 from 5 to 7
move 14 from 2 to 7
move 3 from 2 to 1
move 3 from 8 to 2
move 1 from 5 to 7
move 6 from 2 to 4
move 2 from 2 to 7
move 2 from 3 to 6
move 6 from 8 to 2
move 4 from 6 to 4
move 2 from 6 to 9
move 4 from 4 to 2
move 2 from 4 to 8
move 10 from 7 to 2
move 18 from 2 to 6
move 2 from 2 to 6
move 2 from 9 to 2
move 2 from 8 to 5
move 1 from 2 to 9
move 1 from 2 to 9
move 1 from 5 to 7
move 1 from 2 to 6
move 2 from 9 to 2
move 6 from 7 to 3
move 7 from 6 to 8
move 5 from 7 to 2
move 1 from 7 to 4
move 1 from 5 to 7
move 4 from 8 to 7
move 5 from 2 to 3
move 1 from 7 to 5
move 2 from 2 to 8
move 9 from 4 to 3
move 13 from 6 to 8
move 10 from 3 to 1
move 1 from 5 to 2
move 3 from 6 to 8
move 5 from 1 to 2
move 1 from 1 to 8
move 2 from 4 to 3
move 17 from 8 to 6
move 5 from 6 to 3
move 3 from 1 to 2
move 9 from 6 to 5
move 2 from 6 to 8
move 5 from 5 to 9
move 3 from 9 to 8
move 3 from 1 to 3
move 3 from 7 to 5
move 6 from 5 to 8
move 7 from 2 to 4
move 1 from 6 to 3
move 1 from 1 to 5
move 4 from 4 to 5
move 2 from 2 to 9
move 3 from 1 to 3
move 4 from 5 to 8
move 1 from 4 to 5
move 6 from 8 to 7
move 1 from 5 to 2
move 4 from 9 to 2
move 2 from 5 to 9
move 2 from 1 to 8
move 2 from 4 to 9
move 6 from 7 to 5
move 3 from 5 to 2
move 3 from 2 to 5
move 10 from 8 to 3
move 2 from 8 to 5
move 3 from 2 to 5
move 6 from 5 to 1
move 4 from 5 to 6
move 1 from 7 to 5
move 23 from 3 to 7
move 2 from 5 to 9
move 2 from 1 to 5
move 2 from 6 to 3
move 6 from 3 to 1
move 1 from 1 to 7
move 4 from 3 to 1
move 1 from 8 to 5
move 2 from 9 to 2
move 3 from 3 to 8
move 2 from 6 to 8
move 12 from 1 to 3
move 1 from 9 to 7
move 3 from 5 to 9
move 9 from 3 to 8
move 1 from 1 to 7
move 1 from 9 to 4
move 3 from 3 to 6
move 3 from 2 to 1
move 3 from 8 to 6
move 1 from 4 to 2
move 1 from 2 to 9
move 1 from 2 to 7
move 20 from 7 to 5
move 3 from 7 to 3
move 3 from 1 to 3
move 5 from 8 to 1
move 5 from 1 to 5
move 4 from 5 to 2
move 3 from 2 to 6
move 3 from 8 to 7
move 1 from 2 to 6
move 2 from 8 to 6
move 2 from 7 to 5
move 2 from 3 to 6
move 12 from 5 to 1
move 6 from 5 to 7
move 12 from 6 to 8
move 4 from 9 to 3
move 4 from 5 to 8
move 3 from 1 to 5
move 4 from 7 to 4
move 3 from 5 to 9
move 7 from 1 to 6
move 1 from 1 to 3
move 6 from 7 to 6
move 1 from 1 to 3
move 10 from 3 to 6
move 10 from 6 to 2
move 2 from 9 to 5
move 4 from 6 to 5
move 9 from 6 to 1
move 16 from 8 to 7
move 3 from 8 to 7
move 1 from 8 to 1
move 7 from 2 to 1
move 1 from 5 to 9
move 1 from 6 to 1
move 2 from 2 to 1
move 3 from 1 to 4
move 1 from 6 to 8
move 7 from 4 to 1
move 1 from 8 to 2
move 22 from 1 to 8
move 18 from 7 to 9
move 6 from 5 to 2
move 2 from 2 to 7
move 2 from 1 to 5
move 4 from 7 to 6
move 1 from 5 to 6
move 2 from 8 to 2
move 3 from 2 to 6
move 1 from 5 to 6
move 15 from 9 to 6
move 6 from 9 to 5
move 1 from 9 to 8
move 1 from 2 to 9
move 5 from 5 to 9
move 9 from 8 to 6
move 3 from 2 to 7
move 12 from 8 to 9
move 1 from 7 to 5
move 1 from 5 to 7
move 3 from 7 to 1
move 17 from 6 to 3
move 1 from 2 to 6
move 2 from 1 to 4
move 16 from 6 to 4
move 7 from 4 to 6
move 1 from 5 to 7
move 8 from 4 to 5
move 9 from 9 to 8
move 16 from 3 to 7
move 1 from 1 to 5
move 3 from 5 to 1
move 5 from 6 to 2
move 3 from 1 to 7
move 3 from 6 to 7
move 3 from 9 to 3
move 5 from 8 to 5
move 11 from 5 to 7
move 2 from 3 to 7
move 1 from 2 to 1
move 1 from 3 to 6
move 17 from 7 to 9
move 1 from 3 to 2
move 3 from 4 to 6
move 1 from 1 to 2
move 1 from 6 to 4
move 14 from 7 to 6
move 15 from 9 to 6
move 4 from 8 to 7
move 1 from 4 to 7
move 7 from 9 to 5
move 5 from 2 to 9
move 7 from 5 to 1
move 3 from 1 to 7
move 29 from 6 to 4
move 1 from 2 to 4
move 18 from 4 to 2
move 3 from 1 to 4
move 1 from 1 to 7
move 18 from 2 to 4
move 3 from 6 to 5
move 15 from 4 to 1
move 1 from 5 to 1
move 1 from 5 to 4
move 9 from 4 to 1
move 5 from 1 to 3
move 9 from 1 to 5
move 2 from 4 to 3
move 5 from 5 to 6
move 3 from 7 to 9
move 7 from 7 to 5
move 6 from 4 to 6
move 2 from 3 to 7
move 6 from 5 to 8
move 2 from 8 to 4
move 1 from 8 to 9
move 9 from 6 to 2
move 3 from 9 to 3
move 1 from 2 to 1
move 6 from 7 to 4
move 2 from 2 to 8
move 3 from 9 to 5
move 5 from 4 to 8
move 1 from 6 to 9
move 1 from 3 to 1
move 1 from 3 to 4
move 1 from 6 to 5
move 1 from 9 to 3
move 10 from 8 to 7
move 3 from 9 to 2
move 7 from 2 to 4
move 6 from 5 to 7
move 4 from 5 to 8
move 7 from 3 to 2
move 3 from 7 to 1
move 9 from 1 to 5
move 5 from 7 to 9
move 7 from 1 to 4
move 11 from 4 to 2
move 4 from 8 to 3
move 5 from 4 to 7
move 4 from 4 to 1
move 1 from 3 to 6
move 12 from 7 to 4
move 2 from 1 to 8
move 5 from 9 to 7
move 7 from 5 to 6
move 1 from 1 to 4
move 1 from 9 to 8
move 1 from 4 to 7
move 1 from 8 to 9
move 5 from 7 to 9
move 2 from 7 to 5
move 2 from 6 to 3
move 5 from 2 to 7
move 1 from 7 to 8
move 1 from 1 to 6
move 3 from 5 to 1"""

test_input = """    
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def main():
    first_question()
    second_question()


def first_question():
    stacks = {}
    for line in puzzle_input.split("\n"):
        if not line.strip():
            continue
        if line.startswith("move"):
            matches = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            quantity, from_stack, to_stack = (int(x) for x in matches.groups())
            for q in range(quantity):
                # pop from the top of the stack, meaning the last element (right)
                stacks[to_stack].append(stacks[from_stack].pop())
        else:
            # print the index of letters in the line
            indices = [m.start() for m in re.finditer(r"[a-zA-Z]", line)]
            crates = [m for m in re.findall(r"[a-zA-Z]", line)]
            for i, c in zip(indices, crates):
                index = i // 4 + 1
                if index not in stacks:
                    stacks[index] = deque()
                # we read the stack from the top, so we insert at the beginning
                stacks[index].appendleft(c)
            print(stacks)
    print(stacks)
    top_of_the_stacks = [stacks[i][-1] for i in sorted(stacks.keys())]
    print("".join(top_of_the_stacks))


def second_question():
    stacks = {}
    for line in puzzle_input.split("\n"):
        if not line.strip():
            continue
        if line.startswith("move"):
            matches = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            quantity, from_stack, to_stack = (int(x) for x in matches.groups())
            # pop from the top of the stack, meaning the last element (right)
            crates_popped = [stacks[from_stack].pop() for _ in range(quantity)]
            # reverse it, new feature of the CrateMover 9001
            crates_popped.reverse()
            for crate in crates_popped:
                stacks[to_stack].append(crate)
        else:
            # print the index of letters in the line
            indices = [m.start() for m in re.finditer(r"[a-zA-Z]", line)]
            crates = [m for m in re.findall(r"[a-zA-Z]", line)]
            for i, c in zip(indices, crates):
                index = i // 4 + 1
                if index not in stacks:
                    stacks[index] = deque()
                # we read the stack from the top, so we insert at the beginning
                stacks[index].appendleft(c)
            print(stacks)
    print(stacks)
    top_of_the_stacks = [stacks[i][-1] for i in sorted(stacks.keys())]
    print("".join(top_of_the_stacks))


if __name__ == '__main__':
    main()
