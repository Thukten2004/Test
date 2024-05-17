import pygame
import random
import sys
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Define game constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
font = pygame.font.Font(None, 36)

# Game variables
score = 0
game_over = False

# Countdown timer
countdown = 3
countdown_font = pygame.font.Font(None, 72)

# Game loop
clock = pygame.time.Clock()

def reset_game():
    global score, countdown, game_over
    score = 0
    countdown = 3
    game_over = False
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = 2

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    def check_collision(self):
        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.speed_x = -self.speed_x
        if self.y <= BALL_RADIUS:
            self.speed_y = -self.speed_y
class Paddle:
    def __init__(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - self.height - 10
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= 10
        elif direction == "right" and self.x < WIDTH - self.width:
            self.x += 10
class Game:
    def __init__(self):
        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
    def update(self):
        self.ball.move()
        self.ball.check_collision()
        if self.ball.y >= HEIGHT - BALL_RADIUS - PADDLE_HEIGHT:
            if self.paddle.x <= self.ball.x <= self.paddle.x + PADDLE_WIDTH:
                self.ball.y = HEIGHT - BALL_RADIUS - PADDLE_HEIGHT - 1
                self.ball.speed_y = -self.ball.speed_y
                self.score += 1
            else:
                self.game_over = True

    def draw(self, screen):
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, (self.ball.x, self.ball.y), BALL_RADIUS)
        pygame.draw.rect(screen, WHITE, (self.paddle.x,self.paddle.y, self.paddle.width, self.paddle.height))
        score_text = self.font.render(f"Score: {self.score}",True, WHITE)
        screen.blit(score_text, (10, 10))
        if self.game_over:
            game_over_text = self.font.render(f"Your score:        {self.score}", True, WHITE)
            game_over_rect = game_over_text.get_rect()
            game_over_rect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(game_over_text, game_over_rect)
def main():
    game_state = GameState()
    countdown = CountdownTimer(3)

    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if countdown.active:
            countdown.update()
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and game_state.paddle_y > 0:
                game_state.paddle_y -= game_state.paddle_speed
            if keys[pygame.K_DOWN] and game_state.paddle_y < screen_height - game_state.paddle_height:
                game_state.paddle_y += game_state.paddle_speed

            if not game_state.game_over:
                game_state.ball_x += game_state.ball_speed_x
                game_state.ball_y += game_state.ball_speed_y

                if game_state.ball_y <= 0 or game_state.ball_y >= screen_height - game_state.ball_size:
                    game_state.ball_speed_y *= -1

                if game_state.ball_x <= 0:
                    game_state.game_over = True
                elif game_state.ball_x >= screen_width - game_state.ball_size:
                    if game_state.paddle_y <= game_state.ball_y <= game_state.paddle_y + game_state.paddle_height:
                        game_state.score += 1
                        game_state.ball_speed_x *= -1
                    else:
                        game_state.game_over = True

            # Drawing paddle and ball
            pygame.draw.rect(screen, WHITE, pygame.Rect(game_state.paddle_x, game_state.paddle_y, game_state.paddle_width, game_state.paddle_height))
            pygame.draw.ellipse(screen, WHITE, pygame.Rect(game_state.ball_x, game_state.ball_y, game_state.ball_size, game_state.ball_size))

            # Draw score
            draw_text(f"Score: {game_state.score}", font, WHITE, 100, 50)

            if game_state.game_over:
                draw_text("Game Over", font, WHITE, screen_width // 2, screen_height // 2)
                draw_text(f"Your score: {game_state.score}", font, WHITE, screen_width // 2, screen_height // 2 + 50)
                draw_text("Press Space to play again", font, WHITE, screen_width // 2, screen_height // 2 + 100)
                pygame.display.flip()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    game_state.reset_game()
                    countdown.start()

        countdown.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
main()
