""" pygame 7x7 view """
import pygame
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.mover import Mover
from pyrubikIHM.pg_drawers.pg_draw_7x7 import PGDrawer7x7
from pyrubikIHM.views.pg_view import PGView

class Pygame7x7View(PGView):
    """ pygame 7x7 view """

    def __init__(self, title):
        super().__init__(title)
        self.pg_drawer = PGDrawer7x7()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(7)
        self.mover = Mover()

    def _render(self):
        self.pg_drawer.draw(self.screen, self.cube)
        
    def _handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_k:
                    self.cube = self.mover.simple_move(self.cube, "U")
                case pygame.K_m:
                    self.cube = self.mover.simple_move(self.cube, "U'")
                case pygame.K_o:
                    self.cube = self.mover.simple_move(self.cube, "R")
                case pygame.K_l:
                    self.cube = self.mover.simple_move(self.cube, "R'")
