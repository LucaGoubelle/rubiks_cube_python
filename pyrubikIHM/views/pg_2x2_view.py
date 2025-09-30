import pygame
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.mover import Mover
from pyrubikIHM.pg_drawers.pg_draw_2x2 import PGDrawer2x2
from pyrubikIHM.views.pg_view import PGView


class Pygame2x2View(PGView):
    """ pygame 2x2 view """
    
    def __init__(self, title):
        super().__init__(title)
        self.pg_draw_2x2 = PGDrawer2x2()
        cube_builder = CubeBuilder()
        self.cube = cube_builder.build(2)
        self.mover = Mover()
        
    def _render(self):
        self.pg_draw_2x2.draw(self.screen, self.cube)
        
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
