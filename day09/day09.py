 # day09
import re

class Puzzle():
    
    def __init__(self, test_flag=False):
        if test_flag:
            self.raw = self.load_into_memory("test.txt")
        else:
            self.raw = self.load_into_memory("input.txt")

    def load_into_memory(self, filename):
        """load input into memory string"""
        with open(filename) as f:
            return f.read()   

    def remove_garbage(self, data_string):
        """remove all garbage, correctly 
        resolving parenthesis balancing and exclamation marks"""
        removed_ex_marks = re.sub(r'!.', '', data_string)
        return re.sub(r'<.*?>(?![^<]*>)', '', removed_ex_marks)

    def collect_garbage(self, data_string):
        """resolve exclamation marks and return garbage contents"""
        removed_ex_marks = re.sub(r'!.', '', data_string)
        return re.findall(r'<(.*?)>(?![^<]*>)', removed_ex_marks)
        
    def solve_part1(self):
        """Returns score"""
        braces = self.remove_garbage(self.raw)
        score, nest = 0, 1
        for brace in braces:
            if brace == '{':
                score += nest
                nest += 1
            elif brace == '}':
                nest -= 1
        return score

    def solve_part2(self):
        """Returns total removed garbage"""
        garbage =  self.collect_garbage(self.raw)
        return len(''.join(garbage))
        
if __name__ == '__main__':
    puzzle = Puzzle(test_flag=False)
    print("part1:", puzzle.solve_part1())
    print("part2:", puzzle.solve_part2())
    