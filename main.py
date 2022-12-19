import pygame
import time
import os
import random
pygame.font.init()

# Window initialisation
window_WIDTH, window_HEIGHT = 750, 750
WINDOW = pygame.display.set_mode((window_WIDTH, window_HEIGHT))
pygame.display.set_caption("Last Line of Defense")

# Background image
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")),(window_WIDTH, window_HEIGHT))

# Load alien ship asset images
ALIEN_GREEN = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
ALIEN_RED = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
ALIEN_BLUE= pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Load player ship asset image
PLAYER_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Load laser asset images
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

def main():
    run = True
    framesPerSecond = 144
    lives = 3
    level = 1
    textFont = pygame.font.SysFont("comicsans", 20)
    clock = pygame.time.Clock()
    # Checks for changes
    def redraw_window():
        # Set background image at top left corner
        WINDOW.blit(BACKGROUND,(0,0))
        # Render text
        lives_text = textFont.render(f"Lives: {lives}", 1, (0,255,0))
        level_text = textFont.render(f"Level: {level}", 1, (255,0,0))

        WINDOW.blit(lives_text, (window_WIDTH-level_text.get_width() - 20, 670))
        WINDOW.blit(level_text, (window_WIDTH-level_text.get_width() - 20, 700))
        pygame.display.update()
    # Provides consistent frames on devices 
    while run: 
        clock.tick(framesPerSecond)
        redraw_window()
        
        # Check for input
        for event in pygame.event.get():
            #Turn game off
            if event.type == pygame.QUIT:
                run = False
main()