# app.py

from collections import deque

class RobotGrid:
    """
    RobotGrid simulates a robot navigating a bounded 2D grid from -9999 to +9999 in both axes.
    The robot can only move to "safe" squares, where the sum of the digits
    of the product of the coordinates is less than 19.
    """

    MIN_COORD = -9999
    MAX_COORD = 9999

    @staticmethod
    def is_safe(x: int, y: int) -> bool:
        """
        Check if the coordinate (x, y) is safe.
        A square is safe if the sum of digits of |x * y| is less than 19.
        """
        product = x * y
        digit_sum = sum(int(ch) for ch in str(abs(product)))
        return digit_sum < 19

    def total_safe_squares(self) -> int:
        """
        Calculate the total number of safe squares reachable from (0, 0),
        moving only up/down/left/right, within the bounds.
        """
        start = (0, 0)
        if not self.is_safe(*start):
            return 0

        visited = set([start])
        queue = deque([start])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited \
                   and self.MIN_COORD <= nx <= self.MAX_COORD \
                   and self.MIN_COORD <= ny <= self.MAX_COORD \
                   and self.is_safe(nx, ny):
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return len(visited)

    def shortest_safe_journey(self, a: int, b: int, x: int, y: int) -> int:
        """
        Find the length of the shortest path from (a, b) to (x, y) over safe squares.
        Returns -1 if no safe path exists.
        """
        start = (a, b)
        target = (x, y)

        # both endpoints must be safe
        if not (self.is_safe(*start) and self.is_safe(*target)):
            return -1

        visited = set([start])
        queue = deque([(a, b, 0)])  # (x, y, distance)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            cx, cy, dist = queue.popleft()
            if (cx, cy) == target:
                return dist

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in visited \
                   and self.MIN_COORD <= nx <= self.MAX_COORD \
                   and self.MIN_COORD <= ny <= self.MAX_COORD \
                   and self.is_safe(nx, ny):
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

        return -1


if __name__ == "__main__":
    grid = RobotGrid()


