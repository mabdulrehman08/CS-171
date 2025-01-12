import pygame
import random
# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.25
FLAP_STRENGTH = -8
PIPE_WIDTH = 50
PIPE_GAP = 150
PIPE_VELOCITY = 3
BIRD_WIDTH = 40
BIRD_HEIGHT = 40

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load bird image
bird_image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_image.fill(BLUE)

# Font for displaying score
font = pygame.font.SysFont("Arial", 24)

class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))

class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - (self.height + PIPE_GAP))

    def move(self):
        self.x -= PIPE_VELOCITY
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

    def off_screen(self):
        return self.x < -PIPE_WIDTH

    def collide(self, bird):
        if bird.x + BIRD_WIDTH > self.top_rect.x and bird.x < self.top_rect.x + PIPE_WIDTH:
            if bird.y < self.top_rect.height or bird.y + BIRD_HEIGHT > self.bottom_rect.y:
                return True
        return False

def main():
    bird = Bird()
    pipes = [Pipe()]
    clock = pygame.time.Clock()
    running = True
    score = 0

    while running:
        screen.fill(WHITE)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        # Move bird and pipes
        bird.move()
        for pipe in pipes:
            pipe.move()

        # Check for collisions
        for pipe in pipes:
            if pipe.collide(bird):
                running = False

        # Remove off-screen pipes
        pipes = [pipe for pipe in pipes if not pipe.off_screen()]

        # Add new pipe
        if pipes[-1].x < SCREEN_WIDTH - 200:
            pipes.append(Pipe())
            score += 1

        # Draw everything
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
