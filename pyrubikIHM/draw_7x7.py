
from pyrubikIHM.helpers.face_drawer import FaceDrawer
from pyrubikIHM.cube_img_drawer import CubeIMGDrawer

class Cube7x7IMGDrawer(CubeIMGDrawer):
    """ cube 7x7 img drawer """

    def __init__(self):
        self.face_drawer = FaceDrawer()

    def _draw_front_face(self, img1, cube):
        self.face_drawer.draw_front_face(img1, cube.front, 100,105, size=20)

    def _draw_right_face(self, img1, cube):
        self.face_drawer.draw_right_face(img1, cube.right, 275, 105, size=20)

    def _draw_up_face(self, img1, cube):
        self.face_drawer.draw_up_face(img1, cube.up, 200, 0, size=20)
