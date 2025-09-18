
from pyrubikIHM.helpers.pg_face_drawer import PGFaceDrawer
from pyrubikIHM.pg_drawers.cube_pg_drawer import CubePGDrawer


class PGDrawer2x2(CubePGDrawer):
    """ PG drawer 2x2 """
    
    def __init__(self):
        self.face_drawer = PGFaceDrawer()
        self.front_coord = {"x": 100, "y": 100}
        self.right_coord = {"x": 210, "y": 100}
        self.up_coord = {"x": 155, "y": 40}
        
    def _draw_front_face(self, screen, cube):
        self.face_drawer.draw_front_face(screen, cube.front, self.front_coord["x"], self.front_coord["y"])

    def _draw_right_face(self, screen, cube):
        self.face_drawer.draw_right_face(screen, cube.right, self.right_coord["x"], self.right_coord["y"])

    def _draw_up_face(self, screen, cube):
        self.face_drawer.draw_up_face(screen, cube.up, self.up_coord["x"], self.up_coord["y"])
