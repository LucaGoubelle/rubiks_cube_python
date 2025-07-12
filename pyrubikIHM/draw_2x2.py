from pyrubikIHM.helpers.face_drawer import FaceDrawer
from pyrubikIHM.cube_img_drawer import CubeIMGDrawer

class Cube2x2IMGDrawer(CubeIMGDrawer):
    """
    cube 2x2 img drawer
    @author: LucaGoubelle
    """

    def __init__(self):
        self.face_drawer = FaceDrawer()
        self.front_coord = {"x": 100, "y": 100}
        self.right_coord = {"x": 210, "y": 100}
        self.up_coord = {"x": 155, "y": 40}

    def _draw_front_face(self, img1, cube):
        self.face_drawer.draw_front_face(img1, cube.front, self.front_coord["x"], self.front_coord["y"])

    def _draw_right_face(self, img1, cube):
        self.face_drawer.draw_right_face(img1, cube.right, self.right_coord["x"], self.right_coord["y"])

    def _draw_up_face(self, img1, cube):
        self.face_drawer.draw_up_face(img1, cube.up, self.up_coord["x"], self.up_coord["y"])
