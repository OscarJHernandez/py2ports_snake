"""Run the real entrypoint for a frame without editing the game logic."""
import os
from pathlib import Path
import runpy
import sys
import unittest
from unittest.mock import patch

os.environ.update(SDL_VIDEODRIVER="dummy", SDL_AUDIODRIVER="dummy")
import pygame


class DesktopSmoke(unittest.TestCase):
    def test_entrypoint(self):
        source = Path(__file__).resolve().parents[1] / "src"
        sys.path.insert(0, str(source))
        original = pygame.display.set_mode

        def display(*args, **kwargs):
            screen = original(*args, **kwargs)
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            return screen

        try:
            with patch.object(pygame.display, "set_mode", display):
                runpy.run_path(str(source / "run.py"), run_name="__main__")
        finally:
            sys.path.remove(str(source))
            pygame.quit()


if __name__ == "__main__":
    unittest.main()
