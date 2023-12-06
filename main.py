import pygame
import sys
import random

pygame.font.init()
font = pygame.font.SysFont("Arial", 36)
size = width, height = 800, 600
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
        self.bombs = 3
        self.power = 0
        self.lives = 5
        self.movementcountery = 0
        self.movementcounteryshift = 0
        self.movementcounterx = 0
        self.movementcounterxshift = 0
        self.rect = pygame.Rect(self.x, self.y, 7, 7)
        # this is the starting position of the player

    def move(self, direction1, shift):
        # direction1 is the direction that is told to it from the code
        # shift checks if the shift key is held if it is the character moves about half speed
        # checks the current direction
        if direction1 == "up":
            # checks if at top of screen
            if self.rect.y <= 3:
                self.rect.y = 3
            # if it is at the top of the screen it will stay still
            else:
                if shift:
                    self.movementcounteryshift += 1
                    if self.movementcounteryshift > 14:
                        self.rect.y -= 1
                        self.movementcounteryshift = 0
                else:
                    self.movementcountery += 1
                    if self.movementcountery > 4:
                        self.rect.y -= 1
                        self.movementcountery = 0
        elif direction1 == "down":
            if self.rect.y >= 600 - 3:
                self.rect.y = 600 - 3
            else:
                if shift:
                    self.movementcounteryshift -= 1
                    if self.movementcounteryshift < -14:
                        self.rect.y += 1
                        self.movementcounteryshift = 0
                else:
                    self.movementcountery -= 1
                    if self.movementcountery < -4:
                        self.rect.y += 1
                        self.movementcountery = 0
        if direction1 == "left":
            if self.rect.x <= 3:
                self.rect.x = 3
            else:
                if shift:
                    self.movementcounterxshift += 1
                    if self.movementcounterxshift > 14:
                        self.rect.x -= 1
                        self.movementcounterxshift = 0
                else:
                    self.movementcounterx += 1
                    if self.movementcounterx > 4:
                        self.rect.x -= 1
                        self.movementcounterx = 0
        elif direction1 == "right":
            if self.rect.x >= 600 - 3:
                self.rect.x = 600 - 3
            else:
                if shift:
                    self.movementcounterxshift -= 1
                    if self.movementcounterxshift < -14:
                        self.rect.x += 1
                        self.movementcounterxshift = 0
                else:
                    self.movementcounterx -= 1
                    if self.movementcounterx < -4:
                        self.rect.x += 1
                        self.movementcounterx = 0

    # draw the character and defines its size
    def display(self):
        if self.power >= 125:
            self.power = 125
        pygame.draw.rect(screen, (225, 225, 225), self.rect)


class enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.health = random.randint(1,6)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def firestraight(self):
        projectileArrayEnemy.append(straight(self.rect.x, self.rect.y, "enemy", None))

    def firewiggly(self):
        projectileArrayEnemy.append(wiggly(self.rect.x, self.rect.y, "enemy", "left"))

    def lose_health(self):
        self.health -= 1

    def move(self):
        self.rect.x += random.randint(-1, 1)
        self.rect.y += random.randint(-1, 1)

    def display(self):
        pygame.draw.rect(screen, (0, 225, 0), self.rect)

class Power:
    def __init__(self, x, y, big):
        self.x = x
        self.y = y
        if big == True:
            self.big = True
        else:
            self.big = False
        if self.big:
            self.width = 26
            self.height = 26
        else:
            self.width = 14
            self.height = 14
        self.movementcounter = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision(self, player):
        return self.rect.colliderect(player.rect)

    def display(self):
        pygame.draw.rect(screen, (225, 0, 0), self.rect)
        self.movementcounter += 1
        if self.movementcounter > 6:
            self.movementcounter = 0
            self.rect.y += 1

class projectile:
    def __init__(self, x, y, ownedby, side):
        if ownedby == "player":
            self.ownedByPlayer = True
        else:
            self.ownedByPlayer = False
        self.side = side
        self.x = x
        self.y = y
        self.width = 6
        self.height = 6
        self.movementCounterx = 1
        self.movementCountery = 0
        self.secondMovement = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision(self, Enemy):
        return self.rect.colliderect(Enemy.rect)

    def display(self):
        if self.ownedByPlayer:
            pygame.draw.rect(screen, (255, 3, 234), self.rect)
        else:
            pygame.draw.rect(screen, (0, 252, 21), self.rect)
class straight(projectile):

    def move(self):
        self.movementCountery += 1
        if self.movementCountery >= 3:
            self.movementCountery = 0
            if self.ownedByPlayer == False:
                self.rect.y += 1
            else:
                self.rect.y -= 1

class wiggly(projectile):
    def move(self):
        self.movementCountery += 1
        if self.movementCountery >= 3:
            self.movementCountery = 0
            if self.ownedByPlayer == False:
                self.rect.y += 1
            else:
                self.rect.y -= 1
        if self.side == "left":
            if self.movementCounterx < 0:
                self.secondMovement += 1
                if self.secondMovement >= 6:
                    self.secondMovement = 0
                    self.movementCounterx-=1
                    self.rect.x +=1
            if self.movementCounterx > 0:
                self.secondMovement += 1
                if self.secondMovement >= 6:
                    self.secondMovement = 0
                    self.movementCounterx+=1
                    self.rect.x -=1
            if self.movementCounterx > 50:
                self.movementCounterx = -1
            if self.movementCounterx < -50:
                self.movementCounterx = 1
        if self.side == "right":
            if self.movementCounterx < 0:
                self.secondMovement += 1
                if self.secondMovement >= 6:
                    self.secondMovement = 0
                    self.movementCounterx-=1
                    self.rect.x -=1
            if self.movementCounterx > 0:
                self.secondMovement += 1
                if self.secondMovement >= 6:
                    self.secondMovement = 0
                    self.movementCounterx+=1
                    self.rect.x +=1
            if self.movementCounterx > 50:
                self.movementCounterx = -1
            if self.movementCounterx < -50:
                self.movementCounterx = 1

player1 = Player()
Clock = pygame.time.Clock()
screen.fill((0, 0, 0))
player1.display()
lastTimeFired = 0
firstTimeFired = 0
lastTimeSpawned = 0
thisTimeSpawned = 0
lastTimeBombed = 0
enemiesSpawn = False
lastTimeDied = 0
score = 0
Powerlist = []

while True:
    if pygame.time.get_ticks() > 3000:
        enemiesSpawn = True

    # closes the game if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT or player1.lives == 0:
            if player1.lives == 0:
                print("Game Over")
                score += pygame.time.get_ticks()/1000
                score = int(score)
                print("Your final score was: {}".format(score))
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

    if firstTimeFired - lastTimeFired >= 150:
        time = True

    # fires projectiles
    if fire and time:
        lastTimeFired = pygame.time.get_ticks()
        projectileArrayPlayer.append(straight(player1.rect.x+12, player1.rect.y, "player", None))
        projectileArrayPlayer.append(straight(player1.rect.x-12, player1.rect.y, "player", None))
        if player1.power >= 25:
            projectileArrayPlayer.append(straight(player1.rect.x, player1.rect.y - 4, "player", None))
        if player1.power >= 10:
            projectileArrayPlayer.append(wiggly(player1.rect.x, player1.rect.y - 4, "player", "left"))
            projectileArrayPlayer.append(wiggly(player1.rect.x, player1.rect.y - 4, "player", "right"))
        time = False

    thisTimeSpawned = pygame.time.get_ticks()

    CheckBomb = pygame.key.get_pressed()
    if CheckBomb[pygame.K_x]:
        if pygame.time.get_ticks() - lastTimeBombed >= 500:
            if player1.bombs > 0:
                player1.bombs -= 1
                enemyArray = []
                projectileArrayEnemy = []
                lastTimeBombed = pygame.time.get_ticks()



    # spawns enemies
    if enemiesSpawn and thisTimeSpawned - lastTimeSpawned >= 4000:
        lastTimeSpawned = pygame.time.get_ticks()
        numOfEn = random.randint(1, 8)
        for i in range(0, numOfEn):
            enemyArray.append(enemy(random.randint(0, 580), random.randint(0, 150)))

    # checks for collision
    for i in range(0, len(projectileArrayPlayer)):
        try:
            for j in range(0, len(enemyArray)):
                try:
                    if projectileArrayPlayer[i].check_collision(enemyArray[j]):
                        del projectileArrayPlayer[i]
                        enemyArray[j].lose_health()
                        if enemyArray[j].health == 0:
                            score += 10
                            if random.randint(1,3) == 2:
                                if random.randint(1,6) == 4:
                                    Powerlist.append(Power(enemyArray[j].rect.x, enemyArray[j].rect.y, True))
                                else:
                                    Powerlist.append(Power(enemyArray[j].rect.x, enemyArray[j].rect.y, False))
                            del enemyArray[j]
                except:
                    pass
        except:
            pass

    for j in range(0, len(enemyArray)):
        try:
            if enemyArray[j].rect.y < -10 or enemyArray[j].rect.x < -10 or enemyArray[j].rect.y > 610 or enemyArray[j].rect.x > 590:
                del enemyArray[j]
        except:
            pass
        try:
           if random.randint(1,300) == 1:
                enemyArray[j].firestraight()
           elif random.randint(1,375) == 1:
                enemyArray[j].firewiggly()
        except:
            pass
    for i in range(0, len(Powerlist)):
        try:
            if Powerlist[i].check_collision(player1):
                score += 5
                if Powerlist[i].big:
                    player1.power += 5
                else:
                    player1.power += 1
                del Powerlist[i]
        except IndexError:
            pass

    # redraws the screen
    pygame.draw.rect(screen, black, (0,0,600,600))
    pygame.draw.rect(screen, (0,0,200), (600,0,800,600))
    player1.display()
    textSurfaceL = font.render("Lives: {}".format(player1.lives), True, (252,82,64))
    textSurfaceP = font.render("Power: {}".format(player1.power), True, (252,82,64))
    textSurfaceS = font.render("Score: {}".format(score), True, (252, 82, 64))
    screen.blit(textSurfaceL, (620, 120))
    screen.blit(textSurfaceP, (620, 220))
    screen.blit(textSurfaceS, (620, 320))
    for i in range(0, len(projectileArrayPlayer)):
        try:
            if projectileArrayPlayer[i].rect.y < 0:
                del projectileArrayPlayer[i]
        except:
            pass
        try:
            if projectileArrayPlayer[i].rect.x > 600:
                del projectileArrayPlayer[i]
        except:
            pass
        try:
            projectileArrayPlayer[i].move()
            projectileArrayPlayer[i].display()
        except:
            pass

    for i in range(0, len(projectileArrayEnemy)):
        try:
            if projectileArrayEnemy[i].rect.y < 0:
                del projectileArrayEnemy[i]
        except:
            pass
        try:
            if projectileArrayEnemy[i].rect.x > 600:
                del projectileArrayEnemy[i]
        except:
            pass
        try:
            projectileArrayEnemy[i].move()
            projectileArrayEnemy[i].display()
        except:
            pass

    for i in range(0, len(Powerlist)):
        try:
            if Powerlist[i].rect.y > 800:
                del Powerlist[i]
        except:
            pass
        try:
            Powerlist[i].display()
        except IndexError:
            pass

    for i in range(0, len(projectileArrayEnemy)):
        try:
            if pygame.time.get_ticks() - lastTimeDied > 5000:
                if projectileArrayEnemy[i].check_collision(player1):
                    del projectileArrayEnemy[i]
                    player1.lives -=1
                    lastTimeDied = pygame.time.get_ticks()
        except:
            pass

    for i in range(0, len(enemyArray)):
        enemyArray[i].move()
        enemyArray[i].display()

    pygame.display.flip()
