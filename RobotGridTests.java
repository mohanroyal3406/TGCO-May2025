# test.py

import unittest
from app import RobotGrid

class RobotGridTests(unittest.TestCase):

    def test_is_safe(self):
        # known safe
        self.assertTrue(RobotGrid.is_safe(3, 4))        # 3*4=12 → 1+2=3
        self.assertTrue(RobotGrid.is_safe(6, 9))        # 6*9=54 → 5+4=9
        self.assertTrue(RobotGrid.is_safe(96, -69))     # 96*69=6624 → 6+6+2+4=18
        # known unsafe
        self.assertFalse(RobotGrid.is_safe(67, 43))     # 67*43=2881 → 2+8+8+1=19
        self.assertFalse(RobotGrid.is_safe(123, 456))   # 123*456=56088 → 5+6+0+8+8=27

    def test_total_safe_squares_small_bounds(self):
        # shrink bounds to a 5×5 region for predictable count
        orig_min, orig_max = RobotGrid.MIN_COORD, RobotGrid.MAX_COORD
        RobotGrid.MIN_COORD, RobotGrid.MAX_COORD = -2, 2

        grid = RobotGrid()
        expected = sum(
            1
            for x in range(-2, 3)
            for y in range(-2, 3)
            if grid.is_safe(x, y)
        )
        self.assertEqual(grid.total_safe_squares(), expected)

        # restore original bounds
        RobotGrid.MIN_COORD, RobotGrid.MAX_COORD = orig_min, orig_max

    def test_shortest_safe_journey(self):
        grid = RobotGrid()

        # reachable, Manhattan distance = 3+4 = 7
        self.assertEqual(grid.shortest_safe_journey(0, 0, 3, 4), 7)

        # destination unsafe → -1
        self.assertEqual(grid.shortest_safe_journey(0, 0, 67, 43), -1)

        # adjacent move
        self.assertEqual(grid.shortest_safe_journey(1, 1, 1, 2), 1)

        # same start/end
        self.assertEqual(grid.shortest_safe_journey(5, 5, 5, 5), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
