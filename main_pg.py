""" entry point for pygame """
from pyrubikIHM.views.pg_2x2_view import Pygame2x2View
from pyrubikIHM.views.pg_3x3_view import Pygame3x3View
from pyrubikIHM.views.pg_4x4_view import Pygame4x4View
from pyrubikIHM.views.pg_5x5_view import Pygame5x5View
from pyrubikIHM.views.pg_6x6_view import Pygame6x6View
from pyrubikIHM.views.pg_7x7_view import Pygame7x7View

size: int = 5

match size:
    case 2:
        pg_view = Pygame2x2View("2x2")
    case 3:
        pg_view = Pygame3x3View("3x3")
    case 4:
        pg_view = Pygame4x4View("4x4")
    case 5:
        pg_view = Pygame5x5View("5x5")
    case 6:
        pg_view = Pygame6x6View("6x6")
    case 7:
        pg_view = Pygame7x7View("7x7")
    case _:
        pg_view = Pygame3x3View("3x3")
        
pg_view.run()
