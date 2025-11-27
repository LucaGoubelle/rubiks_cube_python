""" draw kilominx """
from pyminxIHM.pg_drawers.minx_pg_drawer import MinxPGDrawer

class PGKilominxDrawer(MinxPGDrawer):
    """ draw kilominx """
    
    def draw(self, screen, minx):
        self._draw_up(screen, minx.up)
        self._draw_front(screen, minx.front)
        self._draw_left(screen, minx.left)
        self._draw_right(screen, minx.right)
        self._draw_down_left(screen, minx.down_left)
        self._draw_down_right(screen, minx.down_right)
        
    def _draw_up(self, screen, face):
        self._draw_sticker(screen, face[0], [(250,7), (320,30), (250,73), (179,30)])
        self._draw_sticker(screen, face[1], [(320,30), (392,53 ), (365,91 ), (250,73)])
        self._draw_sticker(screen, face[2], [(365,91), (338,128), (250,128), (250,73)])
        self._draw_sticker(screen, face[3], [(250,128), (161,128), (135,91 ), (250,73)])
        self._draw_sticker(screen, face[4], [(135,91), (107,53 ), (179,30 ), (250,73)])
    
    def _draw_front(self, screen, face):
        self._draw_sticker(screen, face[0], [(161,128), (250,128), (250,250), (134,212)])
        self._draw_sticker(screen, face[1], [(250,128), (338,128), (365,212), (250,250)])
        self._draw_sticker(screen, face[2], [(365,212), (392,296), (321,348), (250,250)])
        self._draw_sticker(screen, face[3], [(321,348), (250,399), (178,348), (250,250)])
        self._draw_sticker(screen, face[4], [(178,348), (107,296), (134,212), (250,250)])
    
    def _draw_left(self, screen, face):
        self._draw_sticker(screen, face[0], [(107,53), (135,91), (83,194), (63,114)])
        self._draw_sticker(screen, face[1], [(135,91), (161,128), (134,212), (83,194)])
        self._draw_sticker(screen, face[2], [(134,212), (107,296), (63,310), (83,194)])
        self._draw_sticker(screen, face[3], [(63,310), (19,325), (19,249), (83,194)])
        self._draw_sticker(screen, face[4], [(19,249), (19,174), (63,114), (83,194)])
    
    def _draw_right(self, screen, face):
        self._draw_sticker(screen, face[0], [(338,128), (365,91 ), (417,194), (365,212)])
        self._draw_sticker(screen, face[1], [(365,91 ), (392,53 ), (437,114), (417,194)])
        self._draw_sticker(screen, face[2], [(437,114), (480,174), (480,250), (417,194)])
        self._draw_sticker(screen, face[3], [(480,250), (480,325), (436,310), (417,194)])
        self._draw_sticker(screen, face[4], [(436,310), (392,296), (365,212), (417,194)])
    
    def _draw_down_left(self, screen, face):
        self._draw_sticker(screen, face[0], [(107,296), (178,348), (146,392), ( 63,310)])
        self._draw_sticker(screen, face[1], [(178,348), (250,399), (250,446), (146,392)])
        self._draw_sticker(screen, face[2], [(250,446), (250,492), (177,469), (146,392)])
        self._draw_sticker(screen, face[3], [(177,469), (107,446), (63,386 ), (146,392)])
        self._draw_sticker(screen, face[4], [(63,386 ), (19,325 ), (63,310 ), (146,392)])
    
    def _draw_down_right(self, screen, face):
        self._draw_sticker(screen, face[0], [(392,296), (436,310), (353,392), (321,348)])
        self._draw_sticker(screen, face[1], [(436,310), (480,325), (436,386), (353,392)])
        self._draw_sticker(screen, face[2], [(436,386), (392,446), (321,469), (353,392)])
        self._draw_sticker(screen, face[3], [(321,469), (250,492), (250,446), (353,392)])
        self._draw_sticker(screen, face[4], [(250,446), (250,399), (321,348), (353,392)])
