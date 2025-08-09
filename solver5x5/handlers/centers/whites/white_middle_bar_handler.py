from pyrubik.data.cube import Cube
from pyrubik.moves.mover import Mover
from solver_helpers.seekers.center_5_seeker import Center5Seeker


class WhiteMiddleBarHandler:
    """ white middle bar handler """

    def __init__(self):
        self.mover = Mover()
        self.center_seeker = Center5Seeker()

    def handle(self, cube: Cube) -> Cube:
        cube = self._handle_first_center_edge(cube)
        cube = self._handle_second_center_edge(cube)
        cube = self.mover.simple_move(cube, "D")
        return cube
        
    def _handle_first_center_edge(self, cube: Cube) -> Cube:
        count: int = 0
        while count < 4:
            result: str = self.center_seeker.seek_center_edge(cube, "front", "white")
            result2: str = self.center_seeker.seek_center_edge(cube, "up", "white")
            # map front
            hmap = {}
            hmap["front::up"] = "F Rw' D2"
            hmap["front::down"] = "F' Rw' D2"
            hmap["front::left"] = "F2 Rw' D2"
            hmap["front::right"] = "Rw' D2"

            # map up
            hmap2 = {}
            hmap["up::front"] = "U' Rw2 D2"
            hmap["up::right"] = "Rw2 D2"
            hmap["up::back"] = "U Rw2 D2"
            hmap["up::left"] = "U2 Rw2 D2"

            if result in hmap:
                cube = self.mover.multi_moves(cube, hmap[result])
                break
            elif result2 in hmap2:
                cube = self.mover.multi_moves(cube, hmap2[result2])
                break
            else:
                cube = self.mover.multi_moves(cube, "D y")
                count += 1
        return cube
    
    def _handle_second_center_edge(self, cube: Cube) -> Cube:
        count: int = 0
        while count < 4 :
            result: str = self.center_seeker.seek_center_edge(cube, "front", "white")
            result2: str = self.center_seeker.seek_center_edge(cube, "up", "white")
            # map front
            hmap = {}
            hmap["front::up"] = "F Rw' D"
            hmap["front::down"] = "F' Rw' D"
            hmap["front::left"] = "F2 Rw' D"
            hmap["front::right"] = "Rw' D"

            # map up
            hmap2 = {}
            hmap["up::front"] = "U' Rw2 D"
            hmap["up::right"] = "Rw2 D"
            hmap["up::back"] = "U Rw2 D"
            hmap["up::left"] = "U2 Rw2 D"

            if result in hmap:
                cube = self.mover.multi_moves(cube, hmap[result])
                break
            elif result2 in hmap2:
                cube = self.mover.multi_moves(cube, hmap2[result2])
                break
            else:
                cube = self.mover.multi_moves(cube, "D y")
                count += 1
            
        return cube
