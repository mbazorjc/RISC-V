import time
import os

# Set the number of disks
NUM_DISKS = 3

# Dictionary representing the 3 pegs and their current disks
# Peg A starts with all disks (e.g., [3, 2, 1]), B and C are empty
pegs = {
    'A': list(range(NUM_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def draw_pegs():
    """
    ITERATION DEMONSTRATION:
    This function uses iteration (for loops) to traverse the data structure 
    and draw the current state of the pegs row by row.
    """
    # Clear the terminal screen for a smooth animation effect
    os.system('clear' if os.name == 'posix' else 'cls')
    print("Tower of Hanoi Simulation\n")
    
    # Loop from the top row down to the bottom
    for i in range(NUM_DISKS - 1, -1, -1):
        row_string = ""
        # Loop through each peg to construct the row visually
        for peg in ['A', 'B', 'C']:
            if len(pegs[peg]) > i:
                disk_size = pegs[peg][i]
                # Draw the disk using '=' characters
                disk_visual = "=" * (disk_size * 2)
                row_string += disk_visual.center(NUM_DISKS * 2 + 2)
            else:
                # Draw the empty peg using a '|' character
                row_string += "|".center(NUM_DISKS * 2 + 2)
        print(row_string)
        
    # Draw the base
    print("-" * ((NUM_DISKS * 2 + 2) * 3))
    print("A".center(NUM_DISKS * 2 + 2) + "B".center(NUM_DISKS * 2 + 2) + "C".center(NUM_DISKS * 2 + 2))
    print("\n")
    
    # Pause so the user can see the animation
    time.sleep(0.8)

def move_tower(n, source, target, auxiliary):
    """
    RECURSION DEMONSTRATION:
    This function calls itself to break down the problem into smaller, 
    identical sub-problems until it hits the base case.
    """
    # Base Case & Condition: If n is 0, we do nothing. 
    # If n > 0, we proceed with the recursive steps.
    if n > 0:
        # Step 1 (Recursive): Move n-1 disks from Source to Auxiliary
        move_tower(n - 1, source, auxiliary, target)

        # Step 2 (Action): Move the largest remaining disk from Source to Target
        disk = pegs[source].pop()
        pegs[target].append(disk)
        draw_pegs() # Update the graphics after moving

        # Step 3 (Recursive): Move the n-1 disks from Auxiliary to Target
        move_tower(n - 1, auxiliary, target, source)

# --- Main Execution ---
if __name__ == "__main__":
    # Draw the initial state
    draw_pegs()
    # Start the recursive solver
    move_tower(NUM_DISKS, 'A', 'C', 'B')
    print("Puzzle Complete!")
