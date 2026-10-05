import sys
import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Set up display window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wildlife Information Display")

# 3. Define Colors (RGB)
WHITE = (255, 255, 255)
DARK_GREEN = (20, 50, 20)
YELLOW = (255, 220, 0)

# 4. Load & Scale Images
# Replace 'background.jpg' and 'animal.png' with your image file paths
bg_image = pygame.image.load("background.jpg").convert()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

animal_image = pygame.image.load("animal.png").convert_alpha()
animal_image = pygame.transform.scale(animal_image, (300, 300))
animal_rect = animal_image.get_rect(center=(SCREEN_WIDTH // 2, 320))

# 5. Load Fonts for Text Rendering
title_font = pygame.font.SysFont("arial", 40, bold=True)
fact_font = pygame.font.SysFont("arial", 22)

# Render Text Surfaces
title_text = title_font.render("Wildlife Spotlight: The Snow Leopard", True, YELLOW)
title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 60))

fact_text = fact_font.render(
    "Fact: Snow leopards use their long tails for balance and to wrap around themselves for warmth.",
    True,
    WHITE
)
fact_rect = fact_text.get_rect(center=(SCREEN_WIDTH // 2, 520))

# 6. Set up Clock for Frame Rate Control
clock = pygame.time.Clock()
FPS = 60

# 7. Main Game Loop
running = True
while running:
    # Event Handling Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw / Render Visuals
    screen.blit(bg_image, (0, 0))               # Draw background image
    screen.blit(animal_image, animal_rect)       # Draw wildlife image
    screen.blit(title_text, title_rect)         # Render heading
    screen.blit(fact_text, fact_rect)           # Render wildlife fact

    # Update Display
    pygame.display.flip()

    # Cap Frame Rate
    clock.tick(FPS)

# Clean up and exit
pygame.quit()
sys.exit()