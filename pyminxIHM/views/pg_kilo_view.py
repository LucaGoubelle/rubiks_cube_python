
from pyminx.data.minx_factory import MinxFactory
from pyminxIHM.pg_drawers.pg_draw_kilominx import PGKilominxDrawer
from pyminxIHM.views.pg_view import PGView


class PygameKilominxView(PGView):
    """ pygame kilominx view """
    
    def __init__(self, title):
        super().__init__(title)
        self.pg_draw_kilo = PGKilominxDrawer()
        factory = MinxFactory()
        self.minx = factory.make("kilominx")
        
    def _render(self):
        self.pg_draw_kilo.draw(self.screen, self.minx)
