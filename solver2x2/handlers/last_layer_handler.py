""" last layer handler """


from pyrubik.data.cube import Cube


class LastLayerHandler:
    """ last layer handler """

    
    def _oll(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    
    def _pll(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube
    
    
    def _auf(self, cube: Cube) -> Cube:
        # TODO: implement this method
        return cube

    
    def handle(self, cube: Cube) -> Cube:
        cube = self._oll(cube)
        cube = self._pll(cube)
        cube = self._auf(cube)
        return cube
