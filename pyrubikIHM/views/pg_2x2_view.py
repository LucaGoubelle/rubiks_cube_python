import pygame
from pyrubik.data.cube_builder import CubeBuilder
from pyrubik.moves.mover import Mover
from pyrubik.moves.scrambler import CubeScrambler
from pyrubikIHM.pg_drawers.pg_draw_2x2 import PGDrawer2x2
from pyrubikIHM.views.pg_view import PGView


class Pygame2x2View(PGView):
    """ pygame 2x2 view """
    
    def __init__(self, title):
        super().__init__(title)
        self.pg_draw_2x2 = PGDrawer2x2()
        self.builder = CubeBuilder()
        self.cube = self.builder.build(2)
        self.mover = Mover()
        self.scrambler = CubeScrambler()
        
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
                case pygame.K_d:
                    self.cube = self.mover.simple_move(self.cube, "D")
                case pygame.K_q:
                    self.cube = self.mover.simple_move(self.cube, "D'")
                case pygame.K_s:
                    self.cube = self.mover.simple_move(self.cube, "L")
                case pygame.K_z:
                    self.cube = self.mover.simple_move(self.cube, "L'")
                case pygame.K_j:
                    self.cube = self.mover.simple_move(self.cube, "F")
                case pygame.K_f:
                    self.cube = self.mover.simple_move(self.cube, "F'")
                case pygame.K_LEFT:
                    self.cube = self.mover.simple_move(self.cube, "y")
                case pygame.K_RIGHT:
                    self.cube = self.mover.simple_move(self.cube, "y'")
                case pygame.K_SPACE:
                    self.cube = self.scrambler.scramble(self.cube)
                case pygame.K_ESCAPE:
                    self.cube = self.builder.build(2)
