puzzle_input = """addx 1
addx 4
addx -2
addx 3
addx 3
addx 1
noop
addx 5
noop
noop
noop
addx 5
addx 2
addx 3
noop
addx 2
addx 4
noop
addx -1
noop
addx 3
addx -10
addx -17
noop
addx -3
addx 2
addx 25
addx -24
addx 2
addx 5
addx 2
addx 3
noop
addx 2
addx 14
addx -9
noop
addx 5
noop
noop
addx -2
addx 5
addx 2
addx -5
noop
noop
addx -19
addx -11
addx 5
addx 3
noop
addx 2
addx 3
addx -2
addx 2
noop
addx 3
addx 4
noop
noop
addx 5
noop
noop
noop
addx 5
addx -3
addx 8
noop
addx -15
noop
addx -12
addx -9
noop
addx 6
addx 7
addx -6
addx 4
noop
noop
noop
addx 4
addx 1
addx 5
addx -11
addx 29
addx -15
noop
addx -12
addx 17
addx 7
noop
noop
addx -32
addx 3
addx -8
addx 7
noop
addx -2
addx 5
addx 2
addx 6
addx -8
addx 5
addx 2
addx 5
addx 17
addx -12
addx -2
noop
noop
addx 7
addx 9
addx -8
addx 2
addx -33
addx -1
addx 2
noop
addx 26
addx -22
addx 19
addx -16
addx 8
addx -1
addx 3
addx -2
addx 2
addx -17
addx 24
addx 1
noop
addx 5
addx -1
noop
addx 5
noop
noop
addx 1
noop
noop"""

test_input = """noop
addx 3
addx -5"""

test_input_2 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def main():
    first_question()
    second_question()


operation_duration = {
    "noop": 1,
    "addx": 2,
}

operation_function = {
    "noop": lambda *args: args[0],
    "addx": lambda *args: sum(args),
}


def first_question():
    current_input = puzzle_input
    cycle_count = 0
    register_value = 1
    signal_strengths = [20 + i*40 for i in range(6)]
    total_signal_strength = 0
    for line in current_input.split("\n"):
        instruction, *operands = line.split(" ")
        operands = list(map(int, operands))
        op_cycles = operation_duration[instruction]
        while op_cycles > 0:
            # beginning of cycle
            cycle_count += 1
            op_cycles -= 1
            if cycle_count in signal_strengths:
                total_signal_strength += register_value * cycle_count
                print(f"Signal strength {cycle_count} reached with value {register_value}")
            # end of cycle
            if op_cycles == 0:
                register_value = operation_function[instruction](*operands, register_value)
    print(f"Total signal strength is {total_signal_strength}")
    print(cycle_count, register_value)


def second_question():
    current_input = puzzle_input
    cycle_count = 0
    register_value = 1
    crt_screen = ["." for _ in range(40*6)]
    for line in current_input.split("\n"):
        instruction, *operands = line.split(" ")
        operands = list(map(int, operands))
        op_cycles = operation_duration[instruction]
        while op_cycles > 0:
            # beginning of cycle
            cycle_count += 1
            op_cycles -= 1
            position = cycle_count - 1
            if abs(position % 40 - register_value) <= 1:
                crt_screen[position] = "#"
            # end of cycle
            if op_cycles == 0:
                register_value = operation_function[instruction](*operands, register_value)
    for i in range(0, len(crt_screen), 40):
        print("".join(crt_screen[i:i+40]))

if __name__ == '__main__':
    main()
