""" pygame drawer 5x5 """
from pyrubikIHM.pg_drawers.cube_pg_drawer import CubePGDrawer
from pyrubikIHM.helpers.pg_face_drawer import PGFaceDrawer

class PGDrawer5x5(CubePGDrawer):
    """ pygame drawer 5x5 """

    def __init__(self):
        self.face_drawer = PGFaceDrawer()
        self.size = 30

    def _draw_front_face(self, screen, cube):
        self.face_drawer.draw_front_face(screen, cube.front, 100,100, size=self.size)

    def _draw_right_face(self, screen, cube):
        self.face_drawer.draw_right_face(screen, cube.right, 275, 100, size=self.size)

    def _draw_up_face(self, screen, cube):
        self.face_drawer.draw_up_face(screen, cube.up, 195, 0, size=self.size)
