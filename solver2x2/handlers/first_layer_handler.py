""" first layer handler """

from pyrubik.data.cube import Cube


class FirstLayerHandler:
    """ first layer handler """

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
        cube = FirstLayerHandler._insertWGR(cube)
        cube = FirstLayerHandler._insertWGO(cube)
        cube = FirstLayerHandler._insertWBO(cube)
        return cube
