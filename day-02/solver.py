import timeit
import unittest

class FFSolver():
    dp = {}

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        sp = 0
        ans = -1
        for char in list(input.strip()):
            if char == '^':
                sp += 1
            else:
                sp -= 1
            ans = max(sp, ans)
        return ans

    def part_two(self, input: str) -> int:
        sp = 0
        counter = 0
        ans = -1
        for char in list(input.strip()):
            if char == '^':
                if counter > 0:
                    counter += 1
                else:
                    counter = 1
            else:
                if counter < 0:
                    counter -= 1
                else:
                    counter = -1
            sp += counter
            ans = max(sp, ans)
        return ans

    def part_three(self, input: str) -> int:
        sp = 0
        last_seen = ""
        counter = 1
        ans = -1
        for char in list(input.strip()):
            if char == last_seen:
                counter += 1
            else:
                counter = 1
            change = self.fib(counter) - self.fib(counter-1)
            if char == 'v':
                change *= -1
            sp += change
            ans = max(sp, ans)
            last_seen = char
        return ans

    def fib(self, i):
        if i in self.dp.keys():
            return self.dp[i]
        if i == 0:
            self.dp[i] = 0
            return 0
        if i == 1:
            self.dp[i] = 1
            return 1
        res = self.fib(i-2) + self.fib(i-1)
        self.dp[i] = res
        return res

class FFSolutionTest(unittest.TestCase):

    def setUp(self):
        from solver import FFSolver
        self.test_part_one = """
        """
        self.solution_part_one = 3

        self.test_part_three = "^^^^^^^^^^^^vvvvvvvvv^"
        self.solution_part_three = 144

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
