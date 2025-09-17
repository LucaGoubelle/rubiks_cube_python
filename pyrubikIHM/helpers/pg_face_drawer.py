""" face drawer """
from pyrubikIHM.helpers.pg_sticker_drawer import PGStickerDrawer

class PGFaceDrawer:
    """ 
    face drawer 
    @author: LucaGoubelle
    """

    def __init__(self):
        self.sticker_drawer = PGStickerDrawer()

    def draw_front_face(self, screen, face, x,y, size=50, offset=5) -> None:
        """
        draw a front face of stickers
        @author: LucaGoubelle
        """
        for i in range(len(face)):
            for j in range(len(face)):
                self.sticker_drawer.draw_front_sticker(
                    screen,
                    x+(j*size)+(j*offset),
                    y+(i*size)+(i*offset),
                    face[i][j],
                    size=size
                )

    def draw_right_face(self, screen, face, x,y, size=50, offset=5):
        """
        draw a right face of stickers
        @author: LucaGoubelle
        """
        half = size // 2
        for i in range(len(face)):
            for j in range(len(face)):
                self.sticker_drawer.draw_right_sticker(
                    screen,
                    x+(j*half)+(j*offset),
                    y+(i*size)+(i*offset)-((j*half)+(j*offset)),
                    face[i][j],
                    size=size
                )

    def draw_up_face(self, screen, face, x,y, size=50, offset=5):
        """
        draw a up face of stickers
        @author: LucaGoubelle
        """
        half = size // 2
        for i in range(len(face)):
            for j in range(len(face)):
                self.sticker_drawer.draw_up_sticker(
                    screen,
                    x+(j*size)+(j*offset)-((i*half)+(i*offset)),
                    y+(i*half)+(i*offset),
                    face[i][j],
                    size=size
                )
