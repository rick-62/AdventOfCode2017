 # day07
import re
from collections import Counter
from functools import lru_cache
 
class Puzzle():

    def __init__(self, test_flag=False):
        if test_flag:
            self.load_into_memory("test.txt")
        else:
            self.load_into_memory("input.txt")
        self.complete = False
        self.solution = None
        
    def load_into_memory(self, filename):
        """load input into memory (dict)"""
        regex = re.compile(r'([a-z]+)\s\(([0-9]+)\)(\s->\s(.+))?')
        tower, weights = {}, {}
        with open(filename) as f:
            for line in f:
                data = re.search(regex, line)
                weights[data.group(1)] = int(data.group(2))
                if data.group(4) != None:
                    tower[data.group(1)] = data.group(4).split(', ')
        self.tower = tower
        self.weights = weights
        
    def solve_part1(self):
        """Returns top lvl program for part 1"""
        p_lst = []
        for i in self.tower.values():
            p_lst += i
        counter = Counter(p_lst)
        for k in self.tower.keys():
            if k not in counter.keys():
                return(k)
                
    def corrected_weight(self, Ws_dict):
        """Returns corrected weight for the unbalanced program"""
        distinct_weights = Counter(Ws_dict.values())
        unbalanced_weight = min(distinct_weights, key=distinct_weights.get)
        balanced_weight = max(distinct_weights, key=distinct_weights.get)
        weight_diff = balanced_weight - unbalanced_weight
        for k, i in Ws_dict.items():
            if i == unbalanced_weight:
                unbalanced_program = k
                break
        return self.weights[unbalanced_program] + weight_diff

        
    def weight_check(self, program):
        """checks weights for all programs"""
        Wp = self.weights.get(program, 0)
        Ws = 0
        if program in self.tower.keys():
            Ws_dict = {p:self.weight_check(p) for p in self.tower[program]}
            if self.complete: return 
            print(Ws_dict)
            balanced = len(set(Ws_dict.values())) <= 1
            if not balanced:
                self.solution = self.corrected_weight(Ws_dict)
                self.complete = True
                return
            Ws = sum(Ws_dict.values())
        return Wp + Ws

        
    def solve_part2(self):
        """Returns corrected weights for part 2"""
        self.weight_check(self.solve_part1())
        return self.solution
        
if __name__ == '__main__':
    puzzle = Puzzle(test_flag=False)
    print("part1:", puzzle.solve_part1())
    print("part2:", puzzle.solve_part2())