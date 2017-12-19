 # day15
import sys
import time

class Puzzle():

    def __init__(self, start_values):
        self.A_start = start_values[0]
        self.B_start = start_values[1]
        self.A_factor = 16807
        self.B_factor = 48271

    def solve_part1(self):
        """part 1"""
        genA = self.genX(self.A_start, self.A_factor)
        genB = self.genX(self.B_start, self.B_factor)
        return self.judge(genA, genB, cycles=40000000)

    def genX(self, start, factor, remainder=2147483647):
        """Provides generator"""
        previous_value = start
        while True:
            value = (previous_value * factor) % remainder
            previous_value = value
            yield bin(value)[-16:].zfill(16)

    def judge(self, genA, genB, cycles=400000):
        """compares the outputs of genA and genB"""
        total = 0
        for i in range(cycles):
            if next(genA) == next(genB):
                total += 1
        return total
   
    def solve_part2(self):
        """part 2"""
        genA = self.genX2(self.A_start, self.A_factor, 4)
        genB = self.genX2(self.B_start, self.B_factor, 8) 
        return self.judge(genA, genB, cycles=5000000)

    def genX2(self, start, factor, mult, remainder=2147483647):
        """Provides generator"""
        previous_value = start
        while True:
            value = (previous_value * factor) % remainder
            previous_value = value
            if value % mult == 0:  # difference between part 1
                yield bin(value)[-16:].zfill(16)


if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    part1_flag = True if 'part1' in sys.argv else False
    part2_flag = True if 'part2' in sys.argv else False
    start_values = (65, 8921) if test_flag else (512, 191)
    puzzle = Puzzle(start_values)
    t0 = time.time()
    if not part2_flag:
        print("part1:", puzzle.solve_part1(), 
              "\ttime taken: {:.3}".format(time.time() - t0))
    t1 = time.time()
    if not part1_flag:
        print("part2:", puzzle.solve_part2(), 
            "\ttime taken: {:.3}".format(time.time() - t1))
    

    