 # day10
from collections import Counter

class Puzzle():

    def __init__(self, test_flag=False):
        if test_flag:
            self.raw = self.load_into_memory("test.txt")
        else:
            self.raw = self.load_into_memory("input.txt")

    def load_into_memory(self, filename):
        """load input into memory string"""
        with open(filename) as f:
            lines = f.readlines()
            return lines
            
    def add_missing_dirs(self, counts):
        """only really relevant for testing"""
        return {d:counts.get(d, 0) 
                for d 
                in ['n', 's', 'nw', 'ne', 'se', 'sw']}
            
    def count_directions(self, dirs):
        """adding or removing from dictionary"""
        counts = self.add_missing_dirs(Counter(dirs))
        return counts
    
    def dir_reduction(self, a, b, c=0):
        """reduce a & b via negation or conversion"""
        overlap = min(a, b)
        a -= overlap
        b -= overlap
        return a, b, c + overlap

    def counts_to_steps(self, n, s, ne, nw, se, sw):
        """converts directions relative to start"""
        sum_dirs = lambda:sum([n, s, ne, nw, se, sw])
        prev_total = 0
        while sum_dirs() != prev_total:
            prev_total = sum_dirs()
            n, s, _ = self.dir_reduction(n, s)          # n + s = 0
            nw, se, _ = self.dir_reduction(nw, se)      # nw + se = 0
            ne, sw, _ = self.dir_reduction(ne, sw)      # ne + sw = 0
            sw, se, s = self.dir_reduction(sw, se, s)   # sw + se = s
            nw, ne, n = self.dir_reduction(nw, ne, n)   # nw + ne = n
            ne, s, se = self.dir_reduction(ne, s, se)   # ne + s = se
            nw, s, sw = self.dir_reduction(nw, s, sw)   # ne + s = sw
            se, n, ne = self.dir_reduction(se, n, ne)   # se + n = ne
            sw, n, nw = self.dir_reduction(sw, n, nw)   # sw + n = nw
        return sum_dirs()

    def solve_part1(self):
        """returns number of steps away from start"""
        for line in self.raw:
            dirs = line.strip('\n').split(',')
            counts = self.count_directions(dirs)
            steps = self.counts_to_steps(**counts)
            print(steps)
        return 
            
    # not great solution, but quickest to solve based on part 1
    def solve_part2(self):
        """return sum of all directions"""
        dirs = self.raw[0].strip('\n').split(',')
        mx = 0
        for i,d in enumerate(dirs):
            counts = self.count_directions(dirs[:i])
            steps = self.counts_to_steps(**counts)
            if steps > mx: 
                mx = steps
        return mx

        
if __name__ == '__main__':
    puzzle = Puzzle(test_flag=False)
    print("part1:", end=' ') 
    puzzle.solve_part1()
    print("part2:", puzzle.solve_part2())
    