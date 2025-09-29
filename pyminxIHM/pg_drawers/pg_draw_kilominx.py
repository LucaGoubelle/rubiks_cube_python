""" draw kilominx """
import pygame

class PGKilominxDrawer:
    """ draw kilominx """
    
    def draw(self, screen, minx):
        self._draw_up(screen, minx.up)
        self._draw_front(screen, minx.front)
        self._draw_left(screen, minx.left)
        self._draw_right(screen, minx.right)
        self._draw_down_left(screen, minx.down_left)
        self._draw_down_right(screen, minx.down_right)
        
    def _draw_sticker(self, screen, elem, pts):
        pygame.draw.polygon(screen, elem, pts)
        pygame.draw.polygon(screen, (0,0,0), pts, 1)
        
    def _draw_up(self, screen, face):
        self._draw_sticker(screen, face[0], [(250,7), (320,30), (250,73), (179,30)])
        self._draw_sticker(screen, face[1], [(320,30), (392,53 ), (365,91 ), (250,73)])
        self._draw_sticker(screen, face[2], [(365,91), (338,128), (250,128), (250,73)])
        self._draw_sticker(screen, face[3], [(250,128), (161,128), (135,91 ), (250,73)])
        self._draw_sticker(screen, face[4], [(135,91), (107,53 ), (179,30 ), (250,73)])
    
    def _draw_front(self, screen, face):
        pass
    
    def _draw_left(self, screen, face):
        pass
    
    def _draw_right(self, screen, face):
        pass
    
    def _draw_down_left(self, screen, face):
        pass
    
    def _draw_down_right(self, screen, face):
        pass
