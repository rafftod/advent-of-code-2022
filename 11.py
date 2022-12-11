from dataclasses import dataclass
from math import prod
import sys

puzzle_input = """Monkey 0:
  Starting items: 74, 64, 74, 63, 53
  Operation: new = old * 7
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 1:
  Starting items: 69, 99, 95, 62
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 5

Monkey 2:
  Starting items: 59, 81
  Operation: new = old + 8
  Test: divisible by 7
    If true: throw to monkey 4
    If false: throw to monkey 3

Monkey 3:
  Starting items: 50, 67, 63, 57, 63, 83, 97
  Operation: new = old + 4
  Test: divisible by 13
    If true: throw to monkey 0
    If false: throw to monkey 7

Monkey 4:
  Starting items: 61, 94, 85, 52, 81, 90, 94, 70
  Operation: new = old + 3
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 3

Monkey 5:
  Starting items: 69
  Operation: new = old + 5
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 2

Monkey 6:
  Starting items: 54, 55, 58
  Operation: new = old + 7
  Test: divisible by 11
    If true: throw to monkey 1
    If false: throw to monkey 5

Monkey 7:
  Starting items: 79, 51, 83, 88, 93, 76
  Operation: new = old * 3
  Test: divisible by 2
    If true: throw to monkey 0
    If false: throw to monkey 6"""

test_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


@dataclass
class Monkey:
    starting_items: list[int]
    operation: str
    test_divisor: int
    test_success_recipient: int
    test_failure_recipient: int
    number_of_inspections: int = 0

    def update_worry_level(self, item_index: int) -> None:
        self.starting_items[item_index] = eval(self.operation.replace("old", str(self.starting_items[item_index])))

    def test(self, worry_level: int) -> True:
        return worry_level % self.test_divisor == 0



def main():
    first_question()
    second_question()


def first_question():
    solve_question()


def solve_question(worry_reduction: bool = True, number_of_rounds: int = 20):
    current_input = puzzle_input
    monkey_list = []
    for line in current_input.split("\n"):
        if "Monkey" in line:
            monkey_list.append(Monkey([], None, None, None, None))
        elif "Starting items" in line:
            monkey_list[-1].starting_items = list(map(int, line.split(": ")[1].split(", ")))
        elif "Operation" in line:
            monkey_list[-1].operation = line.split(": ")[1].split(" = ")[1]
        elif "Test" in line:
            monkey_list[-1].test_divisor = int(line.split("by ")[1])
        elif "If true" in line:
            monkey_list[-1].test_success_recipient = int(line.split(" ")[-1])
        elif "If false" in line:
            monkey_list[-1].test_failure_recipient = int(line.split(" ")[-1])
    # product of all divisors
    total_divisor = prod([monkey.test_divisor for monkey in monkey_list])
    # process rounds of the game
    for _ in range(number_of_rounds):
        for m, monkey in enumerate(monkey_list):
            print(f"Monkey {monkey_list.index(monkey)} (items {monkey.starting_items}):")
            items_to_remove = []
            for item_index, __ in enumerate(monkey.starting_items):
                print(f"  Monkey inspects an item with a worry level of {monkey.starting_items[item_index]}.")
                monkey.number_of_inspections += 1
                monkey.update_worry_level(item_index)
                print(f"    Monkey updates the worry level to {monkey.starting_items[item_index]}.")
                if worry_reduction:
                    monkey.starting_items[item_index] = monkey.starting_items[item_index] // 3
                    print(f"    Monkey divides the worry level by 3 to get {monkey.starting_items[item_index]}.")
                recipient = monkey.test_success_recipient if monkey.test(monkey.starting_items[item_index]) else monkey.test_failure_recipient
                value_to_pass = monkey.starting_items[item_index] % total_divisor
                print(f"    Monkey passes the worry level to monkey {recipient} with a value of {value_to_pass}.")
                monkey_list[recipient].starting_items.append(value_to_pass)
                items_to_remove.append(item_index)
            for item_index in sorted(items_to_remove, reverse=True):
                monkey.starting_items.pop(item_index)
        # print results
        print(f"Round {_ + 1} results:")
        for monkey in monkey_list:
            print(f"Monkey {monkey_list.index(monkey)}: {monkey.number_of_inspections}.")
    # print final results
    print("Final results:")
    for monkey in monkey_list:
        print(f"Monkey {monkey_list.index(monkey)} inspected {monkey.number_of_inspections} times.")
    print(
        f"Level of monkey business is {prod(monkey.number_of_inspections for monkey in sorted(monkey_list, key=lambda m: m.number_of_inspections, reverse=True)[:2])}.")


def second_question():
    solve_question(worry_reduction=False, number_of_rounds=10000)


if __name__ == '__main__':
    main()
