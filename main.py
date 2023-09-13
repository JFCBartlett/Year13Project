import pygame
import sys

size = width, height = 600, 600
black = 0, 0, 0
white = 255, 255, 255
speed = 1
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Touhou")
projectileArray = []


class Player:
    def __init__(self):
        self.x = 300
        self.y = 500
        # this is the size of the player

    def move(self, direction1, shift):
        # direction1 is the direction that is told to it from the code
        # shift checks if the shift key is held if it is the character moves about half speed
        # checks the current direction
        if direction1 == "up":
            # checks if at top of screen
            if self.y == 3:
                self.y = 3
            # if it is at the top of the screen it will stay still
            else:
                if shift == True:
                    self.y -= 0.08
                else:
                    self.y -= 0.15
        elif direction1 == "down":
            if self.y == 600 - 3:
                self.y = 600 - 3
            else:
                if shift == True:
                    self.y += 0.08
                else:
                    self.y += 0.15
        if direction1 == "left":
            if self.x == 3:
                self.x = 3
            else:
                if shift == True:
                    self.x -= 0.08
                else:
                    self.x -= 0.15
        elif direction1 == "right":
            if self.x == 600 - 3:
                self.x = 600 - 3
            else:
                if shift == True:
                    self.x += 0.08
                else:
                    self.x += 0.15

    # draw the character
    def display(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 3)


class projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10

    def display(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y))
        self.y -= 2


player1 = Player()

screen.fill((0, 0, 0))
player1.display()

while True:
    # closes the game if the pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # checks if the shift is pressed and gives true or false from it
    shiftpressed = pygame.key.get_pressed()
    if shiftpressed[pygame.K_LSHIFT]:
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


    checkfire = pygame.key.get_pressed()
    if checkfire[pygame.K_z]:
        fire = True

    if fire == True:
        projectileArray.append(projectile())
    screen.fill((0, 0, 0))
    player1.display()
    pygame.display.flip()
