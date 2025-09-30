""" pygame 6x6 view """
import pygame
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.mover import Mover
from pyrubikIHM.pg_drawers.pg_draw_6x6 import PGDrawer6x6
from pyrubikIHM.views.pg_view import PGView

class Pygame6x6View(PGView):
    """ pygame 6x6 view """
    
    def __init__(self, title):
        super().__init__(title)
        self.pg_drawer = PGDrawer6x6()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(6)
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