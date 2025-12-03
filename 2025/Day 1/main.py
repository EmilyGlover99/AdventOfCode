from safe import Safe


class GetSafeCode:

    def __init__(self, safe_simulator, initial_safe_location=50, safe_instructions_list=None):
        self.safe_simulator = safe_simulator
        self.safe_instructions_list = safe_instructions_list
        self.current_safe_location = initial_safe_location

    def load_file_from_path(self, file_path):
        try:
            with open(file_path, 'r') as f:
                self.safe_instructions_list = f.read().split('\n')
        except FileNotFoundError:
            print(f"File {file_path} not found.")

    def crack_the_safe(self):

        for instruction in self.safe_instructions_list:
            self.safe_simulator.execute_instruction(instruction)

        safe_combination = self.safe_simulator.location_history.count(0)
        return safe_combination


safe_sim = Safe()

safe_cracker = GetSafeCode(safe_sim)
# safe_cracker.load_file_from_path('./Day 1/practise_code.txt')
safe_cracker.load_file_from_path('./Day 1/safe_code.txt')
solution = safe_cracker.crack_the_safe()
solution2 = safe_cracker.safe_simulator.total_zeros

print(f"There are {solution} 0\'s in the safe code!")
print(f"We both land on and pass 0 a total of {solution2} times")
