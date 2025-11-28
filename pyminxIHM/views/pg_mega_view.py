from pyminx.data.minx_factory import MinxFactory
from pyminxIHM.pg_drawers.pg_draw_megaminx import PGMegaminxDrawer
from pyminxIHM.views.pg_view import PGView


class PygameMegaminxView(PGView):
    """ pygame megaminx view """

    def __init__(self, title):
        super().__init__(title)
        self.pg_draw_mega = PGMegaminxDrawer()
        factory = MinxFactory()
        self.minx = factory.make("megaminx")
        
    def _render(self):
        self.pg_draw_mega.draw(self.screen, self.minx)
