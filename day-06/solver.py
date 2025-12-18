import timeit
import unittest
from collections import defaultdict

class FFSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        ans = 0
        for line in input.splitlines():
            a,b = tuple(map(int, line.split(',')))
            fx, fy = ((100*a)%1000, (100*b)%1000)
            if 250<=fx<750 and 250<=fy<750:
                ans += 1
        return ans

    def part_two(self, input: str) -> int:
        ans = 0
        for line in input.splitlines():
            for time in range(3600, 3600*1000, 3600):
                a,b = tuple(map(int, line.split(',')))
                fx, fy = ((time*a)%1000, (time*b)%1000)
                if 250<=fx<750 and 250<=fy<750:
                    ans += 1
        return ans

    def part_three(self, input: str) -> int:
        ans = 0
        for line in input.splitlines():
            for time in range(1000):
                a,b = tuple(map(int, line.split(',')))
                fx = (31556926*(time+1)*a)%1000 
                fy = (31556926*(time+1)*b)%1000
                if 250<=fx<750 and 250<=fy<750:
                    ans += 1
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
