import pygame
import random


def movetheballs(CupSprite1, CupSprite2, CupSprite3, HEIGHT, WIDTH, DisplaySurface, all_sprites, Player, BallSprite):
    choices3 = [CupSprite1.rect.centerx, CupSprite3.rect.centerx]
    Movement3 = random.choice(choices3)
    speed = 0.6

    current_x1 = CupSprite1.rect.centerx
    target_x1 = CupSprite2.rect.centerx

    current_x2 = CupSprite2.rect.centerx
    target_x2 = Movement3

    current_x3 = CupSprite3.rect.centerx
    target_x3 = CupSprite2.rect.centerx

    if Movement3 == CupSprite1.rect.centerx and current_x2 > target_x2:
        while current_x2 > target_x2 and current_x1 < target_x1:
            current_x2 -= speed
            current_x1 += speed
            if current_x2 < target_x2:
                current_x2 = target_x2
            if current_x1 > target_x1:
                current_x1 = target_x1

            CupSprite2.rect = CupSprite2.surf.get_rect(center=(current_x2, (HEIGHT // 2)))
            CupSprite1.rect = CupSprite1.surf.get_rect(center=(current_x1, (HEIGHT // 2)))

            DisplaySurface.fill((0, 150, 160))

            for entity in all_sprites:
                DisplaySurface.blit(entity.surf, entity.rect)
            pygame.display.update()

    elif Movement3 == CupSprite1.rect.centerx and current_x2 < target_x2:
        while current_x2 < target_x2 and current_x1 > target_x1:
            current_x2 += speed
            current_x1 -= speed
            if current_x2 > target_x2:
                current_x2 = target_x2
            if current_x1 < target_x1:
                current_x1 = target_x1

            CupSprite2.rect = CupSprite2.surf.get_rect(center=(current_x2, (HEIGHT // 2)))
            CupSprite1.rect = CupSprite1.surf.get_rect(center=(current_x1, (HEIGHT // 2)))

            DisplaySurface.fill((0, 150, 160))

            for entity in all_sprites:
                DisplaySurface.blit(entity.surf, entity.rect)
            pygame.display.update()

    elif Movement3 == CupSprite3.rect.centerx and current_x2 < target_x2:
        while current_x2 < target_x2 and current_x3 > target_x3:
            current_x2 += speed
            current_x3 -= speed
            if current_x2 > target_x2:
                current_x2 = target_x2
            if current_x3 < target_x3:
                current_x3 = target_x3

            CupSprite2.rect = CupSprite2.surf.get_rect(center=(current_x2, (HEIGHT // 2)))
            CupSprite3.rect = CupSprite3.surf.get_rect(center=(current_x3, (HEIGHT // 2)))

            DisplaySurface.fill((0, 150, 160))

            for entity in all_sprites:
                DisplaySurface.blit(entity.surf, entity.rect)
            pygame.display.update()

    elif Movement3 == CupSprite3.rect.centerx and current_x2 > target_x2:
        while current_x2 > target_x2 and current_x3 < target_x3:
            current_x2 -= speed
            current_x3 += speed
            if current_x2 < target_x2:
                current_x2 = target_x2
            if current_x3 > target_x3:
                current_x3 = target_x3

            CupSprite2.rect = CupSprite2.surf.get_rect(center=(current_x2, (HEIGHT // 2)))
            CupSprite3.rect = CupSprite1.surf.get_rect(center=(current_x3, (HEIGHT // 2)))

            DisplaySurface.fill((0, 150, 160))

            for entity in all_sprites:
                DisplaySurface.blit(entity.surf, entity.rect)
            pygame.display.update()

    all_sprites.remove(CupSprite1, CupSprite2, CupSprite3, Player)
    all_sprites.add(BallSprite, CupSprite1, CupSprite2, CupSprite3, Player)
    BallSprite.rect.centerx = CupSprite2.rect.centerx
