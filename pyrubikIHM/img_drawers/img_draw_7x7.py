
from pyrubikIHM.helpers.img_face_drawer import IMGFaceDrawer
from pyrubikIHM.img_drawers.cube_img_drawer import CubeIMGDrawer

class Cube7x7IMGDrawer(CubeIMGDrawer):
    """ cube 7x7 img drawer """

    def __init__(self):
        self.face_drawer = IMGFaceDrawer()
        self.front_coord = {"x": 100, "y": 105}
        self.right_coord = {"x": 275, "y": 105}
        self.up_coord = {"x": 200, "y": 0}
        self.size = 20

    def _draw_front_face(self, img1, cube):
        self.face_drawer.draw_front_face(img1, cube.front, self.front_coord["x"], self.front_coord["y"], size=self.size)

    def _draw_right_face(self, img1, cube):
        self.face_drawer.draw_right_face(img1, cube.right, self.right_coord["x"], self.right_coord["y"], size=self.size)

    def _draw_up_face(self, img1, cube):
        self.face_drawer.draw_up_face(img1, cube.up, self.up_coord["x"], self.up_coord["y"], size=self.size)
