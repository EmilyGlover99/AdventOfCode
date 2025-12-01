

class Safe:

    def __init__(self, initial_location=50):
        self.current_location = initial_location
        self.location_history = [self.current_location]
        self.total_zeros = 0

    def execute_instruction(self, instruction):
        self.move_safe(instruction[0], int(instruction[1:]))
        self.location_history.append(self.current_location)

    def move_safe(self, direction, distance):
        if direction == 'L':
            self.move_left(distance)
        elif direction == 'R':
            self.move_right(distance)
        else:
            print("The direction must be 'L' or 'R'")

    def move_left(self, distance):
        distance_remainder = distance % 100
        complete_turns = distance // 100

        if self.current_location == 0:
            self.total_zeros += complete_turns
            self.current_location = 100 - distance_remainder

        else:
            self.total_zeros += complete_turns

            if self.current_location < distance_remainder:
                self.current_location = 100 - (distance_remainder - self.current_location)
                self.total_zeros += 1
            else:
                self.current_location -= distance_remainder
                if self.current_location == 0:
                    self.total_zeros += 1

    def move_right(self, distance):
        distance_remainder = distance % 100
        complete_turns = distance // 100

        if self.current_location == 0:
            self.total_zeros += complete_turns
            self.current_location = distance_remainder

        else:
            self.total_zeros += complete_turns

            if 99 < self.current_location + distance_remainder:
                self.current_location = (self.current_location + distance_remainder) - 100
                self.total_zeros += 1
            else:
                self.current_location += distance_remainder
                if self.current_location == 0:
                    self.total_zeros += 1

