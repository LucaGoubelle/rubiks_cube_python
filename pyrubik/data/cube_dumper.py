""" cube dumper """
import json
import xmltodict
from pyrubik.data.cube import Cube

class CubeDumper:
    """ Cube dumper """

    def dump(self, cube: Cube) -> str:
        """ dump cube """
        return json.dumps(cube.__dict__, indent=4)

    def dump_to_xml(self, cube: Cube) -> str:
        """ dump cube to xml string """
        return xmltodict.unparse({"cube": cube.__dict__}, pretty=True)
