import json
import xmltodict

from pyminx.data.models.minx import Minx

class MinxDumper:
    """ minx dumper """
    
    def dump(self, minx: Minx) -> str:
        """
        dump the minx object to JSON string
        """
        return json.dumps(minx.__dict__)

    def dump_to_xml(self, minx: Minx) -> str:
        """
        dump the minx object to XML string
        """
        return xmltodict.unparse({"minx": minx.__dict__}, pretty=True)
