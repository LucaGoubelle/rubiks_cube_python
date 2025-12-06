
from pyrubik.data.cube import Cube, Face


class CentersCaster:
    """ centers caster """

    def __init__(self):
        self.size = 0

    def _get_actual_face(self, cube: Cube, face: str) -> Face:
        match face:
            case "up": return cube.up
            case "front": return cube.front
            case "left": return cube.left
            case "right": return cube.right
            case "down": return cube.down
            case "back": return cube.back
            case _: return cube.front

    def _get_str_centers(self, color_to_filter: str, centers: Face) -> str:
        content: str = ""
        for row in centers:
            for elem in row:
                content += "1" if elem == color_to_filter else "0"
        return content
    
    def cast(self, cube: Cube, face: str, color_to_filter: str) -> str:
        if len(cube.front) != self.size:
            raise Exception(f"Cube must be a {self.size}x{self.size} to use CentersCaster class")
        actual_face: Face = self._get_actual_face(cube, face)
        actual_centers: Face = self._extract_centers(actual_face)
        return self._get_str_centers(color_to_filter, actual_centers)

    def _exctract_centers(self, actual_face: Face) -> Face:
        return []
