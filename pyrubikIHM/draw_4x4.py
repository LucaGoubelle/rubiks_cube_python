from PIL import Image, ImageDraw
from pyrubikIHM.helpers.face_drawer import FaceDrawer
from pyrubikIHM.cube_img_drawer import CubeIMGDrawer

class Cube4x4IMGDrawer(CubeIMGDrawer):
    """ cube 4x4 img drawer """

    def __init__(self):
        self.face_drawer = FaceDrawer()

    def draw(self, cube, title=None):
        img = Image.new("RGB", (800, 600), "#323232")
        img1 = ImageDraw.Draw(img)
        self._draw_front_face(img1, cube)
        self._draw_right_face(img1, cube)
        self._draw_up_face(img1, cube)
        img.show(title=title)

    def _draw_front_face(self, img1, cube):
        self.face_drawer.draw_front_face(img1, cube.front, 100,100, size=40)

    def _draw_right_face(self, img1, cube):
        self.face_drawer.draw_right_face(img1, cube.right, 280, 100, size=40)

    def _draw_up_face(self, img1, cube):
        self.face_drawer.draw_up_face(img1, cube.up, 195, 0, size=40)
