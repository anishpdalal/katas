import unittest

from langton.AntGrid import AntGrid
from langton.Square import Square


class TestAnt(unittest.TestCase):

    def test_ant_grid_starts_at_0_x_coordinate(self):
        ant = AntGrid()
        self.assertEqual(0, ant.x)

    def test_ant_grid_starts_at_0_y_coordinate(self):
        ant = AntGrid()
        self.assertEqual(0, ant.y)

    def test_ant_grid_starts_with_up_direction(self):
        ant = AntGrid()
        self.assertEqual("up", ant.dir)

    def test_ant_grid_has_grid_set(self):
        ant = AntGrid()
        self.assertIsInstance(ant.grid_list, list)

    def test_ant_grid_contains_0_0_square(self):
        ant = AntGrid()
        self.assertIn(Square(x=0, y=0), ant.grid_list)

    # turning tests
    def test_ant_grid_turn_right_dir_up_to_right(self):
        ant = AntGrid()
        ant.dir = "up"
        ant.turn_right()
        self.assertEqual("right", ant.dir)

    def test_ant_grid_turn_right_dir_right_to_down(self):
        ant = AntGrid()
        ant.dir = "right"
        ant.turn_right()
        self.assertEqual("down", ant.dir)

    def test_ant_grid_turn_right_dir_down_to_left(self):
        ant = AntGrid()
        ant.dir = "down"
        ant.turn_right()
        self.assertEqual("left", ant.dir)

    def test_ant_grid_turn_right_dir_right_to_left(self):
        ant = AntGrid()
        ant.dir = "left"
        ant.turn_right()
        self.assertEqual("up", ant.dir)
