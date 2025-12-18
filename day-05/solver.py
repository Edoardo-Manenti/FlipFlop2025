import timeit
import unittest
from collections import defaultdict

class FFSolver():

    def setup(self, input_file_path = 'input.txt') -> str:
        return open("input.txt", "r").read()

    def part_one(self, input: str) -> int:
        tunnels = list(input.strip())
        dp = defaultdict(list)
        for i,v in enumerate(tunnels):
            dp[v].append(i)

        curr = 0
        ans = 0
        while curr <= len(tunnels)-1:
            ans += abs(dp[tunnels[curr]][0] - dp[tunnels[curr]][1])
            if dp[tunnels[curr]][0] == curr:
                curr = dp[tunnels[curr]][1]+1
            else:
                curr = dp[tunnels[curr]][0]+1
        return ans

    def part_two(self, input: str) -> int:
        seen = set()
        tunnels = list(input.strip())
        dp = defaultdict(list)
        for i,v in enumerate(tunnels):
            dp[v].append(i)
        curr = 0
        ans = 0
        while curr <= len(tunnels)-1:
            seen.add(tunnels[curr])
            ans += abs(dp[tunnels[curr]][0] - dp[tunnels[curr]][1])
            if dp[tunnels[curr]][0] == curr:
                curr = dp[tunnels[curr]][1]+1
            else:
                curr = dp[tunnels[curr]][0]+1
        ans = []
        for k in dp.keys():
            if k not in seen:
                ans.append(k)

        return "".join(ans)

    def part_three(self, input: str) -> int:
        tunnels = list(input.strip())
        dp = defaultdict(list)
        for i,v in enumerate(tunnels):
            dp[v].append(i)

        curr = 0
        ans = 0
        while curr <= len(tunnels)-1:
            if tunnels[curr].isupper():
                ans -= abs(dp[tunnels[curr]][0] - dp[tunnels[curr]][1])
            else:
                ans += abs(dp[tunnels[curr]][0] - dp[tunnels[curr]][1])

            if dp[tunnels[curr]][0] == curr:
                curr = dp[tunnels[curr]][1]+1
            else:
                curr = dp[tunnels[curr]][0]+1
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
