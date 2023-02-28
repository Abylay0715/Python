import pygame
import time
import random

pygame.init()

# Set up the display
width = 500
height = 500
display = pygame.display.set_mode((width, height))

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake block size and initial position
block_size = 10
x = 150
y = 150
x_change = 0
y_change = 0

# Set up the font for the score display
font = pygame.font.SysFont(None, 25)

# Set up the food block
food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

# Set up the snake
snake_list = []
snake_length = 1

# Set up the game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -block_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = block_size
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -block_size
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = block_size
                x_change = 0

    # Check if the snake hits the edges
    if x >= width or x < 0 or y >= height or y < 0:
        game_over = True

    # Update the snake's position
    x += x_change
    y += y_change

    # Fill the background with white
    display.fill(white)

    # Draw the food block
    pygame.draw.rect(display, red, [food_x, food_y, block_size, block_size])

    # Draw the snake blocks
    for i in range(len(snake_list)):
        pygame.draw.rect(display, black, [snake_list[i][0], snake_list[i][1], block_size, block_size])

    # Add the current position to the snake list
    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)

    # Remove the snake blocks if its length exceeds the current length
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check if the snake hit itself
    for block in snake_list[:-1]:
