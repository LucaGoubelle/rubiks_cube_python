""" cube dumper """
import json
from pyrubik.data.cube import Cube

class CubeDumper:
    """ Cube dumper """

    def dump(self, cube: Cube) -> str:
        """ dump cube """
        return json.dumps(cube.__dict__, indent=4)
