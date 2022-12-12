from collections import deque
from dataclasses import dataclass, field
import numpy as np


test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

puzzle_input = """abccccccccccccccccccaaaaaaaaacccccccccccccccccccccccccccccccccccccaaaa
abcccccccccccccccaaaaaaaaaaacccccccccccccccccccccccccccccccccccccaaaaa
abcaaccaacccccccccaaaaaaaaaacccccccccccccccccccccaaacccccccccccccaaaaa
abcaaaaaaccccccccaaaaaaaaaaaaacccccccccccccccccccaacccccccccccccaaaaaa
abcaaaaaacccaaacccccaaaaaaaaaaaccccccccccccccccccaaaccccccccccccccccaa
abaaaaaaacccaaaaccccaaaaaacaaaacccccccccccaaaacjjjacccccccccccccccccca
abaaaaaaaaccaaaaccccaaaaaaccccccaccccccccccaajjjjjkkcccccccccccccccccc
abaaaaaaaaccaaacccccccaaaccccccaaccccccccccajjjjjjkkkaaacccaaaccaccccc
abccaaacccccccccccccccaaccccaaaaaaaacccccccjjjjoookkkkaacccaaaaaaccccc
abcccaacccccccccccccccccccccaaaaaaaaccccccjjjjoooookkkkcccccaaaaaccccc
abcccccccaacccccccccccccccccccaaaacccccccijjjoooooookkkkccaaaaaaaccccc
abccaaccaaaccccccccccccccccccaaaaacccccciijjooouuuoppkkkkkaaaaaaaacccc
abccaaaaaaaccccccccccaaaaacccaacaaaccciiiiiooouuuuupppkkklllaaaaaacccc
abccaaaaaacccccccccccaaaaacccacccaaciiiiiiqooouuuuuupppkllllllacaccccc
abcccaaaaaaaacccccccaaaaaaccccaacaiiiiiqqqqoouuuxuuupppppplllllccccccc
abccaaaaaaaaaccaaaccaaaaaaccccaaaaiiiiqqqqqqttuxxxuuuppppppplllccccccc
abccaaaaaaaacccaaaaaaaaaaacccaaaahiiiqqqttttttuxxxxuuuvvpppplllccccccc
abcaaaaaaacccaaaaaaaaaaacccccaaaahhhqqqqtttttttxxxxuuvvvvvqqlllccccccc
abcccccaaaccaaaaaaaaaccccccccacaahhhqqqttttxxxxxxxyyyyyvvvqqlllccccccc
abcccccaaaccaaaaaaaacccccccccccaahhhqqqtttxxxxxxxyyyyyyvvqqqlllccccccc
SbcccccccccccaaaaaaaaaccccccccccchhhqqqtttxxxxEzzzyyyyvvvqqqmmlccccccc
abcccccccccccaaaaaaaacccaacccccccchhhppptttxxxxyyyyyvvvvqqqmmmcccccccc
abccccccccccaaaaaaaaaaccaacccccccchhhpppptttsxxyyyyyvvvqqqmmmccccccccc
abcaacccccccaaaaaaacaaaaaaccccccccchhhppppsswwyyyyyyyvvqqmmmmccccccccc
abaaaacccccccaccaaaccaaaaaaacccccccchhhpppsswwyywwyyyvvqqmmmddcccccccc
abaaaaccccccccccaaaccaaaaaaacccccccchhhpppsswwwwwwwwwvvqqqmmdddccccccc
abaaaacccccccccaaaccaaaaaaccccccccccgggpppsswwwwrrwwwwvrqqmmdddccccccc
abccccccaaaaaccaaaacaaaaaaccccccaacccggpppssswwsrrrwwwvrrqmmdddacccccc
abccccccaaaaaccaaaacccccaaccccaaaaaacggpppssssssrrrrrrrrrnmmdddaaccccc
abcccccaaaaaaccaaaccccccccccccaaaaaacggppossssssoorrrrrrrnnmdddacccccc
abcccccaaaaaaccccccccaaaaccccccaaaaacgggoooossoooonnnrrnnnnmddaaaacccc
abccccccaaaaaccccccccaaaacccccaaaaaccgggoooooooooonnnnnnnnndddaaaacccc
abccccccaaaccccccccccaaaacccccaaaaacccgggoooooooffennnnnnnedddaaaacccc
abcccccccccccccccccccaaacccccccaacccccggggffffffffeeeeeeeeeedaaacccccc
abccccccccccccccccccaaacccccaccaaccccccggfffffffffeeeeeeeeeecaaacccccc
abccccccccccccccccccaaaacccaaaaaaaaaccccfffffffaaaaaeeeeeecccccccccccc
abccccccccaacaaccccaaaaaacaaaaaaaaaaccccccccccaaaccaaaaccccccccccccccc
abccccccccaaaaacccaaaaaaaaaaacaaaaccccccccccccaaaccccaaccccccccccaaaca
abcccccccaaaaaccccaaaaaaaaaaacaaaaacccccccccccaaaccccccccccccccccaaaaa
abcccccccaaaaaacccaaaaaaaaaacaaaaaacccccccccccaaccccccccccccccccccaaaa
abcccccccccaaaaccaaaaaaaaaaaaaaccaaccccccccccccccccccccccccccccccaaaaa"""

def char_to_elevation(char: str):
    if char.islower():
        return ord(char) - ord("a")
    else:
        return {
            "S": char_to_elevation("a"),
            "E": char_to_elevation("z"),
        }.get(char)


def main():
    first_question()
    second_question()

def first_question():
    current_input = puzzle_input
    grid = np.array([list(line) for line in current_input.split("\n")])
    starting_position = tuple(np.array(np.where(grid == "S")).reshape(2))
    goal_position = tuple(np.array(np.where(grid == "E")).reshape(2))
    grid = np.vectorize(char_to_elevation)(grid)
    queue = deque()
    queue.append((0, *starting_position))
    visited = {starting_position}
    while queue:
        l, x, y = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_y < 0 or new_x >= grid.shape[0] or new_y >= grid.shape[1]:
                continue
            if (new_x, new_y) in visited:
                continue
            if grid[(new_x, new_y)] - grid[(x, y)] > 1:
                continue
            if (new_x, new_y) == goal_position:
                print(l + 1)
                return
            visited.add((new_x, new_y))
            queue.append((l + 1, new_x, new_y))

def second_question():
    current_input = puzzle_input
    grid = np.array([list(line) for line in current_input.split("\n")])
    starting_positions = [(x, y) for x, y in np.argwhere(grid == "a")]
    goal_position = tuple(np.array(np.where(grid == "E")).reshape(2))
    grid = np.vectorize(char_to_elevation)(grid)
    ls = []
    for starting_position in starting_positions:
        queue = deque()
        queue.append((0, *starting_position))
        visited = {starting_position}
        while queue:
            l, x, y = queue.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_y < 0 or new_x >= grid.shape[0] or new_y >= grid.shape[1]:
                    continue
                if (new_x, new_y) in visited:
                    continue
                if grid[(new_x, new_y)] - grid[(x, y)] > 1:
                    continue
                if (new_x, new_y) == goal_position:
                    ls.append(l + 1)
                    break
                visited.add((new_x, new_y))
                queue.append((l + 1, new_x, new_y))
    print(max(ls))
    print(min(ls))

if __name__ == "__main__":
    main()