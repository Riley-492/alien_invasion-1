import pygame
import sys

from settings import Settings
class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """initialize the game and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_caption("Alien Invasion")

        #background
        self.bg_color = (230,230,230)
    def run_game(self):
        """start the main loop of the game"""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw screen when you pass through the loop
            self.screen.fill(self.bg_color)
            #make most recently drawn screen visible
            pygame.display.flip()

    if __name__ == '__main__':
        #make game instance, and run game
        ai.run_game()



