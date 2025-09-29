""" cubestr dumper """
from pyrubik.data.cube import Cube

class CubestrDumper:
    """
    dump cube to string letters color format
    
    @author: LucaGoubelle
    """
    
    def __init__(self):
        self.hmap = {
            "green": "G",
            "blue": "B",
            "red": "R",
            "orange": "O",
            "yellow": "Y",
            "white": "W"
        }
        
    def _encode_face(self, face):
        """
        encode face with char dict in self
        @author: LucaGoubelle
        """
        content: str = ""
        for row in face:
            for elem in row:
                content += self.hmap[elem] if elem in self.hmap else "?"
        return content
        
    def dump(self, cube: Cube) -> str:
        """
        dump cube to string letters color format
        
        example:
        
        WBOOGBOWG_ //back face
        GRGRYRYGG_ //up face
        BOWWBGBRR_ //front face
        YYOYOBRBW_ //left face
        OWRYRYBGW_ //right face
        YWBGWOROY //down face
        
        @author: LucaGoubelle
        """
        content: str = ""
        content += self._encode_face(cube.back) + "_"
        content += self._encode_face(cube.up) + "_"
        content += self._encode_face(cube.front) + "_"
        content += self._encode_face(cube.left) + "_"
        content += self._encode_face(cube.right) + "_"
        content += self._encode_face(cube.down)
        return ""
