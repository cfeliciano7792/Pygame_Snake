import pygame
import sys

pygame.init()

# create display screen - main window
screen = pygame.display.set_mode((400, 500))
# variable will represent framerate - How many times do we want our while loop to run
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # Make sure all code closes when the red X is clicked on the display window
            sys.exit()

    # Fill the main screen green
    screen.fill((175, 215, 72))
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
