import sys; sys.dont_write_bytecode=True

from pyrubikIHM.drawer_factory import DrawerFactory

from pyrubik.data.cube import Cube
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.scrambler import CubeScrambler
from pyrubik.display.printer import CubePrinter

size_cube: int = 4

facto = DrawerFactory()
builder = CubeBuilder()
printer = CubePrinter()
scrambler = CubeScrambler()
drawer = facto.make(size_cube)

cube: Cube = builder.build(size_cube)

printer.print_cube(cube)
drawer.draw(cube)

print("\n---------------------------------------------------\n")

cube = scrambler.scramble(cube)
printer.print_cube(cube)
drawer.draw(cube)

