""" pygame 5x5 view """
import pygame
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.mover import Mover
from pyrubikIHM.pg_drawers.pg_draw_5x5 import PGDrawer5x5
from pyrubikIHM.views.pg_view import PGView

class Pygame5x5View(PGView):
    """ pygame 5x5 view """
    
    def __init__(self, title):
        super().__init__(title)
        self.pg_drawer = PGDrawer5x5()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(5)
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
