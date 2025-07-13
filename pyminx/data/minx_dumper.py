import json

from pyminx.data.models.minx import Minx

class MinxDumper:
    """ minx dumper """
    
    def dump(self, minx: Minx) -> str:
        """
        dump the minx object to JSON string
        """
        return json.dumps(minx)
