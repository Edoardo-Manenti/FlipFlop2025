import timeit
import unittest

class FFSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        x,y = 0, 0
        ans = 0
        for line in input.splitlines():
            tx, ty = tuple(map(int, line.split(',')))
            ans += abs(tx-x) + abs(ty-y)
            x,y = tx, ty
        return ans

    def part_two(self, input: str) -> int:
        x,y = 0, 0
        ans = 0
        for line in input.splitlines():
            tx, ty = tuple(map(int, line.split(',')))
            ans += max(abs(tx-x), abs(ty-y))
            x,y = tx, ty
        return ans

    def part_three(self, input: str) -> int:
        trashes = [tuple(map(int, line.split(','))) for line in input.splitlines()]
        x,y = 0, 0
        ans = 0
        trashes.sort(key=lambda item : item[0]+item[1])
        for tx,ty in trashes:
            ans += max(abs(tx-x), abs(ty-y))
            x,y = tx, ty
        return ans

class FFSolutionTest(unittest.TestCase):

    def setUp(self):
        from solver import FFSolver
        self.test_part_one = """
        """
        self.solution_part_one = 3

        self.test_part_two = """
        """
        self.solution_part_two = 8

        self.solver = FFSolver()

    def test_part_one(self):
        value = self.solver.part_one(self.test_part_one)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_one)

    def test_part_two(self):
        value = self.solver.part_two(self.test_part_two)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_two)

if __name__ == '__main__':
    setup = '''
from solver import FFSolver
solver = FFSolver()
problem = solver.setup()
    '''
    print(f"Time for part1: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_one(problem))', 
                  number = 1)
    } sec")
    print(f"Time for part2: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_two(problem))', 
                  number = 1)
    } sec")
    print(f"Time for part3: {
    timeit.timeit(setup=setup, 
                  stmt='print(solver.part_three(problem))', 
                  number = 1)
    } sec")
