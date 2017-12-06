 # day05

class Puzzle():

    def __init__(self, test_flag=False):
        if test_flag:
            self.jmp_cmds = self.load_into_memory("test.txt")
        else:
            self.jmp_cmds = self.load_into_memory("input.txt")
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            jmp_cmds = [int(l) for l in f.readlines()]
        return jmp_cmds
        
    def solve_part1(self):
        """Returns count for part 1"""
        i = 0
        count = 0
        jmp_cmds = self.jmp_cmds.copy()
        while True:
            try:
                j = i
                i += jmp_cmds[i]
                jmp_cmds[j] += 1
                count += 1
            except IndexError:
                return count
                
    def solve_part2(self):
        """Returns count for part 2"""
        i = 0
        count = 0
        jmp_cmds = self.jmp_cmds.copy()
        while True:
            try:
                j = i
                next_jmp = jmp_cmds[i]
                i += next_jmp
                if next_jmp >= 3:
                    jmp_cmds[j] -= 1
                else: 
                    jmp_cmds[j] += 1
                count += 1
            except IndexError:
                return count

        
if __name__ == '__main__':
    puzzle = Puzzle(test_flag=False)
    print("part1:", puzzle.solve_part1())
    print("part2:", puzzle.solve_part2())