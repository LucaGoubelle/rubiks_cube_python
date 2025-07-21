""" draw kilominx """
from PIL import Image, ImageDraw


class KilominxDrawer:
    """
    kilominx drawer
    @author: LucaGoubelle
    """

    def draw(self, minx):
        """
        draw a kilominx on a PNG image
        @author: LucaGoubelle
        """
        img = Image.new("RGB", (800, 600), "#323232")
        img1 = ImageDraw.Draw(img)
        self._draw_up(img1, minx.up)
        self._draw_front(img1, minx.front)
        self._draw_left(img1, minx.left)
        self._draw_right(img1, minx.right)
        self._draw_down_left(img1, minx.down_left)
        self._draw_down_right(img1, minx.down_right)
        img.show()

    def _draw_up(self, img1: ImageDraw, face):
        img1.polygon([(250,7), (320,30), (250,73), (179,30)], fill=face[0], outline="black")
        img1.polygon([(320,30), (392,53 ), (365,91 ), (250,73)], fill=face[1], outline="black")
        img1.polygon([(365,91), (338,128), (250,128), (250,73)], fill=face[2], outline="black")
        img1.polygon([(250,128), (161,128), (135,91 ), (250,73)], fill=face[3], outline="black")
        img1.polygon([(135,91), (107,53 ), (179,30 ), (250,73)], fill=face[4], outline="black")

    def _draw_front(self, img1: ImageDraw, face):
        img1.polygon([(161,128), (250,128), (250,250), (134,212)], fill=face[0], outline="black")
        img1.polygon([(250,128), (338,128), (365,212), (250,250)], fill=face[1], outline="black")
        img1.polygon([(365,212), (392,296), (321,348), (250,250)], fill=face[2], outline="black")
        img1.polygon([(321,348), (250,399), (178,348), (250,250)], fill=face[3], outline="black")
        img1.polygon([(178,348), (107,296), (134,212), (250,250)], fill=face[4], outline="black")

    def _draw_left(self, img1: ImageDraw, face):
        img1.polygon([(107,53 ), (135,91 ), (83,194 ), (63,114)], fill=face[0], outline="black")
        img1.polygon([(135,91 ), (161,128), (134,212), (83,194)], fill=face[1], outline="black")
        img1.polygon([(134,212), (107,296), (63,310 ), (83,194)], fill=face[2], outline="black")
        img1.polygon([(63,310 ), (19,325 ), (19,249 ), (83,194)], fill=face[3], outline="black")
        img1.polygon([(19,249 ), (19,174 ), (63,114 ), (83,194)], fill=face[4], outline="black")

    def _draw_right(self, img1: ImageDraw, face):
        img1.polygon([(338,128), (365,91 ), (417,194), (365,212)], fill=face[0], outline="black")
        img1.polygon([(365,91 ), (392,53 ), (437,114), (417,194)], fill=face[1], outline="black")
        img1.polygon([(437,114), (480,174), (480,250), (417,194)], fill=face[2], outline="black")
        img1.polygon([(480,250), (480,325), (436,310), (417,194)], fill=face[3], outline="black")
        img1.polygon([(436,310), (392,296), (365,212), (417,194)], fill=face[4], outline="black")

    def _draw_down_left(self, img1: ImageDraw, face):
        img1.polygon([(107,296), (178,348), (146,392), (63,310)], fill=face[0], outline="black")
        img1.polygon([(178,348), (250,399), (250,446), (146,392)], fill=face[1], outline="black")
        img1.polygon([(250,446), (250,492), (177,469), (146,392)], fill=face[2], outline="black")
        img1.polygon([(177,469), (107,446), (63,386 ), (146,392)], fill=face[3], outline="black")
        img1.polygon([(63,386 ), (19,325 ), (63,310 ), (146,392)], fill=face[4], outline="black")

    def _draw_down_right(self, img1: ImageDraw, face):
        img1.polygon([(392,296), (436,310), (353,392), (321,348)], fill=face[0], outline="black")
        img1.polygon([(436,310), (480,325), (436,386), (353,392)], fill=face[1], outline="black")
        img1.polygon([(436,386), (392,446), (321,469), (353,392)], fill=face[2], outline="black")
        img1.polygon([(321,469), (250,492), (250,446), (353,392)], fill=face[3], outline="black")
        img1.polygon([(250,446), (250,399), (321,348), (353,392)], fill=face[4], outline="black")
