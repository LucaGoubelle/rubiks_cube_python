""" 
entry point for console simulation
"""
import sys
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.data.cube_dumper import CubeDumper
from pyrubik.display.printer import CubePrinter
from pyrubik.moves.mover import Mover
from pyrubik.moves.scrambler import CubeScrambler

sys.dont_write_bytecode=True

builder = CubeBuilder()
mover = Mover()
dumper = CubeDumper()
scrambler = CubeScrambler()
printer = CubePrinter()

size_cube: int = 3
cube = builder.build(size_cube)

while True:
    # printing the cube
    printer.print_cube(cube)
    
    # user input
    inp = input("\nENTER A MOVE OR CMD :")
    
    # move handle
    cube = mover.simple_move(cube, inp)
    
    # CMD Handle
    if inp == "scramble":
        cube = scrambler.scramble(cube)
    elif inp == "init":
        cube = builder.build(size_cube)
    elif inp == "dump":
        print(dumper.dump(cube))
    elif inp == "exit":
        break
    
    # IHM jump
    print("\n\n------------------------------------------\n\n")
