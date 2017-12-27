 # day24
import sys

class Puzzle():
    
    def __init__(self, test_flag=False):
        if test_flag:
            self.components = self.load_into_memory("test.txt")
        else:
            self.components = self.load_into_memory("input.txt")
        self.chains = []
        
    def load_into_memory(self, filename):
        """load input into memory"""
        lst = []
        with open(filename) as f:
            for line in f:
                lst.append(tuple(map(int, line.strip('\n').split('/'))))
        return lst
                    
    def solve_part1(self):
        """part 1"""
        self.chain(pins=0, components=self.components)
        dct = {}
        for bridge in self.chains:
            dct[sum([a + b for a, b in bridge])] = bridge
        return max(dct.items())

    def chain(self, pins, components, used=[]):
        """iterates through different chains"""
        for i, component in enumerate(components):
            if pins in component:
                a, b = component
                new_pins = a if a != pins else b
                remaining = components.copy()
                del remaining[i]
                complete_chain = self.chain(new_pins, remaining, used + [component])
                self.chains.append(complete_chain)
        return used   

    def solve_part2(self):
        """part 2"""
        dct = {}
        max_length = max([len(bridge) for bridge in self.chains])
        for bridge in self.chains:
            if len(bridge) == max_length:
                dct[sum([a + b for a, b in bridge])] = bridge            
        return max(dct.items())
                 
        
if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    puzzle = Puzzle(test_flag)
    part1 = puzzle.solve_part1()
    print("part1:", part1)
    part2 = puzzle.solve_part2()
    print("part2:", part2)
    

    if test_flag:
        assert part1[0] == 31
        assert part2[0] == 19
        print("testing complete successfully")
        

    
    