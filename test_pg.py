""" test pygame view """
from pyrubik.data.cube_builder import CubeBuilder
from pyrubikIHM.views.pg_2x2_view import Pygame2x2View

cube_builder = CubeBuilder()
cube = cube_builder.build(2)

pg_view = Pygame2x2View("test01")
pg_view.run()
