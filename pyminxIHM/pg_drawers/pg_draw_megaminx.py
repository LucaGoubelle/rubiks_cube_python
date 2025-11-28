""" draw megaminx """
from pyminxIHM.pg_drawers.minx_pg_drawer import MinxPGDrawer

class PGMegaminxDrawer(MinxPGDrawer):
    """ draw megaminx """

    def draw(self, screen, minx):
        self._draw_body(screen)
        self._draw_up(screen, minx.up)
        self._draw_front(screen, minx.front)
        self._draw_left(screen, minx.left)
        self._draw_right(screen, minx.right)
        self._draw_down_left(screen, minx.down_left)
        self._draw_down_right(screen, minx.down_right)

    def _draw_body(self, screen):
        self._draw_sticker(screen, "black",[
            (123, 20), (193, 35), (230, 94), (237, 164), (192, 219),
            (129, 246), (61, 222), (17, 169), (19, 97), (57, 37)
        ])
    
    def _draw_up(self, screen, face):
        self._draw_sticker(screen, face[0][0], [(123,21), (146,26), (125,31), (102,26)])
        self._draw_sticker(screen, face[0][1], [(151,26), (159,29), (152,38), (130,32)])
        self._draw_sticker(screen, face[0][2], [(166,29), (190,35), (183,45), (158,39)])
        self._draw_sticker(screen, face[0][3], [(157,41), (182,47), (180,50), (150,50)])
        self._draw_sticker(screen, face[0][4], [(148,53), (178,53), (172,63), (141,63)])

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
