import matplotlib.pyplot as plt
import numpy as np
import random

# Function to recursively draw branches, similar to a fractal neural network
def draw_branch(x, y, length, angle, depth, max_depth):
    if depth == max_depth:
        return
    
    # Calculate the end point of the current branch
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    
    # Choose a random color for added effect
    color = plt.cm.viridis(random.random())
    
    # Draw the branch
    plt.plot([x, x_end], [y, y_end], 'o-', color=color, markersize=3, linewidth=1)
    
    # Calculate new branches recursively
    new_length = length * 0.7  # Reduce the length for the next depth
    golden_angle = 2.39996323  # Golden angle in radians
    
    # Left branch
    draw_branch(x_end, y_end, new_length, angle - golden_angle, depth + 1, max_depth)
    # Right branch
    draw_branch(x_end, y_end, new_length, angle + golden_angle, depth + 1, max_depth)
    # more branches just for fun
    draw_branch(x_end, y_end, new_length, angle - golden_angle / 2, depth + 1, max_depth)
    draw_branch(x_end, y_end, new_length, angle + golden_angle / 2, depth + 1, max_depth)

# Main function to draw the neural-like fractal network
def draw_neural_fractal(x, y, initial_length, max_depth):
    plt.figure(figsize=(6, 6))  # Adjust the figure size for better zoom
    draw_branch(x, y, initial_length, -np.pi / 2, 0, max_depth)
    
    # Set display parameters to give it a clean look
    plt.axis('off')
    plt.gca().set_aspect('equal')
    plt.show()

# Draw the fractal neural network with starting point (0, 0), initial length of 1, and depth of 6
draw_neural_fractal(0, 0, 1, 6)
