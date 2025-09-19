""" pygame 5x5 view """
from pyrubik.data.cube_builder import CubeBuilder
from pyrubikIHM.pg_drawers.pg_draw_5x5 import PGDrawer5x5
from pyrubikIHM.views.pg_view import PGView

class Pygame5x5View(PGView):
    """ pygame 5x5 view """
    
    def __init__(self, title):
        super().__init__(title)
        self.pg_drawer = PGDrawer5x5()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(5)
        
    def _render(self):
        self.pg_drawer.draw(self.screen, self.cube)
