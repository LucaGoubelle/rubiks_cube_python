import sys; sys.dont_write_bytecode=True

from pyrubikIHM.drawer_img_factory import DrawerIMGFactory

from pyrubik.data.cube import Cube
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.data.cube_dumper import CubeDumper
from pyrubik.moves.scrambler import CubeScrambler
from pyrubik.display.printer import CubePrinter

size_cube: int = 3

facto = DrawerIMGFactory()
builder = CubeBuilder()
printer = CubePrinter()
dumper = CubeDumper()
scrambler = CubeScrambler()
drawer = facto.make(size_cube)

cube: Cube = builder.build(size_cube)

printer.print_cube(cube)
drawer.draw(cube)

print("\n---------------------------------------------------\n")

cube = scrambler.scramble(cube)
printer.print_cube(cube)
drawer.draw(cube)

print(dumper.dump_to_xml(cube))
