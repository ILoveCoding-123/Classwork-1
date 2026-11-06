import random
import pygame

# Initialize Pygame and the mixer for sound
pygame.init()
pygame.mixer.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader Project - Part 2")

# Load Background Image & Music (Make sure these files exist in your project directory!)
try:
    background_img = pygame.image.load("background.png").convert()
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
except Exception:
    # Fallback to a solid color if image file is missing
    background_img = None

try:
    pygame.mixer.music.load("background_music.mp3")
    # Play music indefinitely (-1 means loop forever)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
except Exception:
    print("Background music file not found. Running without sound.")

# Colors
BLUE = (0, 120, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 30)

# Sprite groups
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Create player and enemies
player = Player()
all_sprites.add(player)

for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_group.add(enemy)

# Score variable
score = 0

# Game loop variables
clock = pygame.time.Clock()
running = True

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Check for collisions
    collisions = pygame.sprite.spritecollide(player, enemy_group, False)
    if collisions:
        for enemy in collisions:
            score += 1
            # Reposition enemy randomly on collision
            enemy.rect.x = random.randint(0, SCREEN_WIDTH - 30)
            enemy.rect.y = random.randint(0, SCREEN_HEIGHT - 30)

    # Drawing Background
    if background_img:
        screen.blit(background_img, (0, 0))
    else:
        screen.fill(BLACK)

    # Draw all sprites
    all_sprites.draw(screen)

    # Render and display score text (using white for visibility on dark background/images)
    score_surf = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surf, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()