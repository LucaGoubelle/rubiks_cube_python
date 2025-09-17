""" cube pygame drawer """

class CubePGDrawer:
    """ cube pygame drawer """

    def draw(self, screen, cube) -> None:
        self._draw_front_face(screen, cube)
        self._draw_right_face(screen, cube)
        self._draw_up_face(screen, cube)
