 # day17
import sys

class Puzzle():

    def __init__(self, steps):
        self.steps = steps
        self.spinlock = [0]
   
    def solve_part1(self, repeats):
        """part 1"""
        i = 0
        for n in range(1, repeats + 1):
            i = self.next_index(spinlock_length=n, previous_i=i, steps=self.steps)
            self.insert_number(i, n)
        solution = self.spinlock[self.spinlock.index(2017) + 1]
        return solution
            
    def next_index(self, spinlock_length, previous_i, steps):
        """returns next index for insertion"""
        return (previous_i + steps) % spinlock_length + 1

    def insert_number(self, i, n):
        """inserts next numbers into spinlock"""
        self.spinlock.insert(i, n)
        return
    
        
    def solve_part2(self, repeats):
        """part 2"""
        i = 0
        solution = 0
        for n in range(1, repeats + 1):
            i = self.next_index(spinlock_length=n, previous_i=i, steps=self.steps)
            if i == 1:
                solution = n
                print(solution)
        return solution

if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    if test_flag:
        puzzle = Puzzle(steps=3)
    else:
        puzzle = Puzzle(steps=344)
       
    part1 = puzzle.solve_part1(repeats=2017)
    print("part1:", part1, flush=True)
    part2 = puzzle.solve_part2(repeats=50000000)
    print("part2:", part2)

    if test_flag:
        print("testing complete successfully")
        

    
    