import pygame,sys,random
# Set up
pygame.init()
display = pygame.display.set_mode((1200, 1000))
clock = pygame.time.Clock()

# Player
class Player:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        # Image load
        self.up = pygame.image.load('images/up.png').convert()
        self.down = pygame.transform.rotate(self.up, 180).convert()
        self.left = pygame.image.load('images/left.png').convert()
        self.right = pygame.image.load('images/right.png').convert()
    def main(self, display):
        pygame.draw.rect(display, (250, 0, 0), (self.x, self.y, self.width, self.height))
        display.blit(self.up, (self.x, self.y))
        # Player movement
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x-=3
            display.blit(self.left, (self.x, self.y))
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x+=3
            display.blit(self.right, (self.x, self.y))
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y-=3
            display.blit(self.up, (self.x, self.y))
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y+=3
            display.blit(self.down, (self.x, self.y))

player = Player(400, 300, 30, 30)

# Objective
class Mars:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load('images/mars.png').convert()

    def main(self, display):
        display.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))
        pygame.draw.ellipse(display, (250, 0, 0), (self.x, self.y, self.width, self.height))

mars = Mars(random.randint(0, 1000), random.randint(0, 900), 32, 32)

#text setup
font = pygame.font.Font(None, 36)
score=1000000
# Display
while True:
    clock.tick(60)
    pygame.display.update()
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Collision detection
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
    mars_rect = pygame.Rect(mars.x, mars.y, mars.width, mars.height)
    if player_rect.colliderect(mars_rect):
        mars.x=random.randint(100,1000)
        mars.y=random.randint(100,800)
        score+=1
    #text addition to screen
    text = font.render("score:"+str(score), True, (255, 255, 255))
    display.blit(text, (20, 10))
    #addition of classes
    player.main(display)
    mars.main(display)