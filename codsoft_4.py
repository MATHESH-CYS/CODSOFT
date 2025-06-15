import pygame
import random
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

FONT = pygame.font.SysFont("Serif", 30, italic=True)
SMALL_FONT = pygame.font.SysFont("Serif", 30, italic=True)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

CHOICES = ['Rock', 'Paper', 'Scissors']
RESULT_MATRIX = {
    ('rock', 'scissors'): 'win',
    ('scissors', 'paper'): 'win',
    ('paper', 'rock'): 'win'
}

# Button class
class Button:
    def __init__(self, x, y, w, h, text, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self.rect)
        text = FONT.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        SCREEN.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def draw_text(text, size, x, y, color=BLACK):
    font = pygame.font.SysFont("Serif", size, italic=True)
    rendered = font.render(text, True, color)
    SCREEN.blit(rendered, (x, y))

# Determine winner
def determine_winner(user, comp):
    if user == comp:
        return 'tie'
    return 'win' if (user, comp) in RESULT_MATRIX else 'lose'

# Final result screen
def final_result_screen(user_score, comp_score):
    SCREEN.fill(WHITE)
    draw_text("Final Score", 40, 200, 80)
    draw_text(f"You: {user_score}", 30, 200, 140, GREEN)
    draw_text(f"Computer: {comp_score}", 30, 200, 180, RED)

    if user_score > comp_score:
        draw_text("You won the match! 🎉", 30, 200, 230, GREEN)
    elif user_score < comp_score:
        draw_text("Computer won the match! 💻", 30, 200, 230, RED)
    else:
        draw_text("The match is a tie! 🤝", 30, 200, 230, GRAY)

    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# Main game loop
def game_loop():
    user_score = 0
    comp_score = 0
    user_choice = comp_choice = result = None

    buttons = [
        Button(80, 280, 120, 50, 'Rock', RED),
        Button(240, 280, 120, 50, 'Paper', GRAY),
        Button(400, 280, 120, 50, 'Scissor', GREEN)
    ]
    play_again_btn = Button(230, 340, 140, 40, 'Play Again', BLUE)
    exit_btn = Button(400, 340, 100, 40, 'Exit', RED)

    running = True
    while running:
        SCREEN.fill(WHITE)

        draw_text("Choose Rock, Paper, or Scissors", 30, 120, 30)
        for btn in buttons:
            btn.draw()

        if user_choice:
            draw_text(f"You chose: {user_choice}", 28, 80, 100)
            draw_text(f"Computer chose: {comp_choice}", 28, 80, 140)

            if result == 'win':
                draw_text("You Win! 🎉", 32, 80, 180, GREEN)
            elif result == 'lose':
                draw_text("Computer Wins! 💻", 32, 80, 180, RED)
            else:
                draw_text("It's a Tie! 🤝", 32, 80, 180, GRAY)

            draw_text(f"Score: You {user_score} - {comp_score} Computer", 28, 80, 220)
            play_again_btn.draw()
            exit_btn.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                final_result_screen(user_score, comp_score)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if not user_choice:
                    for btn in buttons:
                        if btn.is_clicked(pos):
                            user_choice = btn.text.lower()
                            comp_choice = random.choice(CHOICES).lower()
                            result = determine_winner(user_choice, comp_choice)

                            if result == 'win':
                                user_score += 1
                            elif result == 'lose':
                                comp_score += 1
                elif play_again_btn.is_clicked(pos):
                    user_choice = comp_choice = result = None
                elif exit_btn.is_clicked(pos):
                    final_result_screen(user_score, comp_score)

        pygame.display.flip()

# Run the game
game_loop()

       
