""" pygame 4x4 view """
import pygame
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.mover import Mover
from pyrubikIHM.pg_drawers.pg_draw_4x4 import PGDrawer4x4
from pyrubikIHM.views.pg_view import PGView


class Pygame4x4View(PGView):
    """ pygame 4x4 view """
    
    def __init__(self, title):
        super().__init__(title)
        self.pg_drawer = PGDrawer4x4()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(4)
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
