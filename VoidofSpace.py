# Name: Colin A. Lewis
# Class: Coding, App, & Game Design - A.M. - Mr. Ball
# Date: Friday, December 10th 2021 - Tuesday, February 1st 2022.

# imports pygame Module
import pygame

# Imports the os (Operating System)
import os

# imports the time module (of use for setting a max of 60 FPS (Frames Per Second))
import time

# imports random as rd
import random as rd

# imports mixer from pygame to allow for .mp3, .wav etc... to be functionable.
from pygame import mixer

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    K_SPACE,
    QUIT,
)

# Creates the window width & height and initializes the title/caption.

WIDTH = 1500

HEIGHT = 1000

# -----------------------------------------------------------------------------------------------------------------------

# sets the display's width, height and the game caption.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Void_of_Space")

# ------------------------------------------------------------------------------------------------------------------------

# weapon fired by the player ship
pWeapon = pygame.image.load(os.path.join("Images/pngs/base-ball.png"))

# ------------------------------------------------------------------------------------------------------------------------

# Enemy ship(s)
Enemy = pygame.image.load(os.path.join("Images/Graphics Asset - Spaceships/PNG/Spaceships/04/Spaceship_04_RED.png"))

# Weapon fired by enemies.
eWeapon = pygame.image.load(os.path.join("Images/pngs/tennis-ball.png"))


# -----------------------------------------------------------------------------------------------------------------------


class player(pygame.sprite.Sprite):
    def __init__(self):
        super(player, self).__init__()
        self.moveCount = 0
        PlayerShip_vel = False
        Moving = False
        self.shipSpeed = 20
        currentLevel = 1
        playerHealth = 100000
        self.isDying = False
        ShipChoice = ["./Images/Graphics Asset - Spaceships/PNG/Spaceships/03/Spaceship_03_BLUE.png"]
        pImage = rd.choice(ShipChoice)
        self.surf = pygame.image.load(pImage)
        self.rect = self.surf.get_rect(
            center=(
                (WIDTH / 2),
                (HEIGHT - 15)
            )
        )

    # updates the screen for each animation / sprite
    '''  def playerDeath(self, keys):

        deathAnimation = pygame.image.load("Images/Explosion/5.png", "Images/Explosion/6.png", "Images/Explosion/7.png", "Images/Explosion/8.png", "Images/Explosion/9.png", "Images/Explosion/10.png", "Images/Explosion/11.png")


        if self.playerVel < len(shipAnimation):

            self.playerVel = 0
        self.surf = pygame.image.load(shipAnimation[self.playerVel ]).convert_alpha
        self.playerVel += 2

        if self.playerVel < len(deathAnimation):

            self.Death = 0
        self.surf = pygame.image.load(deathAnimation[self.playerVel ]).convert_alpha
    '''

    def pos(self):
        return self.rect.midbottom

    def update(self, keys):

        if keys[K_UP]:
            self.rect.move_ip(0, -self.shipSpeed)

        if keys[K_LEFT]:  # Left
            self.rect.move_ip(-self.shipSpeed, 0)

        if keys[K_DOWN]:  # Downwards
            self.rect.move_ip(0, self.shipSpeed)
        if keys[K_RIGHT]:  # Right
            self.rect.move_ip(self.shipSpeed, 0)

        # Keep the player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


# creates a primary weapon for the ship using the base_ball sprite.
class Primary(pygame.sprite.Sprite):

    def __init__(self, weapon_vel, ship_weapon, y, x):
        super().__init__()
        self.ship_weapon = pygame.image.load("Images/pngs/base-ball.png")

        primary = player

        self.weapon_vel = weapon_vel
        self.update = self.screenUpdate
        screen = self.screen.Update()

        self.x = x
        self.y = y

    # Updates the screen everytime the player fires the weapon by pressing space.
    def updateScreen(self, keys, weapon_vel, ship_weapon):
        pWeapon = pygame.image.load("Images/pngs/base-ball.png")
        self.shoot = weapon_vel
        pygame.display.update()

        if [K_SPACE] == pygame.key.get_pressed():
            shoot = self.shoot

    def draw(self, Primary):
        screen = pygame.display.rect(screen, self.ship_weapon.weapon_vel(-60, 0))
        pygame.display.update()


# creates class: Enemy.
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 100
        self.enemyShip_vel = 0
        self.weapon_vel = 0

        self.eShip = "eShip"
        self.weapon = weapon_vel
        self.weapon_img = eWeapon

    # Plays a death animation everytime a enemy has been downed by the player.
    def deathAnimation(self, Enemy):
        enemyExplosion = pygame.image.load("Images/Explosion/Explosion-2/11.png", "Images/Explosion/Explosion-2/12.png",
                                           "Images/Explosion/Explosion-2/13.png", "Images/Explosion/Explosion-2/14.png",
                                           "Images/Explosion/Explosion-2/15.png", "Images/Explosion/Explosion-2/16.png",
                                           "Images/Explosion/Explosion-2/17.png", "Images/Explosion/Explosion-2/18.png",
                                           "Images/Explosion/Explosion-2/19.png", "Images/Explosion/Explosion-2/20.png",
                                           "Images/Explosion/Explosion-2/21.png", "Images/Explosion/Explosion-2/22.png")
        pygame.display.update()

        if enemyShip_vel < len(enemyExplosion):
            self.enemy_Vel = 0
            self.surf = pygame.image.load(enemyExplosion[enemyShip_vel]).convert_alpha
            self.enemy_Vel += 0
            self.kill()


class engineThrust(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.flameCount = 0
        self.dead = False
        self.FlameAnimation = ["./Images/Graphics Asset - Spaceships/PNG/Flame_01.png",
                                "./Images/Graphics Asset - Spaceships/PNG/Flame_02.png"]

        self.surf = pygame.image.load(self.FlameAnimation[0]).convert_alpha()
        self.rect = self.surf.get_rect(

            midtop=((player.pos()[0]), 600),


                    )

    def update(self):
        if self.dead:
            self.kill()
        else:
            if self.flameCount > len(self.FlameAnimation) - 1:
                self.flameCount = 0
            self.surf = pygame.image.load(self.FlameAnimation [ self.flameCount ]).convert_alpha()
            self.flameCount += 1
            self.rect = self.surf.get_rect(center=(player.rect.left + 250, player.rect.bottom - 100))


# The enemy primary weapon.
class enemyWeapon:
    def __init__(self, weapon_vel, ship_weapon, x, y):
        self.ship_weapon = pygame.image.load("Images/pngs/tennis-ball.png")
        primary = eShip
        self.weapon_vel = weapon_vel
        self.update = updateScreen

    # Updates the screen each time the enemy fires their weapon directly at the player ship.
    def updateScreen(self, weapon_vel, ship_weapon, eWeapon):
        eWeapon = pygame.image.load("Images/pngs/tennis-ball.png")
        pygame.display.update()
        self.shoot = weapon_vel, ship_weapon

        if posit == player:
            eWeapon = shoot


# Detects when the player gets hit or hits an enemy ship / collides with it.
class Collision:
    def __init__(self, x, y, ship_weapon):
        self.x = x
        self.y = y

    def collisions(self, pShip, eShip, x, y):
        rect = pygame(playerShip.get_rect())

        if Collision == playerShip.get_rect():
            collide = pWeapon.updateScreen()
            pygame.display.update()


# Adds a fire rate for the player.
class fireRate:
    def __init__(self, firing, x, y, pWeapon):

        if self.firing == True:

            self.pWeapon = pWeapon(-45)
            self.pWeapon.rect.x + 10
            self.pWeapon.rect.y - 16
            pWeapon.add(self.pWeapon)
            self.fired = time.Time()

            for pWeapon in self.pWeapon:

                if self.player.pWeapon > 10:
                    self.pWeapon.weapon -= 1


pygame.init()
# Keeps the game running at a decent 60 FPS (Frames Per Second).
running = True
FPS = 60
level = 1
lives = 10
health = 100000

# Displays the font used on screen to tell the player how many lives they have left and what level they are currently on.
main_font = pygame.font.SysFont("Comicsans", 50)
lost_font = pygame.font.SysFont("Comicsans", 60)

# creates both the player (& enemy) ships velocity and the weapon velocity.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
playerShip_vel = 5
weapon_vel = 3
enemyShip_vel = 2

# set up Timer
enemyShip = pygame.USEREVENT + 1
pygame.time.set_timer(enemyShip, 3000)

#initializes player sprite
player = player()
clock = pygame.time.Clock()

# groups the sprites.
all_sprites = pygame.sprite.Group()
Enemy_group = pygame.sprite.Group()
Fire_group = pygame.sprite.Group()
all_sprites.add(player)
running = True

# Game sounds
pygame.mixer.init()

s = 'Sound'

# Sound effects for my game including ambient background music and enemy hit sounds.
background_Music = pygame.mixer.Sound("./Sounds/space-wind.mp3")
Thrusters = pygame.mixer.Sound("./Sounds/Rocket_Thrusters.mp3")
background_Music.set_volume(0.10)
Thrusters.set_volume(0.5)

# loops the bg music infinitely
background_Music.play(-1)

# main while loop.
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
        if event.type == KEYDOWN:

            if event.key == K_UP:
                player.setMoving = True
                thrust = engineThrust()
                all_sprites.add(thrust)
                Fire_group.add(thrust)
                Thrusters.play()

            if event.key == K_RIGHT or K_LEFT:
                player.setMoving = True
                thrust = engineThrust()
                all_sprites.add(thrust)
                Fire_group.add(thrust)
                Thrusters.play()

            # Continues playing the Rocket Thruster sound effect when the down key is pressed.
            if event.key == K_DOWN:
                player.setMoving = True

        if event.type == KEYUP:

            if event.key == K_UP:
                print("in key up")
                player.setMoving = False
                Thrusters.stop()
                thrust.dead = True

            # Stops playing the rocket thruster sound effect when moving right or left.
            if event.key == K_RIGHT or K_LEFT:
                player.setMoving = False
                Thrusters.stop()
                thrust.dead = True
                
            #   Continues playing the Rocket Thruster sound effect when the down key is pressed.
            if event.key == K_DOWN:
                player.setMoving = False
                Thrusters.stop()
                thrust.dead = True
        # if event.type == enemyShip:
        # newShip = Enemy()
        # all_sprites.add(newShip)
        # Enemy_group.add(newShip)

    keys = pygame.key.get_pressed()
    # screen.fill changes the background color to black.
    player.update(keys)
    Fire_group.update()
    screen.fill((0, 0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    # Keeps the FPS (Frames Per Second) capped at 60 Frames.
    clock.tick(60)
