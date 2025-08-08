from pyrubik.data.cube import Cube


class WhiteSideBarHandler:
    """ white side bars handler """

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
        #todo: implement this
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
        #todo: implement this
        return cube
    
    def _find_center_edge2(self, cube: Cube) -> Cube:
        #todo: implement this
        return cube
