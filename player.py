import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk1 = pygame.image.load(
            "graphics/player/player_walk_1.png"
        ).convert_alpha()
        player_walk2 = pygame.image.load(
            "graphics/player/player_walk_2.png"
        ).convert_alpha()

        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))

        self.gravity = 0
        self.player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()
        self.jump_sund = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sund.set_volume(0.5)

    def _player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if self.rect.bottom >= 300:
                self.jump_sund.play()
                self.gravity = -20

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.rect.left >= 5:
                self.rect.x -= 5

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.rect.right <= 800:
                self.rect.x += 5

    def _apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def _animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            self.image = self.player_walk[int(self.player_index) % 2]

    def update(self) -> None:
        self._animation_state()
        self._player_input()
        self._apply_gravity()
