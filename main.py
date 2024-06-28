from sys import exit
import pygame
from game import PixelRunner


pygame.init()
clock = pygame.time.Clock()

BLUE = (111, 196, 169)
main_font = pygame.font.Font("font/Pixeltype.ttf", 100)
menu_font = pygame.font.Font("font/Pixeltype.ttf", 50)
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel Runner")

player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.scale(player_stand, (68 * 2.5, 84 * 2.5))
player_stand_rect = player_stand.get_rect(center=(400, 200))

bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.set_volume(0.3)
bg_music.play(loops=-1)

game_name = main_font.render("Pixel Runner", False, BLUE)
game_name_rect = game_name.get_rect(center=(400, 50))

game = PixelRunner(screen, menu_font)
flag_start = True
game_pouse = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            score, game_pouse = game.play()
            flag_start = False

        elif game_pouse:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if exit_massage_rect.collidepoint(x, y):
                    pygame.quit()
                    exit()

                if resume_massage_rect.collidepoint(x, y):
                    score, game_pouse = game.play()

                if restart_massage_rect.collidepoint(x, y):
                    game.game_restart()
                    score, game_pouse = game.play()

    if game_pouse:
        screen.fill((94, 129, 162))
        screen.blit(game_name, game_name_rect)

        resume_massage = menu_font.render(f"RESUME", False, BLUE)
        resume_massage_rect = resume_massage.get_rect(center=(400, 150))
        screen.blit(resume_massage, resume_massage_rect)

        restart_massage = menu_font.render(f"RESTART", False, BLUE)
        restart_massage_rect = restart_massage.get_rect(center=(400, 225))
        screen.blit(restart_massage, restart_massage_rect)

        exit_massage = menu_font.render(f"QUIT", False, BLUE)
        exit_massage_rect = exit_massage.get_rect(center=(400, 300))
        screen.blit(exit_massage, exit_massage_rect)

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)

        if not flag_start:
            score_massage = menu_font.render(f"Your score: {score}", False, BLUE)
            score_massage_rect = score_massage.get_rect(center=(400, 360))
            screen.blit(score_massage, score_massage_rect)
        else:
            game_massage = menu_font.render("Press spasce to run", False, BLUE)
            game_massage_rect = game_massage.get_rect(center=(400, 360))
            screen.blit(game_massage, game_massage_rect)

    pygame.display.update()
    clock.tick(60)
