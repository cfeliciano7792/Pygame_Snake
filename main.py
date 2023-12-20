import pygame
import sys
import random
from pygame.math import Vector2


class Snake:

    def __init__(self):
        # holds list containing the blocks of the snake + starting position
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            # create rectangle
            x_position = block.x * cell_size
            y_position = block.y * cell_size
            block_rect = pygame.Rect(x_position, y_position, cell_size, cell_size)
            # draw rectangle
            pygame.draw.rect(screen, (0, 0, 225), block_rect)

    def move_snake(self):
        # copy of snake except for the last item
        body_copy = self.body[:-1]
        # Adding an element to the front of the list "head" of the snake
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


class Fruit:

    def __init__(self):
        self.randomize()
        # # create an x and y position - using randint to generate random position
        # self.x = random.randint(0, cell_number - 1)
        # self.y = random.randint(0, cell_number - 1)
        # # create a two-dimensional vector
        # self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        """
        Places a fruit onto the game screen. X and Y position are multiplied by cell_size to help
        give illusion of a grid
        """
        # create a rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        # draw rectangle on display screen
        pygame.draw.rect(screen, (126, 166, 100), fruit_rect)

    # create a random position and place the fruit there after eaten by snake
    def randomize(self):
        # create an x and y position - using randint to generate random position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        # create a two-dimensional vector
        self.pos = Vector2(self.x, self.y)


class Main:

    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        # check if head of snake is in the same position as fruit
        if self.fruit.pos == self.snake.body[0]:
            # reposition fruit
            self.fruit.randomize()
            # add a new block to snake


pygame.init()
cell_size = 40
cell_number = 19  # can change later
# create display screen - main window
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
# variable will represent framerate - How many times do we want our while loop to run
clock = pygame.time.Clock()

# Creating a custom event that will trigger every 150 milliseconds
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # Make sure all code closes when the red X is clicked on the display window
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        # This event will trigger when ever a button is pressed on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)
    # Fill the main screen green
    screen.fill((175, 215, 72))
    main_game.draw_elements()
    pygame.display.update()
    # framerate set to 60. Help with consistency across different devices
    clock.tick(60)

# pygame notes
# # Starts pygame modules
# pygame.init()
# # sets the display screen (main window) 400 width and 500 height
# screen = pygame.display.set_mode((400, 500))
# clock = pygame.time.Clock()
# test_surface = pygame.Surface((100, 200))
# test_surface.fill((0, 0, 255))
# # this will create a rectangle surface and draw it around my test_surface
# test_rect = test_surface.get_rect(center=(200, 250))
#
# while True:
#
#     for event in pygame.event.get():
#         # This event will close the game when pressing red X on display screen
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             # make sure that when we want to end the game all code stops running
#             sys.exit()
#
#     # screen.fill(pygame.Color('gold')) - One way to fill color within pygame or use RGB tuple below
#     screen.fill((175, 215, 72))
#
#     test_rect.right +=1
#     # screen.blit(surface name,(x pos, y pos)) - display a surface onto our main game display - top left of surface
#     screen.blit(test_surface, (test_rect))
#
#     # draw all our elements
#     pygame.display.update()
#     # clock.tick(framerate) - How many times do we want the while loop to run. Helps make games more consistent
#     # across multiple devices
#     clock.tick(60)

# pygame.Rect(xpos,ypos,width,height) - Draw a rectangle surface which provides more flexibility with placement
# test_rect = pygame.Rect(100, 200, 100, 100)

# pygame.draw.rect(surface, color, rectangle) - draw rectangle surfaces
# pygame.draw.rect(screen, pygame.Color('red'), test_rect)
