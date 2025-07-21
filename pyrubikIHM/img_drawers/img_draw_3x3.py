
from pyrubikIHM.helpers.img_face_drawer import IMGFaceDrawer
from pyrubikIHM.img_drawers.cube_img_drawer import CubeIMGDrawer

class Cube3x3IMGDrawer(CubeIMGDrawer):
    """
    cube 3x3 img drawer
    @author: LucaGoubelle
    """

    def __init__(self):
        self.face_drawer = IMGFaceDrawer()

    def _draw_front_face(self, img1, cube):
        self.face_drawer.draw_front_face(img1, cube.front, 100, 100)

    def _draw_right_face(self, img1, cube):
        self.face_drawer.draw_right_face(img1, cube.right, 265, 100)

    def _draw_up_face(self, img1, cube):
        self.face_drawer.draw_up_face(img1, cube.up, 185, 10)
