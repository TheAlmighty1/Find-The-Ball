from time import sleep

import os
import pygame
import sys
from pygame.locals import *

from movecups import movetheballs

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
FPS = 60

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
DisplaySurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Find The Ball')
FramePerSec = pygame.time.Clock()
pygame.mouse.set_visible(False)

MouseSprite = pygame.image.load('mouse.png').convert_alpha()
ClickImage = pygame.image.load('click.png').convert_alpha()
CupSprite = pygame.image.load('cup.png').convert_alpha()
ball = pygame.image.load('ball.png').convert_alpha()


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = MouseSprite
        self.rect = self.surf.get_rect(center=(43110, 413110))


class Cup1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = CupSprite
        self.rect = self.surf.get_rect(center=(WIDTH // 3, HEIGHT // 2))


class Cup2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = CupSprite
        self.rect = self.surf.get_rect(center=(WIDTH // 2, HEIGHT // 4))


class Cup3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = CupSprite
        self.rect = self.surf.get_rect(center=(2 * WIDTH // 3, HEIGHT // 2))


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = ball
        self.rect = self.surf.get_rect(center=((WIDTH // 2), (HEIGHT // 2)))


def move(self):
    self.pos = (pygame.mouse.get_pos())
    self.rect.midbottom = self.pos


def clicking(self):
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        self.surf = ClickImage
    if not mouse_pressed[0]:
        self.surf = MouseSprite


def reveal(self):
    mouse_pressed2 = pygame.mouse.get_pressed()
    hits = pygame.sprite.spritecollide(Player, Cups, False)
    if hits and mouse_pressed2[0]:
        pygame.sprite.spritecollide(Player, Cups, True)


def Start():
    target_y = HEIGHT // 2
    current_y = HEIGHT // 4
    speed = 0.5

    while current_y < target_y:
        current_y += speed
        if current_y > target_y:
            current_y = target_y

        CupSprite2.rect = CupSprite2.surf.get_rect(center=((WIDTH // 2), current_y))

        DisplaySurface.fill((0, 150, 160))

        for entity in all_sprites:
            DisplaySurface.blit(entity.surf, entity.rect)
        pygame.display.update()
    hits = pygame.sprite.spritecollide(BallSprite, Cups, False)
    if hits:
        all_sprites.remove(BallSprite)


Won, font = False, pygame.font.Font('freesansbold.ttf', 64)


def Win():
    global Won, text, TextRect
    hits = pygame.sprite.spritecollide(Player, Cups, False)
    hits2 = pygame.sprite.spritecollide(Player, BallGroup, False)
    font = pygame.font.Font('freesansbold.ttf', 128)
    mouse_pressed = pygame.mouse.get_pressed()
    if hits and hits2 and mouse_pressed[0]:
        pygame.sprite.spritecollide(Player, Cups, False)
        text = font.render('You Win!', True, (255, 255, 255), (0, 150, 160))
        TextRect = text.get_rect()
        TextRect.center = (WIDTH // 2), (HEIGHT // 4)
        Won = True
    elif hits and not hits2 and mouse_pressed[0]:
        pygame.sprite.spritecollide(Player, Cups, False)
        text = font.render('You Lose', True, (255, 255, 255), (0, 150, 160))
        TextRect = text.get_rect()
        TextRect.center = (WIDTH // 2), (HEIGHT // 4)
        Won = 'NO'
    return Won, text, TextRect


# sprites
Player = Mouse()
CupSprite1 = Cup1()
CupSprite2 = Cup2()
CupSprite3 = Cup3()
BallSprite = Ball()

all_sprites = pygame.sprite.Group()
Cups = pygame.sprite.Group()
PlayerSprite = pygame.sprite.Group()
BallGroup = pygame.sprite.Group()

all_sprites.add(BallSprite, CupSprite1, CupSprite2, CupSprite3, Player)
Cups.add(CupSprite1, CupSprite2, CupSprite3)
PlayerSprite.add(Player)
BallGroup.add(BallSprite)

# main
started = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE and not started:
                Start()
                all_sprites.remove(BallSprite)
                sleep(0.5)
                for n in range(0, 4):
                    movetheballs(CupSprite1, CupSprite2, CupSprite3, HEIGHT, WIDTH, DisplaySurface, all_sprites, Player,
                                 BallSprite)
                    all_sprites.remove(BallSprite)
                    n = n + 1
                    sleep(0.1)

                movetheballs(CupSprite1, CupSprite2, CupSprite3, HEIGHT, WIDTH, DisplaySurface, all_sprites, Player,
                             BallSprite)
                all_sprites.add(BallSprite)
                sleep(0.1)
                started = True
    DisplaySurface.fill((0, 150, 160))
    if not started:
        text = font.render('Space to Start, Escape to Close', True, (255, 255, 255), (0, 150, 160))
        TextRect = text.get_rect()
        TextRect.center = (WIDTH // 2), (HEIGHT // 7)
        DisplaySurface.blit(text, TextRect)
    if started:
        move(Player)
        if not Won:
            clicking(Player)
            Win()
            reveal(Player)
        if Won:
            DisplaySurface.blit(text, TextRect)
        elif Won == 'NO':
            DisplaySurface.blit(text, TextRect)

    for entity in all_sprites:
        DisplaySurface.blit(entity.surf, entity.rect)

    pygame.display.update()
