""" pygame drawer 6x6 """
from pyrubikIHM.helpers.pg_face_drawer import PGFaceDrawer
from pyrubikIHM.pg_drawers.cube_pg_drawer import CubePGDrawer


class PGDrawer6x6(CubePGDrawer):
    """ pygame drawer 6x6 """
    
    def __init__(self):
        self.face_drawer = PGFaceDrawer()
        self.size = 25
        
    def _draw_front_face(self, screen, cube):
        self.face_drawer.draw_front_face(screen, cube.front, 100,100, size=self.size)

    def _draw_right_face(self, screen, cube):
        self.face_drawer.draw_right_face(screen, cube.right, 280, 100, size=self.size)

    def _draw_up_face(self, screen, cube):
        self.face_drawer.draw_up_face(screen, cube.up, 200, 0, size=self.size)
