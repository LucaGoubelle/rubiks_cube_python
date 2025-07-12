import sys; sys.dont_write_bytecode=True

from solver6x6.solver6x6 import Solver6x6

from pyrubik.data.cube import Cube
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.scrambler import CubeScrambler
from pyrubik.display.printer import CubePrinter

builder = CubeBuilder()
printer = CubePrinter()
scrambler = CubeScrambler()
cube: Cube = builder.build(6)
solver: Solver6x6 = Solver6x6()

# first we scramble the cube
cube = scrambler.scramble(cube)
printer.print_cube(cube)

print("\n---------------------------------------------------\n")

# then we solve the cube
cube = solver.solve(cube)
printer.print_cube(cube)
