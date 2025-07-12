from PIL import Image, ImageDraw

class CubeIMGDrawer:
    """ abs class for drawer """

    def draw(self, cube, title=None):
        img = Image.new("RGB", (800, 600), "#323232")
        img1 = ImageDraw.Draw(img)
        self._draw_front_face(img1, cube)
        self._draw_right_face(img1, cube)
        self._draw_up_face(img1, cube)
        img.show(title=title)
