from pyrubik.data.cube import Cube
from pyrubik.moves.mover import Mover
from solver_helpers.seekers.center_5_seeker import Center5Seeker


class WhiteSideBarHandler:
    """ white side bars handler """
    
    def __init__(self):
        self.center_seeker = Center5Seeker()
        self.mover = Mover()

    def handle(self, cube: Cube) -> Cube:
        cube = self._do_first_side_bar(cube)
        cube = self._do_second_side_bar(cube)
        return cube

    ##################################
    # first side bar
    ##################################
    
    def _do_first_side_bar(self, cube: Cube) -> Cube:
        cube = self._find_center_edge1(cube)
        cube = self._solve_first_center_corner1(cube)
        cube = self._solve_second_center_corner1(cube)
        #todo: implement remaining lines
        return cube

    def _find_center_edge1(self, cube: Cube) -> Cube:
        focus_center_edge: str = cube.front[2][3]
        if focus_center_edge == "white":
            return cube # nothing to do
        else:
            # check up
            result_up: str = self.center_seeker.seek_center_edge(cube, "up", "white")
            hmap_up: dict = {}
            hmap_up["up::right"] = "Rw'"
            hmap_up["up::front"] = "U' Rw'"
            hmap_up["up::back"] = "U Rw'"
            hmap_up["up::left"] = "U2 Rw'"

            sequence: str = hmap_up[result_up] if result_up in hmap_up else "???"
            if sequence != "???":
                cube = self.mover.multi_moves(cube, sequence)
                return cube
            
            # check front
            i: int = 0
            while i < 4:
                
                # todo: implement this part
                i += 1
            return cube
    
    def _solve_first_center_corner1(self, cube: Cube) -> Cube:
        #todo: implement this
        return cube
    
    def _solve_second_center_corner1(self, cube: Cube) -> Cube:
        #todo: implement this
        return cube

    ##################################
    # second side bar
    ##################################

    def _do_second_side_bar(self, cube: Cube) -> Cube:
        cube = self._find_center_edge2(cube)
        cube = self._solve_first_center_corner2(cube)
        cube = self._solve_second_center_corner2(cube)
        #todo: implement remaining lines
        return cube
    
    def _find_center_edge2(self, cube: Cube) -> Cube:
        #todo: implement this
        return cube

    def _solve_first_center_corner2(self, cube: Cube) -> Cube:
        #todo: implement this
        return cube
    
    def _solve_second_center_corner2(self, cube: Cube) -> Cube:
        #todo: implement this
        return cube
