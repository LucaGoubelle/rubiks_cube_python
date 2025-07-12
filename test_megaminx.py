""" test megaminx """
from pyminx.data.minx_factory import MinxFactory
from pyminxIHM.draw_megaminx import MegaminxDrawer

facto = MinxFactory()
drawer = MegaminxDrawer()
minx = facto.make("megaminx")

drawer.draw(minx)
