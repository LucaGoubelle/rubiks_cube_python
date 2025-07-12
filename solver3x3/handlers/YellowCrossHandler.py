""" yellow cross handler """

from pyrubik.data.cube import Cube

class YellowCrossHandler:
    """ yellow cross handler """

    
    def _create(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube

    
    def _correct(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    
    def handle(self, cube: Cube) -> Cube:
        cube = self._create(cube)
        cube = self._correct(cube)
        return cube
