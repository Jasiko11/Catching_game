import pygame
import random

pygame.init()
highscore = 0
size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((size[0][0], size[0][1]))
pygame.display.toggle_fullscreen()

text_score_pos = pygame.Rect(0, 0, 0, 0)

def run_game():
    global text_score_pos
    pygame.display.set_caption("Catching Game")
    clock = pygame.time.Clock()
    dt = 0
    apple_speed = 5
    score = 0
    global highscore

    font = pygame.font.SysFont('arialunicode', 32)
    text_score = font.render(f"Score: {score} Highscore: {highscore}", True, "black")
    text_score_pos.center = (int(screen.get_width() / 2), 100)

    player_pos = pygame.Vector2(screen.get_width() / 2, (screen.get_height() / 2) + 400)
    apple_pos = pygame.Vector2(random.randint(1, 1920), 200)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("#32c5d9")
        pygame.draw.rect(screen, "blue", pygame.Rect(player_pos.x, player_pos.y, 40, 40))
        pygame.draw.circle(screen, "red", apple_pos, 20)
        screen.blit(text_score, text_score_pos)
        apple_pos.y += apple_speed

        if apple_pos.y > 1000:
            play_again()
            running = False

        if player_pos.x - 30 < apple_pos.x < player_pos.x + 30 and player_pos.y - 30 < apple_pos.y < player_pos.y + 30:
            apple_speed = random.randint(3, 10)
            apple_pos.x = random.randint(1, 1920)
            apple_pos.y = 200
            score += 1

            if score > highscore:
                highscore = score
                text_score = font.render(f"Score: {score} Highscore: {highscore}", True, "black")

        keys = pygame.key.get_pressed()
        player_pos.x += (keys[pygame.K_d] - keys[pygame.K_a]) * 500 * dt
        player_pos.x = max(0, min(player_pos.x, screen.get_width() - 40))

        if score > highscore:
            text_score = font.render(f"Score: {score} Highscore: {highscore}", True, "black")

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()


def play_again():
    running = True
    font = pygame.font.SysFont('arialunicode', 32)
    text_play_again = font.render("Do you want to play again?: ", True, "black")
    text_play_again_pos = text_play_again.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

    text_play_again_yes = font.render("yes", True, "black")
    text_play_again_yes_pos = text_play_again_yes.get_rect(center=(screen.get_width() / 2 - 50, screen.get_height() / 2 + 100))

    text_play_again_no = font.render("no", True, "black")
    text_play_again_no_pos = text_play_again_no.get_rect(center=(screen.get_width() / 2 + 50, screen.get_height() / 2 + 100))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if text_play_again_yes_pos.collidepoint(pos):
                    run_game()  # Exit the loop to restart the game
                elif text_play_again_no_pos.collidepoint(pos):
                    running = False

        screen.fill("#32c5d9")
        screen.blit(text_play_again, text_play_again_pos)
        screen.blit(text_play_again_yes, text_play_again_yes_pos)
        screen.blit(text_play_again_no, text_play_again_no_pos)
        pygame.display.flip()

run_game()
