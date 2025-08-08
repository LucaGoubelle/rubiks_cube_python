import sys; sys.dont_write_bytecode=True

from solver5x5.solver5x5 import Solver5x5

from pyrubik.data.cube import Cube
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.scrambler import CubeScrambler
from pyrubik.display.printer import CubePrinter

builder = CubeBuilder()
printer = CubePrinter()
scrambler = CubeScrambler()

size_cube: int = 5
cube: Cube = builder.build(size_cube)
solver: Solver5x5 = Solver5x5()

# first we scramble the cube
cube = scrambler.scramble(cube)
printer.print_cube(cube)

print("\n---------------------------------------------------\n")

# then we solve the cube
cube = solver.solve(cube)
printer.print_cube(cube)
