""" test master kilominx """
from pyminx.data.minx_factory import MinxFactory
from pyminxIHM.draw_master_kilominx import MasterKilominxDrawer

facto = MinxFactory()
drawer = MasterKilominxDrawer()
minx = facto.make("master_kilominx")

drawer.draw(minx)
