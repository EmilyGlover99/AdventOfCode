#
#
# n_chars_per_line = 140
#
# with open('./paper_locations.txt', 'r') as f:
#     paper_string = "".join(line.strip() for line in f.readlines())
#
# accessible_paper_roles = 0
# # some_paper_is_accessible = True
# # while (some_paper_is_accessible):
#
# for char_num in range(0, len(paper_string)):
#     if paper_string[char_num] == "@":
#         row = char_num // n_chars_per_line
#         col = char_num % n_chars_per_line
#
#         adjacent_tiles = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1),
#                           (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
#
#         adjacent_tile_counter = 0
#         for tile in adjacent_tiles:
#             if 139 >= tile[0] >= 0 and 139 >= tile[1] >= 0:
#                 tile_index = tile[0] * n_chars_per_line + tile[1]
#                 tile_value = paper_string[tile_index]
#
#                 if tile_value == "@":
#                     adjacent_tile_counter += 1
#         if adjacent_tile_counter <= 3:
#             accessible_paper_roles += 1
#
# print(accessible_paper_roles)

n_chars_per_line = 140

with open('./paper_locations.txt', 'r') as f:
    paper_string = "".join(line.strip() for line in f.readlines())

accessible_paper_roles_per_iteration = []
some_paper_is_accessible = True

while some_paper_is_accessible:

    accessible_paper_roles = 0

    for char_num in range(0, len(paper_string)):
        if paper_string[char_num] == "@":
            row = char_num // n_chars_per_line
            col = char_num % n_chars_per_line

            adjacent_tiles = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1),
                              (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

            adjacent_tile_counter = 0
            for tile in adjacent_tiles:
                if 139 >= tile[0] >= 0 and 139 >= tile[1] >= 0:
                    tile_index = tile[0] * n_chars_per_line + tile[1]
                    tile_value = paper_string[tile_index]

                    if tile_value == "@":
                        adjacent_tile_counter += 1
            if adjacent_tile_counter <= 3:
                accessible_paper_roles += 1
                # paper_string[char_num] = "."
                paper_string = paper_string[:char_num] + "." + paper_string[char_num + 1:]

    accessible_paper_roles_per_iteration.append(accessible_paper_roles)

    if accessible_paper_roles == 0:
        some_paper_is_accessible = False

total_accessible_paper_roles = sum(accessible_paper_roles_per_iteration)
print(total_accessible_paper_roles)





