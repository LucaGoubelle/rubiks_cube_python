""" pygame drawer 7x7 """
from pyrubikIHM.helpers.pg_face_drawer import PGFaceDrawer
from pyrubikIHM.pg_drawers.cube_pg_drawer import CubePGDrawer

class PGDrawer7x7(CubePGDrawer):
    """ pygame drawer 7x7 """

    def __init__(self):
        self.face_drawer = PGFaceDrawer()
        self.front_coord = {"x": 100, "y": 105}
        self.right_coord = {"x": 275, "y": 105}
        self.up_coord = {"x": 200, "y": 0}
        self.size = 20

    def _draw_front_face(self, screen, cube):
        self.face_drawer.draw_front_face(screen, cube.front, self.front_coord["x"], self.front_coord["y"], size=self.size)

    def _draw_right_face(self, screen, cube):
        self.face_drawer.draw_right_face(screen, cube.right, self.right_coord["x"], self.right_coord["y"], size=self.size)

    def _draw_up_face(self, screen, cube):
        self.face_drawer.draw_up_face(screen, cube.up, self.up_coord["x"], self.up_coord["y"], size=self.size)
