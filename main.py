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

class Ship:
    def __init__(self, x, y, health=200):
        self.x = x
        self.y = y
        self.health = health
        self.shipImage = None
        self.laserImage = None
        self.lasers = []
        self.laserCooldown = 0
    
    def draw(self, window):
        #pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))
        window.blit(self.shipImage, (self.x, self.y))

def main():
    run = True
    framesPerSecond = 144
    lives = 3
    level = 1
    player_velocity = 2.5
    textFont = pygame.font.SysFont("comicsans", 20)
    ship = Ship(300, 650)
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

        ship.draw(WINDOW)
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
        # Creates dictionary of pressed keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ship.x - player_velocity > 0: #Move left
            ship.x -= player_velocity
        if keys[pygame.K_d]and ship.x + player_velocity < window_WIDTH: #Move right
            ship.x += player_velocity
        if keys[pygame.K_w] and ship.y - player_velocity > 0: #Move up
            ship.y -= player_velocity
        if keys[pygame.K_s] and ship.y + player_velocity < window_HEIGHT: #Move down
            ship.y += player_velocity
main()