from typing import List
from random import randint

from pyrubik.data.cube import Cube
from pyrubik.moves.mover import Mover


class CubeScrambler:
    """ scrambler for cube """

    def scramble(self, cube: Cube) -> Cube:
        """ scramble cube """
        size: int = len(cube.front)
        match size:
            case 2: return self.scramble_simple_cube(cube)
            case 3: return self.scramble_simple_cube(cube)
            case 4: return self.scramble_big_cube(cube)
            case 5: return self.scramble_big_cube(cube)
            case _: return self.scramble_simple_cube(cube)
    
    def scramble_simple_cube(self, cube: Cube) -> Cube:
        """ scramble simple cube """
        scrambles: List[str] = [
            "U F' D L2 R2 U2 R2 L D R' F2 L2 D' R F D U D2 F L' F2 R2 D2 L' U2",
            "D U' D' U2 D' F L' R2 U2 F2 L' D2 F2 D F D' L R' D' U' D F D' F L'",
            "D' L U L U' D' U R B2 D2 U2 F' L2 D F' L U' D' F2 D' U2 R2 D U D'",
            "R L' D2 U2 D2 R' D U' R D2 F' L F2 D' F2 U D' R' D' R U' D2 L D F'",
            "D F' F2 U2 F U L F2 R' F2 R2 U2 F2 U2 L R F D2 F' U D2 F' D' U2"
        ]
        scrambling: str = scrambles[randint(0, len(scrambles)-1)]
        mover = Mover()
        cube = mover.multi_moves(cube, scrambling)
        return cube

    def scramble_big_cube(self, cube: Cube) -> Cube:
        """ scramble big cubes """
        scrambling: str = "R' F R' Fw Uw Rw2 F2 Uw2 Fw' R F Uw' Rw F U' Rw F' U' Fw Uw' F R U2 Fw Rw2 F U F2 U' Rw"
        scrambling += " Uw2 F R' F2 R2 F' Uw' Rw F' R' Fw2 U' F2 R' U F' Uw' Fw2 Uw' Rw2 Fw Uw R2 Fw2 U Rw U2 Fw2 U2 Fw"
        mover = Mover()
        cube = mover.multi_moves(cube, scrambling)
        return cube
