import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pet Food Collection Game")
clock = pygame.time.Clock()

# Pet Sprite Class
class Pet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 128, 0))  # Orange pet representation
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep pet within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Food Sprite Class
class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 30
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 255, 0))  # Green food representation
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Sprite Groups
all_sprites = pygame.sprite.Group()
food_group = pygame.sprite.Group()

# Create Pet
pet = Pet(100, 100)
all_sprites.add(pet)

# Create multiple food items
for _ in range(5):
    food_x = random.randint(100, SCREEN_WIDTH - 100)
    food_y = random.randint(100, SCREEN_HEIGHT - 100)
    food = Food(food_x, food_y)
    all_sprites.add(food)
    food_group.add(food)

# Create a background surface (simulating a full-screen background image)
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill((230, 240, 250))  # Light background color

# Setup font for completion message using a named system font
font_name = pygame.font.match_font('arial')
font = pygame.font.Font(font_name, 48)

# Main Game Loop
running = True
game_completed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_completed:
        # Update sprites
        all_sprites.update()

        # Check for collisions between pet and food items (remove collected food)
        collected_food = pygame.sprite.spritecollide(pet, food_group, True)

        # Check if all food has been collected
        if len(food_group) == 0:
            game_completed = True

    # Drawing / Rendering
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # Show completion message if all food is collected
    if game_completed:
        message = font.render("All Food Collected! Great Job!", True, (0, 128, 0))
        message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(message, message_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()