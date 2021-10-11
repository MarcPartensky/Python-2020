#!/usr/bin/env python

"""Début de jeu de pong fait avec baptiste."""

import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("baptiste")
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        print(event)

    pygame.display.update()
    clock.tick(60)
