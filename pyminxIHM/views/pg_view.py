
import sys
import pygame


class PGView:
    """ pygame view """
    
    def __init__(self, title: str):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200,780))
        pygame.display.set_caption(title)
        self.bgcolor = (32,32,32)
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self._handle_events(event)
            
            self.screen.fill(self.bgcolor)
            self._render()
            pygame.display.update()
            self.clock.tick(60)

    def _render(self):
        pass

    def _handle_events(self, event):
        pass
