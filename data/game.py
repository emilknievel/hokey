"""
Main game handler
"""
import sys
import pygame as pyg
from loggingtool import log


class Game:
    def __init__(self):
        """
        Initialize game resources
        """
        self.running = True
        pyg.init()
        self.clock = pyg.time.Clock()
        size = [400, 300]
        self.screen = pyg.display.set_mode(size)
        pyg.display.set_caption('HOKEY')

    def __enter__(self):
        log.debug('Entering game')

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Exiting game')
        pyg.quit()
        sys.exit()

    def main(self):
        while self.running:
            self.clock.tick(10)
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.running = False
            self.update()

    def update(self):
        print('hello')
        # TODO: check state
        # TODO: update graphics
