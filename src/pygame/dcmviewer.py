#!/usr/bin/env python3
import pygame
from pygame.locals import *


def main():
    screen = pygame.display.set_mode((512, 512))
    pygame.display.set_caption("dicom_viewer")
    clock = pygame.time.Clock()
    while True:
       
        clock.tick(30)


        (x, y) = pygame.mouse.get_pos()


 
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        pygame.display.update()


if __name__ == '__main__':
    main()