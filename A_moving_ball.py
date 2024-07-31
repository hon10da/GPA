import pygame
import sys

# تعريف الألوان
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# تعريف الحجم
WIDTH = 800
HEIGHT = 600

# تعريف حجم الكرة وسرعتها
BALL_RADIUS = 10
BALL_SPEED = 5

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0 or self.x >= WIDTH:
            self.dx *= -1
        if self.y <= 0 or self.y >= HEIGHT:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), BALL_RADIUS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Break the Stones")

    ball = Ball()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ball.move()

        screen.fill(BLACK)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
