""" pygame 4x4 view """
from pyrubik.data.cube_builder import CubeBuilder
from pyrubikIHM.pg_drawers.pg_draw_4x4 import PGDrawer4x4
from pyrubikIHM.views.pg_view import PGView


class Pygame4x4View(PGView):
    """ pygame 4x4 view """
    
    def __init__(self, title):
        super().__init__(title)
        self.pg_drawer = PGDrawer4x4()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(4)
        
    def _render(self):
        self.pg_drawer.draw(self.screen, self.cube)
