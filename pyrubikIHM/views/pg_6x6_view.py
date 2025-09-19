""" pygame 6x6 view """
from pyrubik.data.cube_builder import CubeBuilder
from pyrubikIHM.pg_drawers.pg_draw_6x6 import PGDrawer6x6
from pyrubikIHM.views.pg_view import PGView

class Pygame6x6View(PGView):
    """ pygame 6x6 view """
    
    def __init__(self, title):
        super().__init__(title)
        self.pg_drawer = PGDrawer6x6()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(6)
        
    def _render(self):
        self.pg_drawer.draw(self.screen, self.cube)
