import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Duel Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Initialize game variables
player1_score = 0
player2_score = 0
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                player1_score += 1
            elif event.key == pygame.K_p:
                player2_score += 1

    # Clear the screen
    screen.fill(black)

    # Display scores
    player1_text = font.render(f"Player 1: {player1_score}", True, white)
    player2_text = font.render(f"Player 2: {player2_score}", True, white)
    screen.blit(player1_text, (50, 50))
    screen.blit(player2_text, (width - player2_text.get_width() - 50, 50))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
