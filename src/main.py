"""Snake gameplay, developed from the public py2port_pygame_template."""
import random

import pygame
from app import PANEL, run


class Game:
    title = "py2ports Snake"
    subtitle = "Eat. Grow. Beat your best."
    hint = "D-pad / stick / WASD: turn     Start / P: pause"
    accent = (92, 231, 164)
    columns, rows = 20, 15
    directions = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}

    def __init__(self, seed=None):
        self.random = random.Random(seed)
        self.reset()
        self.state = "menu"

    def reset(self):
        self.snake = [(10, 7), (9, 7), (8, 7)]
        self.direction = self.pending = (1, 0)
        self.turned = False
        self.score, self.elapsed = 0, 0.0
        self.state = "playing"
        self.place_food()

    @property
    def speed(self):
        return min(16, 7 + self.score // 50)

    def place_food(self):
        free = [(x, y) for y in range(self.rows) for x in range(self.columns) if (x, y) not in self.snake]
        self.food = self.random.choice(free) if free else None
        if not free:
            self.state = "won"

    def handle(self, action):
        if action == "confirm":
            if self.state == "paused":
                self.state = "playing"
            elif self.state in ("menu", "over", "won"):
                self.reset()
        elif action == "pause" and self.state in ("playing", "paused"):
            self.state = "paused" if self.state == "playing" else "playing"
        elif action == "back":
            self.state = "paused" if self.state == "playing" else "menu"
        elif action in self.directions and self.state == "playing" and not self.turned:
            direction = self.directions[action]
            if direction != self.direction and direction != (-self.direction[0], -self.direction[1]):
                self.pending = direction
                self.turned = True

    def step(self):
        if self.state != "playing":
            return
        self.direction, self.turned = self.pending, False
        x, y = self.snake[0]
        head = (x + self.direction[0], y + self.direction[1])
        growing = head == self.food
        body = self.snake if growing else self.snake[:-1]
        if not (0 <= head[0] < self.columns and 0 <= head[1] < self.rows) or head in body:
            self.state = "over"
            return
        self.snake.insert(0, head)
        if growing:
            self.score += 10
            self.place_food()
        else:
            self.snake.pop()

    def update(self, dt, horizontal=0):
        if self.state != "playing":
            return
        self.elapsed += min(dt, 0.25)
        while self.elapsed >= 1 / self.speed and self.state == "playing":
            self.elapsed -= 1 / self.speed
            self.step()

    def draw(self, view):
        surface = view.surface
        pygame.draw.rect(surface, PANEL, (76, 96, 488, 364), border_radius=8)
        for y in range(self.rows):
            for x in range(self.columns):
                pygame.draw.rect(surface, (28, 43, 57) if (x+y) % 2 else (25, 39, 52), (80+x*24, 98+y*24, 23, 23))
        if self.food:
            x, y = self.food
            pygame.draw.circle(surface, (255, 122, 112), (92+x*24, 110+y*24), 8)
            pygame.draw.circle(surface, (255, 205, 165), (90+x*24, 107+y*24), 3)
        for index, (x, y) in enumerate(self.snake):
            pygame.draw.rect(surface, self.accent if index == 0 else (49, 158, 123), (82+x*24, 100+y*24, 20, 20), border_radius=5)
        x, y = self.snake[0]
        dx, dy = self.direction
        for offset in (-4, 4):
            pygame.draw.circle(surface, (12, 32, 35), (92+x*24+dx*5+(offset if dy else 0), 110+y*24+dy*5+(offset if dx else 0)), 2)


def main():
    run(Game, "py2ports_snake", "SNAKE_FULLSCREEN")


if __name__ == "__main__":
    main()
