import pygame
import sys
import random

size = width, height = 600, 600
black = 0, 0, 0
white = 255, 255, 255
speed = 1
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A Level Project")
projectileArrayPlayer = []
projectileArrayEnemy = []
enemyArray = []


class Player:
    def __init__(self):
        self.x = 300
        self.y = 500
        # this is the starting position of the player

    def move(self, direction1, shift):
        # direction1 is the direction that is told to it from the code
        # shift checks if the shift key is held if it is the character moves about half speed
        # checks the current direction
        if direction1 == "up":
            # checks if at top of screen
            if self.y <= 3:
                self.y = 3
            # if it is at the top of the screen it will stay still
            else:
                if shift:
                    self.y -= 0.08
                else:
                    self.y -= 0.3
        elif direction1 == "down":
            if self.y >= 600 - 3:
                self.y = 600 - 3
            else:
                if shift:
                    self.y += 0.08
                else:
                    self.y += 0.3
        if direction1 == "left":
            if self.x <= 3:
                self.x = 3
            else:
                if shift:
                    self.x -= 0.08
                else:
                    self.x -= 0.4
        elif direction1 == "right":
            if self.x >= 600 - 3:
                self.x = 600 - 3
            else:
                if shift:
                    self.x += 0.08
                else:
                    self.x += 0.4

    # draw the character and defines its size
    def display(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 3)


class enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.health = 8
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def fire(self):
        projectileArrayEnemy.append(projectile(self.rect.x, self.rect.y))

    def lose_health(self):
        self.health -= 1

    def display(self):
        pygame.draw.rect(screen, (0, 225, 0), self.rect)


class projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.movementcounter = 0
        self.width = 6
        self.height = 6
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision(self, Enemy):
        return self.rect.colliderect(Enemy.rect)


    def display(self):
        pygame.draw.rect(screen, (255, 3, 234), self.rect)
        self.movementcounter += 1
        if self.movementcounter == 1:
            self.movementcounter = 0
            self.rect.y -= 1


player1 = Player()
Clock = pygame.time.Clock()
screen.fill((0, 0, 0))
player1.display()
lastTimeFired = 0
firstTimeFired = 0
lastTimeSpawned = 0
thisTimeSpawned = 0
enemiesSpawn = False

while True:
    if pygame.time.get_ticks() > 5000:
        enemiesSpawn = True

    # closes the game if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # checks if the shift is pressed and gives true or false from it
    shiftPressed = pygame.key.get_pressed()
    if shiftPressed[pygame.K_LSHIFT]:
        shift = True
    else:
        shift = False

    # gets the current directional key that is being pressed
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_DOWN]:
        player1.move("down", shift)
    if keystate[pygame.K_UP]:
        player1.move("up", shift)
    if keystate[pygame.K_LEFT]:
        player1.move("left", shift)
    if keystate[pygame.K_RIGHT]:
        player1.move("right", shift)

    # checks if z is pressed if it is it will fire from the player
    fire = False
    time = False
    checkFire = pygame.key.get_pressed()
    if checkFire[pygame.K_z]:
        firstTimeFired = pygame.time.get_ticks()
        fire = True

    if firstTimeFired - lastTimeFired >= 100:
        time = True

    #fires projectiles
    if fire and time:
        lastTimeFired = pygame.time.get_ticks()
        projectileArrayPlayer.append(projectile(player1.x, player1.y))
        time = False

    thisTimeSpawned = pygame.time.get_ticks()

    #spawns enemies
    if enemiesSpawn and thisTimeSpawned - lastTimeSpawned >= 5000:
        lastTimeSpawned = pygame.time.get_ticks()
        numOfEn = random.randint(1, 4)
        for i in range(0, numOfEn):
            enemyArray.append(enemy(random.randint(0,580), random.randint(0,150)))

    #checks for collision
    for i in range(0, len(projectileArrayPlayer)):
        try:
            for j in range(0, len(enemyArray)):
                try:
                    if projectileArrayPlayer[i].check_collision(enemyArray[j]):
                        del projectileArrayPlayer[i]
                        enemyArray[j].lose_health()
                        if enemyArray[j].health == 0:
                            del enemyArray[j]
                except:
                    pass
        except:
            pass



    # redraws the screen
    screen.fill((0, 0, 0))
    player1.display()
    for i in range(0, len(projectileArrayPlayer)):
        try:
            if projectileArrayPlayer[i].rect.y < 0:
                del projectileArrayPlayer[i]
        except:
            pass
        try:
            projectileArrayPlayer[i].display()
        except:
            pass

    for i in range(0, len(enemyArray)):
        try:
            enemyArray[i].display()
        except:
            pass

    pygame.display.flip()
