import timeit
import unittest

class FFSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        s = 0
        for line in input.split("\n"):
            s += len(line.strip())//2
        return s


    def part_two(self, input: str) -> int:
        s = 0
        for line in input.split("\n"):
            t = len(line.strip())//2
            if t&1 == 0:
                s += t
        return s

    def part_three(self, input: str) -> int:
        s = 0
        for line in input.split("\n"):
            if "ne" in line:
                continue
            s += len(line.strip())//2
        return s

class FFSolutionTest(unittest.TestCase):

    def setUp(self):
        from solve import FFSolver
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
