 # day08
import operator as O

 
class Puzzle():
    
    arith = {'inc': O.add, 'dec': O.sub}
    comp = {'==': O.eq, 
            '<': O.lt, 
            '>': O.gt, 
            '!=': O.ne, 
            '>=': O.ge, 
            '<=': O.le}

    def __init__(self, test_flag=False):
        if test_flag:
            self.raw = self.load_into_memory("test.txt")
        else:
            self.raw = self.load_into_memory("input.txt")
        self.vars = {}
        self.instructs = []   
        self.prepare_data() 
        self.values = [] 

    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            return f.readlines()

    def prepare_data(self):
        """separate data from raw input and creates variables"""
        for line in self.raw:
            line = line.strip('\n')
            lst = line.split()
            lst[2] = int(lst[2])
            lst[-1] = int(lst[-1])
            self.vars[lst[0]] = 0
            self.instructs.append(lst)

    def arithmatic(self, instruct):
        """carries out the arithmatic operation"""
        var, op, y = instruct[:3]
        x = self.vars[var]
        return self.arith[op](x, y)

    def comparison(self, instruct):
        """deals with the comparison expressions"""
        var, op, y = instruct[-3:]
        x = self.vars[var]
        return self.comp[op](x, y)

    def solve_instructs(self):
        """incrementally go through instructions and solve"""
        for i in self.instructs:
            if self.comparison(i):
                value = self.arithmatic(i)
                self.vars[i[0]] = value
                self.values.append(value)  # part 2
        return

    def solve_part1(self):
        """Returns largest variable value"""
        self.solve_instructs()
        return max(self.vars.values())

    def solve_part2(self):
        """Returns corrected weights for part 2"""
        return max(self.values)

        
if __name__ == '__main__':
    puzzle = Puzzle(test_flag=False)
    print("part1:", puzzle.solve_part1())
    print("part2:", puzzle.solve_part2())
    