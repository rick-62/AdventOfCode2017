 # day06

class Puzzle():

    def __init__(self, test_flag=False):
        if test_flag:
            self.mem_blocks = self.load_into_memory("test.txt")
        else:
            self.mem_blocks = self.load_into_memory("input.txt")
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            mem_blocks = [int(m) for m in f.read().split()]
        return mem_blocks
        
    def solve_part1(self):
        """Returns count for part 1"""
        mem_blocks = self.mem_blocks.copy()
        n = len(mem_blocks)
        prev_dict = {}
        count = 0
        while tuple(mem_blocks) not in prev_dict.keys():
            prev_dict[tuple(mem_blocks)] = 1
            steps = max(mem_blocks)
            start = mem_blocks.index(steps) + 1
            mem_blocks[start - 1] = 0
            for i in range(start, steps + start):
                mem_blocks[i%n] += 1
            count += 1               
        return count
        
                
    def solve_part2(self):
        """Returns count for part 2"""
        mem_blocks = self.mem_blocks.copy()
        n = len(mem_blocks)
        prev_dict = {}
        count = 0
        while tuple(mem_blocks) not in prev_dict.keys():
            prev_dict[tuple(mem_blocks)] = count
            steps = max(mem_blocks)
            start = mem_blocks.index(steps) + 1
            mem_blocks[start - 1] = 0
            for i in range(start, steps + start):
                mem_blocks[i%n] += 1
            count += 1               
        return count - prev_dict[tuple(mem_blocks)]

        
if __name__ == '__main__':
    puzzle = Puzzle(test_flag=False)
    print("part1:", puzzle.solve_part1())
    print("part2:", puzzle.solve_part2())