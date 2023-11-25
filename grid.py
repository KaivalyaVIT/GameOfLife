# Simulation of Conway's Game of Life by - Kaivalya Sao

import pygame
import numpy as np

# Define colors
color_about_to_die = (200, 200, 225)
color_alive = (255, 255, 215)
color_background = (10, 10, 40)
color_grid = (30, 30, 60)

def update(surface, current_state, cell_size):
    # Create a new empty grid for the next state
    next_state = np.zeros((current_state.shape[0], current_state.shape[1]))

    # Iterate over each cell in the current state
    for row, col in np.ndindex(current_state.shape):
        # Count the number of alive neighbors
        num_alive = np.sum(current_state[row-1:row+2, col-1:col+2]) - current_state[row, col]

        # Apply the rules of the Game of Life to determine the next state of the cell
        if current_state[row, col] == 1 and (num_alive < 2 or num_alive > 3):
            cell_color = color_about_to_die
        elif (current_state[row, col] == 1 and 2 <= num_alive <= 3) or (current_state[row, col] == 0 and num_alive == 3):
            next_state[row, col] = 1
            cell_color = color_alive
        else:
            cell_color = color_background

        # Draw the cell on the surface
        pygame.draw.rect(surface, cell_color, (col*cell_size, row*cell_size, cell_size-1, cell_size-1))

    return next_state

def initialize(dim_x, dim_y):
    # Create an empty grid of cells
    cells = np.zeros((dim_y, dim_x))

    # Define a pattern to initialize some cells
    # pattern = np.array([[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1],
    #                     [0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1],
    #                     [1,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1],
    #                     [1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,0,1,1,0,0,0],
    #                     [1,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0],
    #                     [1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0],
    #                     [0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0],
    #                     [0,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0],
    #                     [1,1,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]])

    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);

    # Position the pattern in the center of the grid
    position = (dim_y // 2, (dim_x // 2) - 10)
    cells[position[0]:position[0]+pattern.shape[0], position[1]:position[1]+pattern.shape[1]] = pattern

    return cells

def main(dim_x, dim_y, cell_size):
    pygame.init()
    surface = pygame.display.set_mode((dim_x * cell_size, dim_y * cell_size))
    pygame.display.set_caption("Game of Life")

    cells = initialize(dim_x, dim_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(color_grid)
        cells = update(surface, cells, cell_size)
        pygame.display.update()

if __name__ == "__main__":
    main(60, 60, 10)