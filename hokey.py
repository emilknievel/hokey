"""
HOKEY
"""

from data.game import Game

if __name__ == '__main__':
    with Game() as game:
        game.main()
