import sys; sys.dont_write_bytecode=True

from solvers_cubes.solver2x2.solver_2x2 import Solver2x2

from pyrubik.data.cube import Cube
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.scrambler import CubeScrambler
from pyrubik.display.printer import CubePrinter

builder = CubeBuilder()
printer = CubePrinter()
scrambler = CubeScrambler()
cube: Cube = builder.build(2)
solver: Solver2x2 = Solver2x2()

# first we scramble the cube
cube = scrambler.scramble(cube)
printer.print_cube(cube)

print("\n---------------------------------------------------\n")

# then we solve the cube
cube = solver.solve(cube)
printer.print_cube(cube)
