from test_common import unittest, pygame, Game


class SnakeTests(unittest.TestCase):
    def setUp(self):
        self.game = Game(seed=7)
        self.game.handle("confirm")

    def test_move_and_eat(self):
        self.game.food = (11, 7)
        self.game.step()
        self.assertEqual(self.game.snake[0], (11, 7))
        self.assertEqual(len(self.game.snake), 4)
        self.assertEqual(self.game.score, 10)
        self.assertNotIn(self.game.food, self.game.snake)

    def test_reverse_and_two_turns_in_one_tick_are_rejected(self):
        self.game.handle("left")
        self.assertEqual(self.game.pending, (1, 0))
        self.game.handle("up")
        self.game.handle("left")
        self.game.step()
        self.assertEqual(self.game.snake[0], (10, 6))
        self.game.handle("left")
        self.game.step()
        self.assertEqual(self.game.snake[0], (9, 6))

    def test_wall_and_self_collisions(self):
        self.game.snake = [(19, 0), (18, 0)]
        self.game.step()
        self.assertEqual(self.game.state, "over")
        self.game.reset()
        self.game.snake = [(2, 2), (3, 2), (3, 3), (2, 3), (1, 3)]
        self.game.step()
        self.assertEqual(self.game.state, "over")

    def test_departing_tail_is_not_collision(self):
        self.game.snake = [(2, 2), (2, 3), (3, 3), (3, 2)]
        self.game.food = (0, 0)
        self.game.step()
        self.assertEqual(self.game.state, "playing")
        self.assertEqual(self.game.snake[0], (3, 2))

    def test_speed_and_time_accumulation(self):
        self.game.score = 100
        self.assertEqual(self.game.speed, 9)
        before = list(self.game.snake)
        self.game.update(0.05)
        self.assertEqual(self.game.snake, before)
        self.game.update(0.07)
        self.assertNotEqual(self.game.snake, before)
        self.game.score = 10000
        self.assertEqual(self.game.speed, 16)

    def test_pause_resume_back_and_restart(self):
        before = list(self.game.snake)
        self.game.handle("pause")
        self.game.update(1)
        self.assertEqual(self.game.snake, before)
        self.game.handle("confirm")
        self.assertEqual(self.game.state, "playing")
        self.game.handle("back")
        self.assertEqual(self.game.state, "paused")
        self.game.handle("back")
        self.assertEqual(self.game.state, "menu")
        self.game.score = 80
        self.game.handle("confirm")
        self.assertEqual(self.game.score, 0)
        self.assertEqual(len(self.game.snake), 3)

    def test_fill_board_wins(self):
        self.game.snake = [(0, 0)] + [(x, y) for y in range(15) for x in range(20) if (x, y) not in ((0, 0), (1, 0))]
        self.game.food = (1, 0)
        self.game.step()
        self.assertEqual(self.game.state, "won")
        self.assertEqual(len(self.game.snake), 300)
        self.assertIsNone(self.game.food)

    def test_seeded_food_is_deterministic(self):
        self.assertEqual(Game(seed=7).food, Game(seed=7).food)
