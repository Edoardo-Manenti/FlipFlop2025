import timeit
import unittest
from collections import defaultdict

class FFSolver():
    dp = {1:1}

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def fact(self, n):
        if n in self.dp.keys():
            return self.dp[n]
        fact_n = n*self.fact(n-1)
        self.dp[n] = fact_n
        return fact_n

    def part_one(self, input: str) -> int:
        ans = 0
        for line in input.splitlines():
            r,c = tuple(map(int, line.split()))
            ans += self.fact(r+c-2)/(self.fact(r-1)*self.fact(c-1))
        return ans

    def part_two(self, input: str) -> int:
        ans = 0
        for line in input.splitlines():
            r,c = tuple(map(int, line.split()))
            ans += self.fact(2*r+c-3)/(self.fact(r-1)*self.fact(r-1)*self.fact(c-1))
        return int(ans)

    def part_three(self, input: str) -> int:
        ans = 0
        for line in input.splitlines():
            na,ad = tuple(map(int, line.split()))
            ans += self.fact((ad-1)*na)//(self.fact(ad-1)**na)
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

        self.test_part_three = """2 2
3 3
2 3
4 3
"""
        self.solution_part_three = 2520+90+2+6

        self.solver = FFSolver()

    def test_part_one(self):
        value = self.solver.part_one(self.test_part_one)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_one)

    def test_part_two(self):
        value = self.solver.part_two(self.test_part_two)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_two)

    def test_part_three(self):
        value = self.solver.part_three(self.test_part_three)

        self.assertIsNotNone(value)
        self.assertEqual(value, self.solution_part_three)

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
