import pygame
import time
import os
import random
pygame.font.init()

# Window initialisation
window_WIDTH, window_HEIGHT = 1000, 1000
WINDOW = pygame.display.set_mode((window_WIDTH, window_HEIGHT))
pygame.display.set_caption("Last Line of Defense")

# Background image
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets/Blue Nebula", "Blue_Nebula_01-1024x1024.png")),(window_WIDTH, window_HEIGHT))

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

# Super class ship for both player and enemy
class Ship:
    COOLDOWN = 72
    def __init__(self, x, y, health=200):
        self.x = x
        self.y = y
        self.health = health
        self.shipImage = None
        self.laserImage = None
        self.laserCooldown = 0
        self.lasers = []
    
    # Draw player and enemy ships
    def draw(self, window):
        #pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))
        window.blit(self.shipImage, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(WINDOW)

    def shoot(self):
        if self.laserCooldown == 0:
            laser = Laser(self.x, self.y, self.laserImage)
            self.lasers.append(laser)
            self.laserCooldown = 1
    def cooldown(self):
        if self.laserCooldown >= self.COOLDOWN:
            self.laserCooldown = 0
        elif self.laserCooldown > 0:
            self.laserCooldown += 1
    # Checks if player is hit by laser and moves the laser
    def move_lasers(self, velocity, object):
        self.cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_screen(window_HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(object):
                object.health -= 10
                # To hit player only once with the same laser
                self.lasers.remove(laser)

    def getWidth(self):
        return self.shipImage.get_width()
    
    def getHeight(self):
        return self.shipImage.get_height()

#Player ship
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.shipImage = PLAYER_SHIP
        self.laserImage = YELLOW_LASER
        # Mask for collision detection
        self.mask = pygame.mask.from_surface(self.shipImage)
        self.maxHealth = health

    def move_lasers(self, velocity, objects):
        self.cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_screen(window_HEIGHT):
                self.lasers.remove(laser)
            else:
                for object in objects:
                    #Remove enemy ship and laser from game if it is hit by the player
                    if laser.collision(object):
                        objects.remove(object)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, windowBar):
        super().draw(windowBar)
        self.healthbar(windowBar)

    def healthbar(self, windowBar):
        # Red part of health bar(missing health)
        pygame.draw.rect(windowBar, (255, 0, 0), (self.x, self.y + self.shipImage.get_height() + 10, self.shipImage.get_width(), 10))
        # Green part of healthbar
        pygame.draw.rect(windowBar, (0, 255, 0), (self.x, self.y + self.shipImage.get_height() + 10, self.shipImage.get_width() * (self.health/self.maxHealth), 10))
# Enemy ships
class Enemy(Ship):
    shipColor_Map = {
        "red": (ALIEN_RED, RED_LASER),
        "green": (ALIEN_GREEN, GREEN_LASER),
        "blue": (ALIEN_BLUE, BLUE_LASER)
    }
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.shipImage, self.laserImage = self.shipColor_Map[color]
        # Mask for collision detection
        self.mask = pygame.mask.from_surface(self.shipImage)
    
    def moveDown(self, velocity):
        self.y += velocity
    
    def shoot(self):
        if self.laserCooldown == 0:
            laser = Laser(self.x-15, self.y, self.laserImage)
            self.lasers.append(laser)
            self.laserCooldown = 1
# Laser projectiles
class Laser:
    def __init__(self, x, y, laserImage):
        self.x = x
        self.y = y
        self.laserImage = laserImage
        self.mask = pygame.mask.from_surface(self.laserImage)
    
    def draw(self, window):
        window.blit(self.laserImage, (self.x, self.y))


    def move(self, velocity):
        self.y += velocity
    
    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)
    
    def collision(self, obj):
        return collide(self, obj)

def collide(object1, object2):
    # calculate offset to know distance between objects
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    #if the masks of both objects overlap 
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None

def main():
    run = True
    lost = False
    lostTime = 0
    gameOverFont = pygame.font.Font(os.path.join("fonts", "Reboot Crush.ttf"), 15)
    framesPerSecond = 144
    lives = 3
    level = 0
    player_velocity = 2
    enemy_velocity = 0.5
    laser_velocity_enemy = 1
    laser_velocity_player = -3.5
    player = Player(450, 700)
    enemies = []
    enemyPerWave = 5
    clock = pygame.time.Clock()
    # Checks for changes
    def redraw_window():
        # Set background image at top left corner
        WINDOW.blit(BACKGROUND,(0,0))
        # Render text
        lives_text = gameOverFont.render(f"Lives: {lives}", 1, (0,255,0))
        level_text = gameOverFont.render(f"Level: {level}", 1, (255,255,255))
        WINDOW.blit(lives_text, (window_WIDTH-level_text.get_width() - 20, 920))
        WINDOW.blit(level_text, (window_WIDTH-level_text.get_width() - 20, 950))

        for enemy in enemies:
            enemy.draw(WINDOW)
        
        player.draw(WINDOW)
        if lost:
            game_over_text = gameOverFont.render("GAME OVER", 1, (255,0,0))
            WINDOW.blit(game_over_text, (window_WIDTH/2 - game_over_text.get_width()/2, 350))
        
        pygame.display.update()
    # Provides consistent frames on devices 
    while run: 
        clock.tick(framesPerSecond)
        redraw_window()
        # Game over
        if lives <= 0 or player.health <= 0:
            lost = True
            lostTime += 1
        
        # Game over message time
        if lost:
            if lostTime > framesPerSecond * 3:
                run = False
            else:
                continue

        # Start next wave of enemies after all have been killed
        if len(enemies) == 0:
            level +- 1
            enemyPerWave += 5
            # Spawn enemies
            for i in range(enemyPerWave):
                enemy = Enemy(random.randrange(50, window_WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        # Check for input
        for event in pygame.event.get():
            #Turn game off
            if event.type == pygame.QUIT:
                run = False
        # Creates dictionary of pressed keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_velocity > 0: #Move left
            player.x -= player_velocity
        if keys[pygame.K_d]and player.x + player_velocity + player.getWidth() < window_WIDTH: #Move right
            player.x += player_velocity
        if keys[pygame.K_w] and player.y - player_velocity > 0: #Move up
            player.y -= player_velocity
        if keys[pygame.K_s] and player.y + player_velocity + player.getHeight() + 20 < window_HEIGHT: #Move down
            player.y += player_velocity
        if keys[pygame.K_SPACE]:
            player.shoot()

        # Enemy behaviour
        for enemy in enemies[:]:
            enemy.moveDown(enemy_velocity)
            enemy.move_lasers(laser_velocity_enemy, player)
            # Enemies shoot randomly
            if random.randrange(0, 5*framesPerSecond) == 1:
                enemy.shoot()
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            #If the enemies reach the bottom, lose a life
            elif enemy.y + enemy.getHeight() > window_HEIGHT:
                lives -= 1
                enemies.remove(enemy)
        
        player.move_lasers(laser_velocity_player, enemies)
def main_menu():
    titleFont = pygame.font.Font(os.path.join("fonts", "THE SOLSTICE.ttf"), 25)
    run = True
    while run:
        WINDOW.blit(BACKGROUND, (0,0))
        title_text = titleFont.render("Last Line of Defense", 1, 'yellow')
        instruction_text = titleFont.render("Click to play...", 1, 'white')
        WINDOW.blit(title_text, (window_WIDTH/2 - title_text.get_width()/2, 120))
        WINDOW.blit(instruction_text, (window_WIDTH/2 - instruction_text.get_width()/2, 800))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()