import pygame
from random import randint


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type: str):
        super().__init__()

        self.type = type
        if type == "fly":
            fly_1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 200
            self.speed = 10
            self.animation_speed = 0.1

        else:
            snail_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
            self.speed = 6
            self.animation_speed = 0.2

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))
        self.previous_x = self.rect.x

    def _animation_state(self):
        self.animation_index += self.animation_speed
        self.image = self.frames[int(self.animation_index) % 2]

    def update(self) -> None:
        self.previous_x = self.rect.x
        self._animation_state()
        self.rect.x -= self.speed
        self._destroy()

    def _destroy(self):
        if self.rect.x <= -100:
            self.kill()
