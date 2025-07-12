from pyrubikIHM.helpers.face_drawer import FaceDrawer
from pyrubikIHM.cube_img_drawer import CubeIMGDrawer

class Cube2x2IMGDrawer(CubeIMGDrawer):
    """
    cube 2x2 img drawer
    @author: LucaGoubelle
    """

    def __init__(self):
        self.face_drawer = FaceDrawer()

    def _draw_front_face(self, img1, cube):
        self.face_drawer.draw_front_face(img1, cube.front, 100, 100)

    def _draw_right_face(self, img1, cube):
        self.face_drawer.draw_right_face(img1, cube.right, 210, 100)

    def _draw_up_face(self, img1, cube):
        self.face_drawer.draw_up_face(img1, cube.up, 155, 40)
