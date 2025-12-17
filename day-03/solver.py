import timeit
import unittest

class FFSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        dp = {}
        for line in input.strip().split("\n"):
            color = tuple(map(int, line.split(',')))
            if color in dp.keys():
                dp[color] += 1
            else:
                dp[color] = 1
        return sorted(dp.items(), key=lambda item: item[1], reverse=True)[0][0]

    def part_two(self, input: str) -> int:
        ans = 0
        for line in input.strip().split("\n"):
            r,g,b = tuple(map(int, line.split(',')))
            if r == g or r == b or g == b:
                continue
            if g > r and g > b:
                ans += 1
        return ans

    def part_three(self, input: str) -> int:
        ans = 0
        for line in input.strip().split("\n"):
            r,g,b = tuple(map(int, line.split(',')))
            if r == g or r == b or g == b:
                ans += 10
            elif r > g and r > b:
                ans += 5
            elif g > r and g > b:
                ans += 2
            else:
                ans += 4
        return ans

class FFSolutionTest(unittest.TestCase):

    def setUp(self):
        from solver import FFSolver
        self.test_part_one = """
10,20,30
20,10,30
30,20,10
10,50,10
50,10,50
10,20,30
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
