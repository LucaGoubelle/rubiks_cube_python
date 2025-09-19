""" pygame 7x7 view """
from pyrubik.data.cube_builder import CubeBuilder
from pyrubikIHM.pg_drawers.pg_draw_7x7 import PGDrawer7x7
from pyrubikIHM.views.pg_view import PGView

class Pygame7x7View(PGView):
    """ pygame 7x7 view """

    def __init__(self, title):
        super().__init__(title)
        self.pg_drawer = PGDrawer7x7()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(7)

    def _render(self):
        self.pg_drawer.draw(self.screen, self.cube)
