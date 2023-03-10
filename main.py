import pygame
import time
import os
import random
from pygame import mixer
pygame.init()
pygame.font.init()

# Window initialisation
window_WIDTH, window_HEIGHT = 1024, 1024
WINDOW = pygame.display.set_mode((window_WIDTH, window_HEIGHT))
pygame.display.set_caption("Last Line of Defense")

# Load player ship asset image
PLAYER_SHIP = pygame.image.load(
    os.path.join("assets/player", "shipFullHealth.png"))
PLAYER_SHIP_SLIGHTDAMAGE = pygame.image.load(
    os.path.join("assets/player", "shipSlightDamage.png"))
PLAYER_SHIP_DAMAGED = pygame.image.load(
    os.path.join("assets/player", "shipDamaged.png"))
PLAYER_SHIP_VERYDAMAGED = pygame.image.load(
    os.path.join("assets/player", "shipVeryDamaged.png"))
ENGINE_SHIP = pygame.image.load(
    os.path.join("assets/player", "shipEngine.png"))

# Set game icon
pygame.display.set_icon(PLAYER_SHIP)

# Load and scale background images for levels and main menu
BACKGROUNDMAINMENU = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "MainMenuBackground.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL1 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Blue Nebula", "Blue_Nebula_01-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL2 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Blue Nebula", "Blue_Nebula_02-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL3 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Blue Nebula", "Blue_Nebula_03-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL4 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Blue Nebula", "Blue_Nebula_04-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL5 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Blue Nebula", "Blue_Nebula_05-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL6 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Blue Nebula", "Blue_Nebula_06-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL7 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Blue Nebula", "Blue_Nebula_07-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL8 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Blue Nebula", "Blue_Nebula_08-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL9 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Green Nebula", "Green_Nebula_01-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL10 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Green Nebula", "Green_Nebula_02-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL11 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Green Nebula", "Green_Nebula_03-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL12 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Green Nebula", "Green_Nebula_04-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL13 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Green Nebula", "Green_Nebula_05-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL14 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Green Nebula", "Green_Nebula_06-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL15 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Green Nebula", "Green_Nebula_07-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL16 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Green Nebula", "Green_Nebula_08-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL17 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Purple Nebula", "Purple_Nebula_01-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL18 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Purple Nebula", "Purple_Nebula_02-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL19 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Purple Nebula", "Purple_Nebula_03-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL20 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Purple Nebula", "Purple_Nebula_04-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL21 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Purple Nebula", "Purple_Nebula_05-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL22 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Purple Nebula", "Purple_Nebula_06-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL23 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Purple Nebula", "Purple_Nebula_07-1024x1024.png")), (window_WIDTH, window_HEIGHT))
BACKGROUNDL24 = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets/Purple Nebula", "Purple_Nebula_08-1024x1024.png")), (window_WIDTH, window_HEIGHT))


# Background Sound
mixer.music.load(os.path.join("audio", "background.wav"))
mixer.music.play(-1)
enemyKilledSound = mixer.Sound(os.path.join(
    "audio", "enemyKilled.wav"))
bulletSound = mixer.Sound(os.path.join(
    "audio", "bullet.wav"))
lifeLostSound = mixer.Sound(os.path.join(
    "audio", "lifeLost.wav"))
gameOverSound = mixer.Sound(os.path.join(
    "audio", "gameOver.wav"))
powerUpSound = mixer.Sound(os.path.join(
    "audio", "powerUp.wav"))
winSound = mixer.Sound(os.path.join(
    "audio", "win.wav"))


# Load alien ship asset images
ALIEN_GREEN1 = pygame.image.load(os.path.join(
    "assets/aliens", "aliengreen1.png"))
ALIEN_RED1 = pygame.image.load(os.path.join(
    "assets/aliens", "alienred1.png"))
ALIEN_RED2 = pygame.image.load(os.path.join(
    "assets/aliens", "alienred2.png"))
ALIEN_CYAN1 = pygame.image.load(os.path.join(
    "assets/aliens", "aliencyan1.png"))
ALIEN_YELLOW1 = pygame.image.load(os.path.join(
    "assets/aliens", "alienyellow1.png"))
ALIEN_BOSS = pygame.image.load(os.path.join(
    "assets/aliens", "alienBoss.png"))
ALIEN_BLUE1 = pygame.image.load(os.path.join(
    "assets/aliens", "alienblue1.png"))
ALIEN_PURPLE1 = pygame.image.load(os.path.join(
    "assets/aliens", "alienpurple1.png"))
ALIEN_PURPLE2 = pygame.image.load(os.path.join(
    "assets/aliens", "alienpurple2.png"))

# Load laser asset images
GREEN_LASER = pygame.image.load(
    os.path.join("assets/lasers", "greenlaser.png"))
RED_LASER = pygame.image.load(os.path.join("assets/lasers", "redlaser.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets/lasers", "bluelaser.png"))
YELLOW_LASER = pygame.image.load(
    os.path.join("assets/lasers", "yellowlaser.png"))
PURPLE_LASER = pygame.image.load(
    os.path.join("assets/lasers", "purplelaser.png"))
PURPLE_BULLET = pygame.image.load(
    os.path.join("assets/lasers", "alienbullet.png"))
PLAYER_LASER = pygame.image.load(
    os.path.join("assets/lasers", "bullet.png"))

# Power ups images
HEALTH_POWER = pygame.image.load(
    os.path.join("assets/powerups", "healthPower.png"))
DAMAGE_POWER = pygame.image.load(
    os.path.join("assets/powerups", "damagePower.png"))
COOLDOWN_POWER = pygame.image.load(
    os.path.join("assets/powerups", "cooldownPower.png"))

# Super class ship for both player and enemy


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
        self.shipImage = None
        self.laserImage = None
        self.engineImage = None
        self.laserCooldown = 0
        self.lasers = []
        self.lives = 3
        self.hit = 0
    # Draw player and enemy ships

    def draw(self, window):
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
                object.health -= 25
                if (object.health < 100 and object.health >= 75):
                    object.shipImage = PLAYER_SHIP_SLIGHTDAMAGE
                elif (object.health < 75 and object.health >= 50):
                    object.shipImage = PLAYER_SHIP_DAMAGED
                elif (object.health < 50 and object.health > 0):
                    object.shipImage = PLAYER_SHIP_VERYDAMAGED
                else:
                    object.lives -= 1
                    lifeLostSound.play()
                    object.health = 100
                    object.shipImage = PLAYER_SHIP
                # To hit player only once with the same laser
                self.lasers.remove(laser)

    def getWidth(self):
        return self.shipImage.get_width()

    def getHeight(self):
        return self.shipImage.get_height()


# Player ship


class Player(Ship):
    DEPLETIOND = 25
    DEPLETIONC = 50

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.shipImage = PLAYER_SHIP
        self.laserImage = PLAYER_LASER
        self.engineImage = ENGINE_SHIP
        # Mask for collision detection
        self.mask = pygame.mask.from_surface(self.shipImage)
        self.kills = 0
        self.score = 0
        self.doubleLaser = False
        self.halfCooldown = False
        self.untilNextLevel = 4
        self.idleEngineSprites = []
        self.moveEngineSprites = []
        self.maxHealth = health
        self.is_moving = False
        self.idleEngineSprites.append(pygame.image.load(
            os.path.join("assets/player", "idle1.png")))
        self.idleEngineSprites.append(pygame.image.load(
            os.path.join("assets/player", "idle2.png")))
        self.idleEngineSprites.append(pygame.image.load(
            os.path.join("assets/player", "idle3.png")))
        self.moveEngineSprites.append(pygame.image.load(
            os.path.join("assets/player", "moving1.png")))
        self.moveEngineSprites.append(pygame.image.load(
            os.path.join("assets/player", "moving2.png")))
        self.moveEngineSprites.append(pygame.image.load(
            os.path.join("assets/player", "moving3.png")))
        self.currentengineSprite = 0
        self.engineTrailSprite = self.idleEngineSprites[self.currentengineSprite]

    def move_lasers(self, velocity, objects):
        self.cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_screen(window_HEIGHT):
                self.lasers.remove(laser)
            else:
                for object in objects:
                    # Remove enemy ship and laser from game if it is hit by the player
                    if laser.collision(object):
                        object.health -= 50
                        object.hit += 1
                        if (object.health <= 0):
                            self.kills += 1
                            enemyKilledSound.play()
                            self.untilNextLevel -= 1
                            if (object.maxHealth == 100):
                                self.score += object.maxHealth
                            elif (object.maxHealth == 500):
                                self.score += object.maxHealth
                            else:
                                self.score += object.maxHealth
                            objects.remove(object)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, windowBar):
        super().draw(windowBar)
        windowBar.blit(self.engineImage, (self.x+26, self.y+50))
        windowBar.blit(self.engineTrailSprite, (self.x+25, self.y+53))
        self.update()
        self.healthbar(windowBar)

    def moving(self):
        self.is_moving = True
        self.engineTrailSprite = self.moveEngineSprites[self.currentengineSprite]

    def idle(self):
        self.is_moving = False
        self.engineTrailSprite = self.idleEngineSprites[self.currentengineSprite]

    def healthbar(self, windowBar):
        # Red part of health bar(missing health)
        pygame.draw.rect(windowBar, (255, 0, 0), (self.x, self.y +
                         self.shipImage.get_height() + 10, self.shipImage.get_width(), 10))
        # Green part of healthbar
        pygame.draw.rect(windowBar, (0, 255, 0), (self.x, self.y + self.shipImage.get_height() +
                         10, self.shipImage.get_width() * (self.health/self.maxHealth), 10))

    def update(self):
        if self.is_moving == True:
            self.currentengineSprite += 1
            if self.currentengineSprite >= len(self.moveEngineSprites):
                self.currentengineSprite = 0
            self.engineTrailSprite = self.moveEngineSprites[self.currentengineSprite]
        elif self.is_moving == False:
            self.currentengineSprite += 1
            if self.currentengineSprite >= len(self.idleEngineSprites):
                self.currentengineSprite = 0
            self.engineTrailSprite = self.idleEngineSprites[self.currentengineSprite]

    def shoot(self):
        if self.doubleLaser == False:
            if self.laserCooldown == 0:
                laser = Laser(self.x+25, self.y, self.laserImage)
                self.lasers.append(laser)
                self.laserCooldown = 1
                bulletSound.play()
                if (self.halfCooldown == True):
                    self.COOLDOWN = 10
                    self.DEPLETIONC -= 1
                    if (self.DEPLETIONC <= 0):
                        self.halfCooldown = False
                        self.COOLDOWN = 30
                        self.DEPLETIONC = 50

        else:
            if self.laserCooldown == 0:
                laser1 = Laser(self.x+50, self.y, self.laserImage)
                laser2 = Laser(self.x, self.y, self.laserImage)
                self.lasers.append(laser1)
                self.lasers.append(laser2)
                self.laserCooldown = 1
                bulletSound.play()
                bulletSound.play()
                self.DEPLETIOND -= 1
                if (self.DEPLETIOND <= 0):
                    self.doubleLaser = False
                    self.DEPLETIOND = 25
                if (self.halfCooldown == True):
                    self.COOLDOWN = 10
                    self.DEPLETIONC -= 1
                    if (self.DEPLETIONC <= 0):
                        self.halfCooldown = False
                        self.COOLDOWN = 30
                        self.DEPLETIONC = 50

# Enemy ships


class Enemy(Ship):
    shipColor_Map = {
        "red1": (ALIEN_RED1, RED_LASER),
        "red2": (ALIEN_RED2, RED_LASER),
        "green1": (ALIEN_GREEN1, GREEN_LASER),
        "blue1": (ALIEN_BLUE1, BLUE_LASER),
        "cyan1": (ALIEN_CYAN1, BLUE_LASER),
        "yellow1": (ALIEN_YELLOW1, YELLOW_LASER),
        "purple1": (ALIEN_PURPLE1, PURPLE_BULLET),
        "purple2": (ALIEN_PURPLE2, PURPLE_LASER),
        "boss": (ALIEN_BOSS, RED_LASER)
    }

    def __init__(self, x, y, color, health=50):
        super().__init__(x, y, health)
        self.shipImage, self.laserImage = self.shipColor_Map[color]
        # Mask for collision detection
        self.mask = pygame.mask.from_surface(self.shipImage)
        self.maxHealth = health

    def draw(self, windowBar):
        super().draw(windowBar)
        if (self.hit > 0):
            self.healthbar(windowBar)

    def moveDown(self, velocity):
        self.y += velocity

    def shoot(self):
        if self.laserCooldown == 0:
            laser = Laser(self.x+23, self.y+50, self.laserImage)
            self.lasers.append(laser)
            self.laserCooldown = 1

    def healthbar(self, windowBar):
        # Red part of health bar(missing health)
        pygame.draw.rect(windowBar, (255, 0, 0), (self.x, self.y +
                         self.shipImage.get_height() + 10, self.shipImage.get_width(), 10))
        # Green part of healthbar
        pygame.draw.rect(windowBar, (0, 255, 0), (self.x, self.y + self.shipImage.get_height() +
                         10, self.shipImage.get_width() * (self.health/self.maxHealth), 10))

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
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

# Power ups


class PowerUp:
    powerUpType = {
        "heal": HEALTH_POWER,
        "damage": DAMAGE_POWER,
        "cooldown": COOLDOWN_POWER
    }

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.powerImage = self.powerUpType[type]
        self.mask = pygame.mask.from_surface(self.powerImage)

    def draw(self, window):
        window.blit(self.powerImage, (self.x, self.y))

    def moveDown(self, velocity):
        self.y += velocity

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, player):
        return collide(self, player) != None

    def activate(self, player):
        if (self.collision(player) != None):
            powerUpSound.play()
            if (self.powerUpType[self.type] == HEALTH_POWER):
                player.health = player.maxHealth
                player.shipImage = PLAYER_SHIP
            elif (self.powerUpType[self.type] == DAMAGE_POWER):
                player.doubleLaser = True
            else:
                player.halfCooldown = True

    def getHeight(self):
        return self.powerImage.get_height()


def collide(object1, object2):
    # calculate offset to know distance between objects
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    # if the masks of both objects overlap
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None


def main():
    run = True
    lost = False
    lostTime = 0
    winTime = 0
    win = False
    gameOverFont = pygame.font.Font(
        os.path.join("fonts", "Reboot Crush.ttf"), 15)
    untilNextLevelFont = pygame.font.Font(
        os.path.join("fonts", "Reboot Crush.ttf"), 10)
    framesPerSecond = 60
    level = 0
    player_velocity = 5
    enemy_velocity = 0.8
    laser_velocity_enemy = 2
    laser_velocity_player = -5
    player = Player(450, 700)
    enemies = []
    powers = []
    enemyPerWave = 4
    levels = {
        "1": BACKGROUNDL1,
        "2": BACKGROUNDL2,
        "3": BACKGROUNDL3,
        "4": BACKGROUNDL4,
        "5": BACKGROUNDL5,
        "6": BACKGROUNDL6,
        "7": BACKGROUNDL7,
        "8": BACKGROUNDL8,
        "9": BACKGROUNDL9,
        "10": BACKGROUNDL10,
        "11": BACKGROUNDL11,
        "12": BACKGROUNDL12,
        "13": BACKGROUNDL13,
        "14": BACKGROUNDL14,
        "15": BACKGROUNDL15,
        "16": BACKGROUNDL16,
        "17": BACKGROUNDL17,
        "18": BACKGROUNDL18,
        "19": BACKGROUNDL19,
        "20": BACKGROUNDL20,
        "21": BACKGROUNDL21,
        "22": BACKGROUNDL22,
        "23": BACKGROUNDL23,
        "24": BACKGROUNDL24
    }
    currentLevelBackground = BACKGROUNDMAINMENU

    clock = pygame.time.Clock()
    # Checks for changes

    def redraw_window():
        WINDOW.blit(currentLevelBackground, (0, 0))
        # Render text
        lives_text = gameOverFont.render(
            f"Lives: {player.lives}", 1, (0, 255, 0))
        level_text = gameOverFont.render(f"Level: {level}", 1, (255, 255, 255))
        kills_text = gameOverFont.render(
            f"Total kills: {player.kills}", 1, 'orange')
        untilNextLevel_text = untilNextLevelFont.render(
            f"Until next level: {player.untilNextLevel}", 1, 'red')
        WINDOW.blit(lives_text, (window_WIDTH -
                    lives_text.get_width() - 20, 920))
        WINDOW.blit(level_text, (window_WIDTH -
                    level_text.get_width() - 20, 950))
        WINDOW.blit(kills_text, (740, 855))
        WINDOW.blit(untilNextLevel_text, (775, 890))
        score_text = gameOverFont.render(
            f"Score: {player.score}", 1, (255, 255, 255))
        for enemy in enemies:
            enemy.draw(WINDOW)
        for power in powers:
            power.draw(WINDOW)
        player.draw(WINDOW)
        if lost:
            game_over_text = gameOverFont.render("GAME OVER", 1, (255, 0, 0))
            WINDOW.blit(game_over_text, (window_WIDTH/2 -
                        game_over_text.get_width()/2, 350))
            WINDOW.blit(score_text, (window_WIDTH/2 -
                        score_text.get_width()/2, 400))
        if win:
            win_text = gameOverFont.render("YOU WIN!", 1, (0, 255, 0))
            WINDOW.blit(win_text, (window_WIDTH/2 -
                        win_text.get_width()/2, 350))
            WINDOW.blit(score_text, (window_WIDTH/2 -
                        score_text.get_width()/2, 400))

        pygame.display.update()
    # Provides consistent frames on devices
    while run:
        clock.tick(framesPerSecond)
        redraw_window()
        # Game over
        if player.lives <= 0:
            lost = True
            lostTime += 1
            gameOverSound.play()

        # Game over message time
        if lost:
            if lostTime > framesPerSecond * 5:
                run = False
            else:
                continue

        if win:
            winTime += 1
            if winTime > framesPerSecond * 3:
                run = False
            else:
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    main_menu()

        # Start next wave of enemies after all have been killed
        if len(enemies) == 0:
            if (level == 24):
                win = True
                winTime += 1
                winSound.play()
            else:
                level += 1
            if (level % 5 == 0):
                player.lives += 1
            enemy_velocity *= 1.02
            laser_velocity_enemy *= 1.01
            player_velocity *= 1.02
            laser_velocity_player *= 1.02
            player.COOLDOWN *= 0.98
            for item in levels.keys():
                if (level == int(item)):
                    currentLevelBackground = levels[item]
            enemyPerWave += 2
            for i in range(int(level/3)):
                power = PowerUp(random.randrange(50, window_WIDTH-100),
                                random.randrange(int((level*-200)-1000), -100), random.choice(["heal", "damage", "cooldown"]))
                powers.append(power)
            player.untilNextLevel = enemyPerWave
            levelUpSound = mixer.Sound(os.path.join(
                "audio", "levelUp.wav"))
            levelUpSound.play()

            # Spawn enemies
            if (level < 3):
                for i in range(enemyPerWave):
                    enemytype = random.choice(["red1", "yellow1", "green1"])
                    enemy = Enemy(random.randrange(50, window_WIDTH-100),
                                  random.randrange(-1000, -100), enemytype)
                    enemies.append(enemy)
            elif (level >= 3 and level < 5):
                for i in range(enemyPerWave):
                    enemytype = random.choice(
                        ["red1", "yellow1", "blue1", "green1"])
                    enemy = Enemy(random.randrange(50, window_WIDTH-100),
                                  random.randrange(-1200, -100), enemytype)
                    enemies.append(enemy)
            elif (level >= 5 and level < 8):
                for i in range(enemyPerWave):
                    enemytype = random.choice(
                        ["red1", "cyan1", "yellow1", "purple1", "blue1", "green1"])
                    enemy = Enemy(random.randrange(50, window_WIDTH-100),
                                  random.randrange(-1400, -100), enemytype)
                    enemies.append(enemy)
            elif (level >= 8 and level < 10):
                for i in range(enemyPerWave):
                    enemytype = random.choice(
                        ["red1", "red2", "yellow1", "purple1", "purple2", "blue1", "green1"])
                    enemy = Enemy(random.randrange(50, window_WIDTH-100),
                                  random.randrange(-1600, -100), enemytype)
                    if (enemytype == "purple2" or enemytype == "red2"):
                        enemy.health = 100
                        enemy.maxHealth = 100
                    enemies.append(enemy)
            elif (level >= 10):
                boss = Enemy(random.randrange(50, window_WIDTH-100),
                             random.randrange(-1800, -100), "boss")
                boss.health = 500
                boss.maxHealth = 500
                enemies.append(boss)
                for i in range(enemyPerWave-1):
                    enemytype = random.choice(
                        ["red1", "red2", "yellow1", "purple1", "purple2", "blue1", "green1"])
                    enemy = Enemy(random.randrange(50, window_WIDTH-100),
                                  random.randrange(enemyPerWave*-85, -100), enemytype)
                    if (enemytype == "purple2" or enemytype == "red2"):
                        enemy.health = 100
                        enemy.maxHealth = 100
                    enemies.append(enemy)

        # Check for input
        for event in pygame.event.get():
            # Turn game off
            if event.type == pygame.QUIT:
                run = False
        # Creates dictionary of pressed keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_velocity > 0:  # Move left
            player.x -= player_velocity
            player.idle()
        if keys[pygame.K_d] and player.x + player_velocity + player.getWidth() < window_WIDTH:  # Move right
            player.x += player_velocity
            player.idle()
        if keys[pygame.K_w] and player.y - player_velocity > 0:  # Move up
            player.y -= player_velocity
            player.moving()
        else:
            player.idle()
        if keys[pygame.K_s] and player.y + player_velocity + player.getHeight() + 20 < window_HEIGHT:  # Move down
            player.y += player_velocity
            player.idle()
        if keys[pygame.K_SPACE]:
            player.shoot()
            WINDOW.blit(player.laserImage, (player.x+25, player.y))

        # Enemy behaviour
        for enemy in enemies[:]:
            enemy.moveDown(enemy_velocity)
            enemy.move_lasers(laser_velocity_enemy, player)
            # Enemies shoot randomly
            if random.randrange(0, 5*framesPerSecond) == 1:
                enemy.shoot()
            if collide(enemy, player):
                player.health -= 25
                enemy.health -= 50
                enemy.hit += 1
                if (enemy.health <= 0):
                    enemyKilledSound.play()
                    player.kills += 1
                    player.untilNextLevel -= 1
                    if (enemy.maxHealth == 100):
                        player.score += enemy.maxHealth
                    elif (enemy.maxHealth == 500):
                        player.score += enemy.maxHealth
                    else:
                        player.score += enemy.maxHealth
                    enemies.remove(enemy)
                if (player.health < 100 and player.health >= 75):
                    player.shipImage = PLAYER_SHIP_SLIGHTDAMAGE
                elif (player.health < 75 and player.health >= 50):
                    player.shipImage = PLAYER_SHIP_DAMAGED
                elif (player.health < 50 and player.health > 0):
                    player.shipImage = PLAYER_SHIP_VERYDAMAGED
                else:
                    player.lives -= 1
                    lifeLostSound.play()
                    player.health = 100
                    player.shipImage = PLAYER_SHIP
            # If the enemies reach the bottom, lose a life
            elif enemy.y + enemy.getHeight() > window_HEIGHT:
                player.lives -= 1
                lifeLostSound.play()
                enemies.remove(enemy)
                player.untilNextLevel -= 1

        for power in powers[:]:
            power.moveDown(enemy_velocity)
            if collide(power, player):
                power.activate(player)
                powers.remove(power)
            elif power.y + power.getHeight() > window_HEIGHT+40:
                powers.remove(power)

        player.move_lasers(laser_velocity_player, enemies)


def main_menu():
    titleFont = pygame.font.Font(os.path.join("fonts", "THE SOLSTICE.ttf"), 25)
    run = True
    while run:
        WINDOW.blit(BACKGROUNDMAINMENU, (0, 0))
        title_text = titleFont.render("Last Line of Defense", 1, 'yellow')
        instruction_text = titleFont.render("Click to play...", 1, 'white')
        WINDOW.blit(title_text, (window_WIDTH/2 -
                    title_text.get_width()/2, 120))
        WINDOW.blit(instruction_text, (window_WIDTH/2 -
                    instruction_text.get_width()/2, 450))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()
