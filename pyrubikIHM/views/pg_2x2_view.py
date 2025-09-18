
from pyrubik.data.cube_builder import CubeBuilder
from pyrubikIHM.pg_drawers.pg_draw_2x2 import PGDrawer2x2
from pyrubikIHM.views.pg_view import PGView


class Pygame2x2View(PGView):
    """ pygame 2x2 view """
    
    def __init__(self, title):
        super().__init__(title)
        self.pg_draw_2x2 = PGDrawer2x2()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(2)
        
    def _render(self):
        self.pg_draw_2x2.draw(self.screen, self.cube)