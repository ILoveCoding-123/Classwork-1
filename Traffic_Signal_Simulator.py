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
ROAD_GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smart Traffic Signal Simulator")
clock = pygame.time.Clock()

# Custom Event for boundary/traffic signal change
TRAFFIC_CHANGE_EVENT = pygame.USEREVENT + 1

# Car Sprite Class
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 60
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.color = BLUE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 4

    def update(self):
        # Move the car horizontally
        self.rect.x += self.velocity

        # Check if the car hits the screen boundaries
        if self.rect.right >= SCREEN_WIDTH - 50:
            self.rect.right = SCREEN_WIDTH - 50
            self.velocity = -self.velocity  # Reverse direction
            pygame.event.post(pygame.event.Event(TRAFFIC_CHANGE_EVENT))
        elif self.rect.left <= 50:
            self.rect.left = 50
            self.velocity = -self.velocity  # Reverse direction
            pygame.event.post(pygame.event.Event(TRAFFIC_CHANGE_EVENT))

    def change_color(self):
        # Randomize car color upon boundary hit
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.image.fill(self.color)

# Traffic Signal Class
class TrafficSignal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "GREEN"
        self.color = GREEN

    def change_state(self):
        # Cycle through signal states
        if self.state == "GREEN":
            self.state = "YELLOW"
            self.color = YELLOW
        elif self.state == "YELLOW":
            self.state = "RED"
            self.color = RED
        else:
            self.state = "GREEN"
            self.color = GREEN

    def draw(self, surface):
        # Draw traffic light housing
        pygame.draw.rect(surface, (30, 30, 30), (self.x - 15, self.y - 45, 30, 90))
        # Draw current active light
        pygame.draw.circle(surface, self.color, (self.x, self.y), 12)

# Sprite Group setup
all_sprites = pygame.sprite.Group()
car = Car(100, SCREEN_HEIGHT // 2 - 15)
all_sprites.add(car)

# Traffic Signal setup
signal = TrafficSignal(SCREEN_WIDTH // 2, 150)

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TRAFFIC_CHANGE_EVENT:
            car.change_color()
            signal.change_state()

    # Update sprites
    all_sprites.update()

    # Drawing / Rendering
    screen.fill(ROAD_GRAY)

    # Draw Road Markings
    pygame.draw.line(screen, WHITE, (50, SCREEN_HEIGHT // 2), (SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2), 4)

    # Draw all sprite groups
    all_sprites.draw(screen)

    # Draw Traffic Signal
    signal.draw(screen)

    # Display updates
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()