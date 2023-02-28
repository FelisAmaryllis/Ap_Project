import pygame

clock = pygame.time.Clock()
ticks = pygame.time.get_ticks()

class Hydrogen_bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((x,y, 60, 30))
        self.image = pygame.Surface((60,30))

    def move(self, screen_width):
        SPEED = 10
        dx = 0
        dx -= SPEED
        for i in range(1,6):
            img = pygame.image.load("assets/images/HydrogenBombAni" + str(i)+".png").convert_alpha()
            #Here

            self.image = img


        self.rect.x += dx

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

class LandMine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((x,y, 30, 10))
        self.image = pygame.Surface((30,10))

    def move(self, screen_width):
        SPEED = 5
        dx = 0
        dx -= SPEED
        for i in range(1,2):
            img = pygame.image.load("assets/images/LandmineAni" + str(i)+".png").convert_alpha()
            self.image = img


        self.rect.x += dx

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

class Atk_Chopper(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((x,y, 80, 50))
        self.image = pygame.Surface((80,50))

    def move(self, screen_width):
        SPEED = 15
        dx = 0
        dx -= SPEED
        dy = 0
        dy += SPEED


        self.rect.x += dx
        self.rect.y += dy


    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)