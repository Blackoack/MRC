import re



class Intro:
    @staticmethod
    def display_intro():
        print("Welcome to the Mars Rover Control Program!🚀\n")
        print("This program allows you to simulate the movement of Mars rovers on a plateau.")
        print("You will be able to define the size of the plateau and deploy multiple rovers with specific starting positions and instructions.")
        print("Each rover can be instructed to turn left (L), turn right (R), or move forward (M).")
        print("The rovers cannot move outside the plateau boundaries or occupy the same position.")
        print("You can also instruct individual rovers after deployment.")
        print("Let's get started!\n")

class Plateau:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def is_inside(self, x, y):
        return 0 <= x <= self.width and 0 <= y <= self.height

    @staticmethod
    def get_plateau_input():
        while True:
            plateau_size = input("Enter the plateau size: ").strip().split()
            try:
                width, height = map(int, plateau_size)
                return width, height
            except (ValueError, TypeError):
                print("Invalid plateau size format. Please re-enter plateau size as e.g. '5 5'.")

class Rover:
    def __init__(self, x, y, direction, plateau):
        self.x = x
        self.y = y
        self.direction = direction
        self.plateau = plateau

    def move(self, rovers):
        new_x, new_y = self.x, self.y
        if self.direction == "N" and self.y < self.plateau.height:
            new_y += 1
        elif self.direction == "S" and self.y > 0:
            new_y -= 1
        elif self.direction == "E" and self.x < self.plateau.width:
            new_x += 1
        elif self.direction == "W" and self.x > 0:
            new_x -= 1

        for rover in rovers:
            if rover is not self and (new_x, new_y) == (rover.x, rover.y):
                print("Collision detected! Cannot move the rover to the same position!")
                return

        self.x, self.y = new_x, new_y

    def left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"

    def right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"

    def execute_instructions(self, instructions, rovers):
        for instruction in instructions:
            if instruction == "L":
                self.left()
            elif instruction == "R":
                self.right()
            elif instruction == "M":
                self.move(rovers)

    @staticmethod
    def get_rover_starting_position_input(occupied_positions, plateau):
        while True:
            rover_position = input("Enter the starting position of the rover: ")
            try:
                x, y, direction = rover_position.split()
                x, y = int(x), int(y)
                if re.match(r"^[NWES]$", direction):
                    if plateau.is_inside(x, y) and (x, y) not in occupied_positions:
                        return x, y, direction
                    else:
                        print("Position already occupied by another rover or outside of the plateau! Please choose a different position!")
                else:
                    print("Invalid rover facing direction! Please enter 'N', 'W', 'E', or 'S'.")
            except (ValueError, TypeError):
                print("Invalid rover position format! Please re-enter your position as e.g. '1 2 N'.")
                continue

    @staticmethod
    def get_instructions_input():
        while True:
            rover_instructions = input("Enter rover instructions: ")
            if re.match(r"^[LRM]*$", rover_instructions):
                return rover_instructions
            else:
                print("Invalid rover instructions format! Please use only 'L', 'R', and 'M' characters to move the rover around.")

    def __str__(self):
        return f"{self.x} {self.y} {self.direction}"

def main():
    Intro.display_intro()

    plateau_size = Plateau.get_plateau_input()
    plateau = Plateau(*plateau_size)

    rovers = []
    occupied_positions = set()

    while True:
        x, y, direction = Rover.get_rover_starting_position_input(occupied_positions, plateau)

        rover = Rover(x, y, direction, plateau)
        rovers.append(rover)
        occupied_positions.add((x, y))

        while True:
            rover_instructions = Rover.get_instructions_input()
            rover.execute_instructions(rover_instructions, rovers)
            print(f"Rover's current position: {rover}")

            while True:
                choice = input("Do you want to continue instructing the rover (yes/no)? ").strip().lower()
                if re.match(r"^\s*(yes|no)\s*$", choice):
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
            if choice == "no":
                break

        occupied_positions.remove((x, y))
        occupied_positions.add((rover.x, rover.y))

        while True:
            another_rover = input("Do you want to deploy another rover (yes/no)? ").strip().lower()
            if re.match(r"^\s*(yes|no)\s*$", another_rover):
                break
            else:
                print("Please enter 'yes' or 'no'.")
        if another_rover == "no":
            break

    for idx, rover in enumerate(rovers, start=1):
        print(f"Rover {idx}'s final position: {rover}")

    while True:
        try:
            rover_idx = int(input("Enter the number of the rover you want to instruct: ")) - 1
            if 0 <= rover_idx < len(rovers):
                rover = rovers[rover_idx]

                while True:
                    rover_instructions = Rover.get_instructions_input()
                    rover.execute_instructions(rover_instructions, rovers)
                    print(f"Rover {rover_idx + 1}'s current position: {rover}")

                    while True:
                        choice = input("Do you want to continue instructing this rover (yes/no)? ").strip().lower()
                        if re.match(r"^\s*(yes|no)\s*$", choice):
                            break
                        else:
                            print("Please enter ' yes' or 'no'.")
                    if choice == "no":
                        break

            else:
                print("Invalid rover number. Please enter a valid rover number or press Ctrl+C to exit.")
        except ValueError:
            print("Invalid input! Press Ctrl+C if you want to exit the program.")

        for idx, rover in enumerate(rovers, start=1):
            print(f"Rover {idx}'s final position: {rover}")



if __name__ == "__main__":
    main()