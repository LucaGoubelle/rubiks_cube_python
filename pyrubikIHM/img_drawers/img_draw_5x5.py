from PIL import Image, ImageDraw
from pyrubikIHM.helpers.img_face_drawer import IMGFaceDrawer
from pyrubikIHM.img_drawers.cube_img_drawer import CubeIMGDrawer

class Cube5x5IMGDrawer(CubeIMGDrawer):
    """ cube 5x5 img drawer """

    def __init__(self):
        self.face_drawer = IMGFaceDrawer()
        self.size = 30

    def _draw_front_face(self, img1, cube):
        self.face_drawer.draw_front_face(img1, cube.front, 100,100, size=self.size)

    def _draw_right_face(self, img1, cube):
        self.face_drawer.draw_right_face(img1, cube.right, 275, 100, size=self.size)

    def _draw_up_face(self, img1, cube):
        self.face_drawer.draw_up_face(img1, cube.up, 195, 0, size=self.size)
