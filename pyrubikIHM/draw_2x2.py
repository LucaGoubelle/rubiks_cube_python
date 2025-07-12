from PIL import Image, ImageDraw
from pyrubikIHM.helpers.sticker_drawer import StickerDrawer


class Cube2x2IMGDrawer:
    """
    cube 2x2 img drawer
    @author: LucaGoubelle
    """

    def __init__(self):
        self.drawer = StickerDrawer()

    def draw(self, cube, title=None):
        """
        draw a 2x2 cube on a PNG image
        @author: LucaGoubelle
        """
        img = Image.new("RGB", (800, 600), "#323232")
        img1 = ImageDraw.Draw(img)
        self._draw_front_face(img1, cube)
        self._draw_right_face(img1, cube)
        self._draw_up_face(img1, cube)
        img.show(title=title)

    def _draw_front_face(self, img1, cube):
        self.drawer.draw_front_sticker(img1, 100, 100, cube.front[0][0])
        self.drawer.draw_front_sticker(img1, 155, 100, cube.front[0][1])

        self.drawer.draw_front_sticker(img1, 100, 155, cube.front[1][0])
        self.drawer.draw_front_sticker(img1, 155, 155, cube.front[1][1])

    def _draw_right_face(self, img1, cube):
        self.drawer.draw_right_sticker(img1, 210, 100, cube.right[0][0])
        self.drawer.draw_right_sticker(img1, 240, 70, cube.right[0][1])

        self.drawer.draw_right_sticker(img1, 210, 155, cube.right[1][0])
        self.drawer.draw_right_sticker(img1, 240, 125, cube.right[1][1])

    def _draw_up_face(self, img1, cube):
        self.drawer.draw_up_sticker(img1, 155, 40, cube.up[0][0])
        self.drawer.draw_up_sticker(img1, 210, 40, cube.up[0][1])

        self.drawer.draw_up_sticker(img1, 125, 70, cube.up[1][0])
        self.drawer.draw_up_sticker(img1, 180, 70, cube.up[1][1])
