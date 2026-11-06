import random
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player and Enemy Sprites Collision")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Fonts for displaying score
font = pygame.font.SysFont(None, 36)

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self):
        # Keyboard controls for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Keep player within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # Position randomly on the screen[cite: 1]
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 30)

# Sprite groups
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create 7 other enemy sprites[cite: 1]
for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_group.add(enemy)

# Score variable[cite: 1]
score = 0

# Game loop variables
clock = pygame.time.Clock()
running = True

# Main Game Loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions between player and enemies[cite: 1]
    # pygame.sprite.spritecollide can automatically remove collided enemies or just trigger logic.
    # Here, we respawn the enemy at a random location and increase the score by 1 upon collision.
    collisions = pygame.sprite.spritecollide(player, enemy_group, False)
    if collisions:
        for enemy in collisions:
            score += 1[cite: 1]
            # Reposition the collided enemy randomly so it doesn't repeatedly trigger instantly
            enemy.rect.x = random.randint(0, SCREEN_WIDTH - 30)
            enemy.rect.y = random.randint(0, SCREEN_HEIGHT - 30)

    # Drawing
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Render and display score text
    score_surf = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_surf, (10, 10))

    # Refresh screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()