from pyrubik.data.cube import Cube
from pyrubik.moves.mover import Mover


class WhiteMiddleBarHandler:
    """ white middle bar handler """

    def __init__(self):
        self.mover = Mover()

    def handle(self, cube: Cube) -> Cube:
        cube = self.__seek_on_up_centers(cube)
        after_result: str = cube.down[2][1]+"_"+cube.down[2][3]
        if after_result == "white_white":
            return cube # nothing to do
        else:
            # TODO:  deal with other cases here
            return cube
        
    def __seek_on_up_centers(self, cube: Cube) -> Cube:
        center_edge_1: str = cube.up[1][2]
        center_edge_2: str = cube.up[2][1]
        center_edge_3: str = cube.up[2][3]
        center_edge_4: str = cube.up[3][2]
        result_seek: str = "1" if center_edge_1 == "white" else "0"
        result_seek += "1" if center_edge_2 == "white" else "0"
        result_seek += "1" if center_edge_3 == "white" else "0"
        result_seek += "1" if center_edge_4 == "white" else "0"
        hmap_results: dict = {
            "1111": "Lw2 Rw2",
            "0110": "Lw2 Rw2",
            "1001": "U Lw2 Rw2",
            "1100": "Lw2 U Rw2",
            "1010": "Rw2 U' Lw2",
            "0011": "Rw2 U Lw2",
            "0101": "Lw2 U' Rw2"
        }
        sequence: str = hmap_results[result_seek] if result_seek in hmap_results else "???"
        return self.mover.multi_moves(cube, sequence)
