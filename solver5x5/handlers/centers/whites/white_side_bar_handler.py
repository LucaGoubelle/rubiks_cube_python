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
            # todo: implement this part
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
