
from pyrubikIHM.helpers.pg_face_drawer import PGFaceDrawer
from pyrubikIHM.pg_drawers.cube_pg_drawer import CubePGDrawer


class PGDrawer3x3(CubePGDrawer):
    """ PG drawer 3x3 """
    
    def __init__(self):
        self.face_drawer = PGFaceDrawer()
        
    def _draw_front_face(self, screen, cube):
        self.face_drawer.draw_front_face(screen, cube.front, 100, 100)

    def _draw_right_face(self, screen, cube):
        self.face_drawer.draw_right_face(screen, cube.right, 265,100)

    def _draw_up_face(self, screen, cube):
        self.face_drawer.draw_up_face(screen, cube.up, 185,10)
