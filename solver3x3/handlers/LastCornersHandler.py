""" last corners handler """

from pyrubik.data.cube import Cube

class LastCornersHandler:
    """ last corners handler """

    def _permute(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    def _orient(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube

    def handle(self, cube: Cube) -> Cube:
        cube = self._permute(cube)
        cube = self._orient(cube)
        return cube
