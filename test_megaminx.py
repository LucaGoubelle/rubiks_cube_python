""" test megaminx """
from pyminx.data.minx_dumper import MinxDumper
from pyminx.data.minx_factory import MinxFactory
from pyminxIHM.draw_megaminx import MegaminxDrawer

facto = MinxFactory()
dumper = MinxDumper()
drawer = MegaminxDrawer()

puzzle_type: str = "megaminx"
minx = facto.make(puzzle_type)

drawer.draw(minx)

print(dumper.dump_to_xml(minx))
