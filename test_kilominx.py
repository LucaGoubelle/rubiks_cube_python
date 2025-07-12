""" test kilominx """
from pyminx.data.minx_factory import MinxFactory
from pyminx.moves.kilominx.kilominx_mover import KilominxMover
from pyminxIHM.draw_kilominx import KilominxDrawer

facto = MinxFactory()
drawer = KilominxDrawer()
mover = KilominxMover()

minx = facto.make("kilominx")
drawer.draw(minx)


# ------ move U test ----------
minx = mover.simple_move(minx, "y'")

drawer.draw(minx)
