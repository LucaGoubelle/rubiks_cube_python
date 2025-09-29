""" minxs pg drawer """
import pygame

class MinxPGDrawer:
    """ Minx PG drawer """
    
    def draw(self, screen, cube):
        # todo: thin about inheritance (code inject) for this mother class
        pass

    def _draw_sticker(self, screen, elem, pts):
        pygame.draw.polygon(screen, elem, pts)
        pygame.draw.polygon(screen, (0,0,0), pts, 1)
