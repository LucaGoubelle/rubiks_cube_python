from typing import List


class ColorDetector:
    """ color detector """

    def detect_on_face(self, face: List[List[str]], color: str) -> List[List[int]]:
        """ detect color on face """
        size: int = len(face)
        result: List[List[int]] = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                result[i][j] = 1 if result[i][j] == color else 0
        return result

    def detect_color_on_edge(self, edge: str, colors: List[str]) -> bool:
        """ detect color on edge """
        results: List[str] = edge.split('_')
        cond1: bool = colors[0] in results
        cond2: bool = colors[1] in results
        return cond1 and cond2
    
    def detect_color_on_corner(self, corner: str, colors: List[str]) -> bool:
        """ detect color on edge """
        results: List[str] = corner.split('_')
        cond1: bool = colors[0] in results
        cond2: bool = colors[1] in results
        cond3: bool = colors[2] in results
        return cond1 and cond2 and cond3
