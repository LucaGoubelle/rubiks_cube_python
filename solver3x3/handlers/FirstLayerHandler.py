""" first layer handler """

from pyrubik.data.cube import Cube


class FirstLayerHandler:
    """ first layer handler """

    
    def _insertWBR(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube

    
    def _insertWGR(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    
    def _insertWGO(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    
    def _insertWBO(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube

    
    def handle(self, cube: Cube) -> Cube:
        cube = self._insertWBR(cube)
        cube = self._insertWGR(cube)
        cube = self._insertWGO(cube)
        cube = self._insertWBO(cube)
        return cube
