 # day20
import sys
import re
from collections import Counter, defaultdict


class Puzzle():

    def __init__(self, test_flag=False):
        if test_flag:
            self.buffer = self.load_into_memory("test.txt")
        else:
            self.buffer = self.load_into_memory("input.txt")
        self.compiled_re = re.compile(
            'p=<([-\s]?[0-9]+),([-\s]?[0-9]+),([-\s]?[0-9]+)>,\s\
             v=<([-\s]?[0-9]+),([-\s]?[0-9]+),([-\s]?[0-9]+)>,\s\
             a=<([-\s]?[0-9]+),([-\s]?[0-9]+),([-\s]?[0-9]+)>', re.VERBOSE)

    def load_into_memory(self, filename):
        """load input into memory"""
        with open(filename) as f:
            return f.readlines()  
        
    # manhatten distance (not euclidian!!!)
    def solve_part1(self, iterations=1000000):
        """part 1"""
        solution = None
        min_M = False
        A_dct = defaultdict(list)
        for i, particle in enumerate(self.next_particle()):
            A_dct[self.magnitude(particle['a'])].append(i)
            p = self.particle_iterations(particle, iterations)
            M = self.magnitude(p)
            if M < min_M or not min_M:
                min_M = M 
                solution = i
        print(sorted(A_dct.items())[:2])
        return solution

    def solve_part1_alt(self, iterations=1000000):
        """part 1 with manhatten distance"""
        solution = None
        min_M = False
        for i, particle in enumerate(self.next_particle()):
            p1 = self.particle_iterations(particle, 10000)
            p2 = self.particle_iterations(particle, iterations)
            M = self.manhatten(p1, p2)
            if M < min_M or not min_M:
                min_M = M 
                solution = i
        return solution

    def particle_iterations(self, particle, n):
        """returns particle position after number of iterations"""
        P, V, A = particle['p'], particle['v'], particle['a']
        new_p = [p + n * v + (a * n * (n + 1)) / 2 
                 for p, v, a 
                 in zip(P, V, A)]
        return new_p

    def next_particle(self):
        """returns dict of p, v & a from buffer input"""
        for line in self.buffer:
            p_dict = {}
            vals = self.compiled_re.match(line)
            p_dict['p'] = [int(v) for v in vals.group(1, 2, 3)]
            p_dict['v'] = [int(v) for v in vals.group(4, 5, 6)]
            p_dict['a'] = [int(v) for v in vals.group(7, 8, 9)]
            yield p_dict

    def magnitude(self, values):
        """calculate magnitude of given values"""
        M = sum(v**2 for v in values)
        return M**0.5

    def manhatten(self, xyz1, xyz2):
        """calc manhatten distance"""
        zipped = zip(xyz1, xyz2)
        return sum([abs(x1 - x2) for x1,x2 in zipped])

    def solve_part2(self, iterations=500):
        """part 2"""
        particles = {i:particle 
                     for i, particle 
                     in enumerate(self.next_particle())}            
        for n in range(iterations):
            positions = {i: tuple(self.particle_iterations(particle, n)) 
                         for i, particle
                         in particles.items()}
            count = Counter(positions.values())
            for i, p in positions.items():
                if count[p] > 1:
                    del particles[i]
        return len(particles)

        
if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    puzzle = Puzzle(test_flag)
    part1 = puzzle.solve_part1_alt()
    print("part1:", part1)
    part2 = puzzle.solve_part2()
    print("part2:", part2)
    
    if test_flag:
        assert part1 == 0
        print("testing complete successfully")
        

    
    