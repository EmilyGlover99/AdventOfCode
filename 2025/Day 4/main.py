

def calculate_row_and_col_from_index(index, row_length):
    row_number = index // row_length
    col_number = index % row_length
    return row_number, col_number


def generate_adjacent_tiles(row, col):
    adjacent_tiles = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1),
                      (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    return adjacent_tiles


def run_paper_trials(paper_string, n_chars_per_line, remove_paper_rolls=False):
    accessible_paper_rolls_per_iteration = []
    some_paper_is_accessible = True
    while some_paper_is_accessible:

        accessible_paper_rolls = 0

        for char_num in range(0, len(paper_string)):
            if paper_string[char_num] == "@":
                row, col = calculate_row_and_col_from_index(char_num, n_chars_per_line)

                adjacent_tiles = generate_adjacent_tiles(row, col)

                adjacent_tile_counter = 0
                for tile in adjacent_tiles:
                    if 139 >= tile[0] >= 0 and 139 >= tile[1] >= 0:
                        tile_index = tile[0] * n_chars_per_line + tile[1]
                        tile_value = paper_string[tile_index]

                        if tile_value == "@":
                            adjacent_tile_counter += 1
                if adjacent_tile_counter <= 3:
                    accessible_paper_rolls += 1
                    if remove_paper_rolls:
                        paper_string = paper_string[:char_num] + "." + paper_string[char_num + 1:]

        accessible_paper_rolls_per_iteration.append(accessible_paper_rolls)

        if accessible_paper_rolls == 0 or not remove_paper_rolls:
            some_paper_is_accessible = False

    total_accessible_paper_rolls = sum(accessible_paper_rolls_per_iteration)
    return total_accessible_paper_rolls


with open('./paper_locations.txt', 'r') as f:
    paper_string = "".join(line.strip() for line in f.readlines())

part_1_solution = run_paper_trials(paper_string, n_chars_per_line=140)
part_2_solution = run_paper_trials(paper_string, n_chars_per_line=140, remove_paper_rolls=True)

print("Part 1 solution is: ", part_1_solution)
print("Part 2 solution is: ", part_2_solution)


