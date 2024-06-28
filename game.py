import pygame
from random import choice

from player import Player
from obstacle import Obstacle


class PixelRunner:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.sky_surf = pygame.image.load("graphics/Sky.png").convert()
        self.ground_surf = pygame.image.load("graphics/ground.png").convert()
        self.game_restart()
        self.clock = pygame.time.Clock()
        self.death = False

    def _update_score(self):
        if self.obstacle_group:
            for obstacle in self.obstacle_group:
                if obstacle.previous_x > 0 and obstacle.rect.x <= 0:
                    self.score += 1

    def _display_score(self):
        score_surf = self.font.render(f"Score: {self.score}", False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(400, 50))
        self.screen.blit(score_surf, score_rect)

    def game_restart(self):
        self.score = 0
        self.old_score = 0

        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.obstacle_group = pygame.sprite.Group()

        self.spawn_speed = 2000
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, self.spawn_speed)

    def play(self):
        if self.death:
            self.game_restart()
            self.death = False

        game_active = True

        while game_active and (not self.death):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == self.obstacle_timer:
                    self.obstacle_group.add(Obstacle(choice(["fly", "snail", "snail"])))

                    if self.old_score != self.score:
                        self.spawn_speed -= self.spawn_speed // 50
                        pygame.time.set_timer(self.obstacle_timer, self.spawn_speed)
                        self.old_score = self.score

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game_active = False

            self.screen.blit(self.sky_surf, (0, 0))
            self.screen.blit(self.ground_surf, (0, 300))

            self._update_score()
            self._display_score()

            self.player.draw(self.screen)
            self.player.update()

            self.obstacle_group.draw(self.screen)
            self.obstacle_group.update()

            collides = pygame.sprite.spritecollide(
                self.player.sprite, self.obstacle_group, False
            )
            self.death = len(collides) != 0

            pygame.display.update()
            self.clock.tick(60)

        return self.score, not game_active
