import itertools

# Read file
with open('./batteries.txt', 'r') as f:
        batteries_list = f.read().split('\n')

bank_values = []

for bank in batteries_list:
    two_sets = itertools.combinations(list(map(int, str(bank))), 2)
    combined = [int(str(x) + str(y)) for (x, y) in two_sets]
    bank_values.append(max(combined))

print(bank_values)
sum = int(sum(bank_values))
print(sum)
