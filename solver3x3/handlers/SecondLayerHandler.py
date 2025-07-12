""" second layer handler """

from pyrubik.data.cube import Cube

class SecondLayerHandler:
    """ second layer handler """

    
    def _insertBR(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    
    def _insertGR(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    
    def _insertGO(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    
    def _insertBO(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube

    
    def handle(self, cube: Cube) -> Cube:
        cube = self._insertBR(cube)
        cube = self._insertGR(cube)
        cube = self._insertGO(cube)
        cube = self._insertBO(cube)
        return cube