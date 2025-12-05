

ids = []
id_ranges = []
line_has_broken = False

with open("./id_numbers.txt") as f:
    for line in f:
        if line_has_broken:
            ids.append(int(line))
        else:
            if line == "\n":
                line_has_broken = True
            else:
                id_ranges.append(line.replace("\n", "").split("-"))

# # Part 1
# good_ids = []
#
# for id_num in ids:
#     for id_range in id_ranges:
#         if int(id_range[0]) <= id_num <= int(id_range[1]):
#             good_ids.append(id_num)
#             break
#
# print("There are a total of ", len(good_ids), " good id's in the ranges provided.")


# Part 2
def check_overlap(range1, merged_ranges_list):
    overlapping_ranges = []
    for single_range in merged_ranges_list:
        if int(range1[0]) <= int(single_range[1]) and int(single_range[0]) <= int(range1[1]):
            overlapping_ranges.append(single_range)

    if overlapping_ranges:
        return True, overlapping_ranges
    return False, []


def merge(range_to_merge, overlapped_ranges, merged_ranges_list):
    for single_range in overlapped_ranges:
        merged_ranges_list.remove(single_range)
    new_range = [min(min([individual_range[0] for individual_range in overlapped_ranges]), int(range_to_merge[0])), max(max([individual_range[1] for individual_range in overlapped_ranges]), int(range_to_merge[1]))]
    merged_ranges_list.append(new_range)


merged_ranges = []
for id_range in id_ranges:
    overlap, overlapping_ranges = check_overlap(id_range, merged_ranges)
    if overlap:
        merge(id_range, overlapping_ranges, merged_ranges)
    else:
        merged_ranges.append([int(id_range[0]), int(id_range[1])])

range_distance = [single_range[1] - single_range[0] + 1 for single_range in merged_ranges]
print("The sum of non-overlapping ranges is: ", sum(range_distance))
