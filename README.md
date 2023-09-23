Mars Rover Control Program

Welcome to the Mars Rover Control Program! This Python program allows you to simulate the movement of Mars rovers on a plateau.
You can define the size of the plateau and deploy multiple rovers with specific starting positions and instructions.
Each rover can be instructed to turn left (L), turn right (R), or move forward (M). The program ensures that the rovers cannot move outside the plateau boundaries or occupy the same position.

Table of Contents
Getting Started
Usage
Example
Contributing

To get started with the Mars Rover Control Program, follow these steps:

Getting Started

1. Clone this repository to your local machine:

git clone https://github.com/your-username/mars-rover-control.git
cd mars-rover-control

2. Make sure you have Python 3.x installed on your computer.
3. Run the program:

python mars_rover.py

4. Follow the on-screen instructions to input the plateau size, rover starting positions, and instructions.

Usage
-The program will prompt you to input the plateau size as two integers (e.g., "5 5").
-You can deploy multiple rovers one by one, specifying their starting positions (x, y) and facing direction (N, S, E, or W).
-For each rover, you can provide a series of instructions using 'L' (left), 'R' (right), and 'M' (move).
The rovers will follow these instructions on the plateau without colliding with each other or going out of bounds.
-After deploying all the rovers, you can choose to instruct individual rovers again.

Example
Here's an example of how to use the Mars Rover Control Program:

1. Input the plateau size:

Enter the plateau size: 5 5

2. Deploy first rover
   
Enter the starting position of the rover: 1 2 N
Enter rover instructions: LMLMLMLMM
Do you want to continue instructing the rover (yes/no)? no

3. Deploy the second rover:

Enter the starting position of the rover: 3 3 E
Enter rover instructions: MMRMMRMRRM
Do you want to continue instructing the rover (yes/no)? no

4. View the final positions of the rovers:

Rover 1's final position: 1 3 N
Rover 2's final position: 5 1 E

Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on this repository.
