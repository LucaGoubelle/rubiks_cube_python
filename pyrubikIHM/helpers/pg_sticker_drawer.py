""" sticker drawer """
import pygame

class PGStickerDrawer:
    """ sticker drawer """

    def draw_front_sticker(self, screen, x,y, elem, size=50) -> None:
        """
        draw a front (flat) sticker
        @author: LucaGoubelle
        """
        points = [(x,y), (x+size,y), (x+size,y+size), (x,y+size)]
        pygame.draw.polygon(screen, elem, points)
        pygame.draw.polygon(screen, (0,0,0), points, 1)

    def draw_up_sticker(self, screen, x,y, elem, size=50) -> None:
        """
        draw an up sticker
        @author: LucaGoubelle
        """
        half: int = size // 2
        points = [(x, y), (x+size, y), (x+size-half, y+half), (x-half, y+half)]
        pygame.draw.polygon(screen, elem, points)
        pygame.draw.polygon(screen, (0,0,0), points, 1)

    def draw_right_sticker(self, screen, x,y, elem, size=50) -> None:
        """
        draw a right sticker
        @author: LucaGoubelle
        """
        half: int = size // 2
        points = [(x, y), (x+half, y-half), (x+half, y-half+size), (x, y+size)]
        pygame.draw.polygon(screen, elem, points)
        pygame.draw.polygon(screen, (0,0,0), points, 1)
