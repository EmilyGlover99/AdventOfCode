import itertools

# Read file
with open('./batteries.txt', 'r') as f:
        batteries_list = f.read().split('\n')


# Part 1

# bank_values = []
#
# for bank in batteries_list:
#     two_sets = itertools.combinations(list(map(int, str(bank))), 2)
#     combined = [int(str(x) + str(y)) for (x, y) in two_sets]
#     bank_values.append(max(combined))
#
# print(bank_values)
# sum = int(sum(bank_values))
# print(sum)

# Part 2

final_numbers = []

for bank in batteries_list:
    # Take the last 12 digits to be the first try:
    final_number = list(bank[-12:])
    final_number_indices = []


    for i in range(0, 12):
        # Find the next best value for each digit
        if i == 0:
            remaining_digits = bank[:len(bank) - 12 + 1]
            largest_remaining_digit = max(remaining_digits)
            index_of_first_largest_digit = remaining_digits.index(largest_remaining_digit)
            final_number[i] = largest_remaining_digit
            final_number_indices.append(index_of_first_largest_digit)
        else:
            remaining_digits = bank[final_number_indices[i - 1] + 1: (len(bank) - 12) + i + 1]
            largest_remaining_digit = max(remaining_digits)
            index_of_first_largest_digit = remaining_digits.index(largest_remaining_digit) + int(final_number_indices[i - 1] + 1)

            final_number[i] = largest_remaining_digit
            final_number_indices.append(index_of_first_largest_digit)

    combined = int("".join(map(str, final_number)))

    final_numbers.append(combined)

print(sum(final_numbers))



