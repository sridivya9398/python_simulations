import math

# Function to move the robot based on the sequence of steps
def move_robot(step_sequence, initial_position):
    x, y = initial_position  

    for step in step_sequence:
        direction, steps = step.split()  
        steps = int(steps)  

        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps

    return [x, y]

# Function to calculate the Euclidean distance between two points
def calculate_distance(pos1, pos2):
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

def main():
    initial_x = int(input("Enter the initial X-coordinate: "))
    initial_y = int(input("Enter the initial Y-coordinate: "))
    initial_position = [initial_x, initial_y]

    n = int(input("Enter the number of steps: "))

    step_sequence = []
    for _ in range(n):
        step = input("Enter step (e.g., 'UP 5'): ")
        step_sequence.append(step)

    final_position = move_robot(step_sequence, initial_position)
    
    distance = calculate_distance(initial_position, final_position)

    print("Final position of the robot: ", final_position)
    print("Distance from initial position: {:.10f}".format(distance))

if __name__ == "__main__":
    main()
