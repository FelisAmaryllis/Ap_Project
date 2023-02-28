import pygame

clock = pygame.time.Clock()
oldticks = 0
animate_player = []

for i in range(1,4):
    load_img = pygame.image.load("assets/images/CharacterAni" + str(i)+ ".png")
    animate_player.append(load_img)




class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((x,y, 40, 70))
        self.image = pygame.image.load("assets/images/CharacterAni3.png").convert_alpha()
        print("Reste")
        self.vel_y = 0 # Got From (insert source) #Cause player to fall
        self.jump = False
        

    def move(self, screen_height,surface):# Move function got from (insert source)s
        GRAVITY = 2
        SPEED = 10
        dy = 0
        jump_timer = 4000
        time = 0
        while True:
            global oldticks
            ticks = pygame.time.get_ticks()
            if (ticks - oldticks) >= 3000:
                print("what")
                surface.blit(animate_player[2], (self.rect.x , self.rect.y))
            elif (ticks- oldticks) == 2000:
                surface.blit(animate_player[1], (self.rect.x , self.rect.y))
            elif (ticks - oldticks) == 1000:
                surface.blit(animate_player[0], (self.rect.x , self.rect.y))
            break


                



        # Check to see what key was pressed
        key = pygame.key.get_pressed()

        # Jumps if W was pressed
        if key[pygame.K_w] and self.jump == False:
            self.jump = True
            self.vel_y = -30
            #Wirte A timer somewhere to mess with, so it delays fall while jumping up

        # Apply gravity and make the player fall after jumping
        self.vel_y += GRAVITY
        dy += self.vel_y  
        

        # Makes invisible border the player lands on
        if self.rect.bottom + dy >= screen_height - 100:
            self.vel_y = 0
            self.jump = False
            dy = screen_height -75 - self.rect.bottom
            
        
        self.rect.y += dy

        
        

        

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
        
