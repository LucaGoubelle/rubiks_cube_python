from typing import List

from pyrubik.display.ansi_colors import HMAP_COLOR
from pyrubik.data.cube import Cube
from pyrubik.exceptions.cube_printer_exception import CubePrinterException

Row = List[str]

class CubePrinter:
    """ 
    print a cube on console 
    @author: LucaGoubelle
    """

    def print_cube(self, cube: Cube) -> None:
        """
        print a cube object on the console
        raise a CubePrinterException if wrong parametters
        @author: LucaGoubelle
        """
        try:
            content: str = ""
            for row in cube.up:
                content += self._print_up_down(row)
            for i in range(len(cube.front)):
                content += self._print_lfrb(cube.left[i], cube.front[i], cube.right[i], cube.back[i])
            for row in cube.down:
                content += self._print_up_down(row)
            print(content)
            del content
        except Exception as exc:
            raise CubePrinterException() from exc

    def _print_up_down(self, row: Row) -> str:
        content: str = ""
        for _ in row:
            content += " "
        for elem in row:
            content += HMAP_COLOR[elem]
        content += "\n"
        return content

    def _print_lfrb(self, 
        row_l: Row, 
        row_f: Row, 
        row_r: Row, 
        row_b: Row
    ) -> str:
        content: str = ""
        for elem in row_l:
            content += HMAP_COLOR[elem]
        for elem in row_f:
            content += HMAP_COLOR[elem]
        for elem in row_r:
            content += HMAP_COLOR[elem]
        for elem in row_b:
            content += HMAP_COLOR[elem]
        content += "\n"
        return content
