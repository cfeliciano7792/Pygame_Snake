import pygame
import sys
import random
from pygame.math import Vector2


class Snake:

    def __init__(self):
        # holds list containing the blocks of the snake + starting position
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

    def draw_snake(self):

        self.update_head_graphics()
        self.update_tail_graphics()
        # enumerate used to see block before and after
        # index is the index we are on while block is the object we are looking at
        for index, block in enumerate(self.body):
            x_position = int(block.x * cell_size)
            y_position = int(block.y * cell_size)
            block_rect = pygame.Rect(x_position, y_position, cell_size, cell_size)

            # What direction is the snake moving?
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                # checks to see if a vertical block or horizontal block should be used
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                # Check for corner blocks
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        # when snake eats a fruit only one new block is added to the snake
        if self.new_block:
            # copy of snake
            body_copy = self.body[:]
            # Adding an element to the front of the list "head" of the snake
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            # prevents multiple blocks being added to the snake when a fruit is eaten
            self.new_block = False
        else:
            # copy of snake except for the last item
            body_copy = self.body[:-1]
            # Adding an element to the front of the list "head" of the snake
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


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
        screen.blit(apple, fruit_rect)
        # draw rectangle on display screen
        # pygame.draw.rect(screen, (126, 166, 100), fruit_rect)

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
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        # check if head of snake is in the same position as fruit
        if self.fruit.pos == self.snake.body[0]:
            # reposition fruit
            self.fruit.randomize()
            # add a new block to snake
            self.snake.add_block()

    def check_fail(self):
        # check if snake goes off-screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # check if snake hits its self
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 20))
        score_x = int(cell_size*cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x,score_y))
        screen.blit(score_surface, score_rect)

pygame.init()
cell_size = 40
cell_number = 20  # can change later
# create display screen - main window
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
# variable will represent framerate - How many times do we want our while loop to run
clock = pygame.time.Clock()

# adds an image and converts it to a format that pygame can use
apple = pygame.image.load('Graphics/apple.png').convert_alpha()

# creating a font to use in game
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

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
                # prevents snake from moving up if it is currently moving down
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                # prevents snake from moving left if it is currently moving right
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
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
