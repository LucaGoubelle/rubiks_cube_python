
from pyrubik.data.cube_builder import CubeBuilder
from pyrubikIHM.pg_drawers.pg_draw_3x3 import PGDrawer3x3
from pyrubikIHM.views.pg_view import PGView


class Pygame3x3View(PGView):
    """ pygame 3x3 view """

    def __init__(self, title):
        super().__init__(title)
        self.pg_drawer = PGDrawer3x3()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(3)

    def _render(self):
        self.pg_drawer.draw(self.screen, self.cube)
