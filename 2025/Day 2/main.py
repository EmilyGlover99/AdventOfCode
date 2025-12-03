# Read file
with open('./ids.txt', 'r') as f:
        ids_list = f.read().split(',')


# Part 1
# invalid_ids = []
#
# for id_range in ids_list:
#     start_number, end_number = id_range.split('-')
#
#     for id_number in range(int(start_number), int(end_number) + 1):
#         if len(str(id_number)) % 2 == 0:
#             mid = len(str(id_number)) // 2
#             left = str(id_number)[:mid]
#             right = str(id_number)[mid:]
#
#             if left == right:
#                 print(str(id_number) + " is an invalid ID")
#                 invalid_ids.append(int(id_number))
# print(sum(invalid_ids))

# Part 2
invalid_ids = []

for id_range in ids_list:
    start_number, end_number = id_range.split('-')
    for id_number in range(int(start_number), int(end_number) + 1):
        divisors = [i for i in range(2, len(str(id_number)) + 1) if len(str(id_number)) % i == 0]
        for divisor in divisors:
            # Split the string into n = divisor parts
            part_length = len(str(id_number)) // divisor
            split_string_list = [str(id_number)[i*part_length:(i+1)*part_length] for i in range(divisor)]

            if len(set(split_string_list)) == 1:
                invalid_ids.append(id_number)
                break
print(sum(invalid_ids))




