import sys; sys.dont_write_bytecode=True

from pyrubikIHM.draw_7x7 import Cube7x7IMGDrawer

from pyrubik.data.cube import Cube
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.scrambler import CubeScrambler
from pyrubik.display.printer import CubePrinter

builder = CubeBuilder()
printer = CubePrinter()
scrambler = CubeScrambler()
drawer = Cube7x7IMGDrawer()
cube: Cube = builder.build(7)

printer.print_cube(cube)
drawer.draw(cube)

print("\n---------------------------------------------------\n")

cube = scrambler.scramble(cube)
printer.print_cube(cube)
drawer.draw(cube)

