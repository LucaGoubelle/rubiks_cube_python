from pyrubikIHM.img_drawers.cube_img_drawer import CubeIMGDrawer
from pyrubikIHM.img_drawers.img_draw_2x2 import Cube2x2IMGDrawer
from pyrubikIHM.img_drawers.img_draw_3x3 import Cube3x3IMGDrawer
from pyrubikIHM.img_drawers.img_draw_4x4 import Cube4x4IMGDrawer
from pyrubikIHM.img_drawers.img_draw_5x5 import Cube5x5IMGDrawer
from pyrubikIHM.img_drawers.img_draw_6x6 import Cube6x6IMGDrawer
from pyrubikIHM.img_drawers.img_draw_7x7 import Cube7x7IMGDrawer

class DrawerIMGFactory:
    """ drawer factory """

    def make(self, size: int) -> CubeIMGDrawer:
        match size:
            case 2: return Cube2x2IMGDrawer()
            case 3: return Cube3x3IMGDrawer()
            case 4: return Cube4x4IMGDrawer()
            case 5: return Cube5x5IMGDrawer()
            case 6: return Cube6x6IMGDrawer()
            case 7: return Cube7x7IMGDrawer()
            case _: return Cube3x3IMGDrawer()
