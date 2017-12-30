 # day25
import sys

class Puzzle():
    
    def __init__(self, test_flag=False):
        self.tape = {}
        self.cursor = 0
        self.state = 'A'
        self.rules = {'A': {0: (1, 1, 'B'), 1: (0, -1, 'F')},
                      'B': {0: (0, 1, 'C'), 1: (0, 1, 'D')},
                      'C': {0: (1, -1, 'D'), 1: (1, 1, 'E')},
                      'D': {0: (0, -1, 'E'), 1: (0, -1, 'D')},
                      'E': {0: (0, 1, 'A'), 1: (1, 1, 'C')},
                      'F': {0: (1, -1, 'A'), 1: (1, 1, 'A')}}
                            
    def solve_part1(self, steps=12994925):
        """part 1"""
        for _ in range(steps):
            self.next_step()
        return sum(self.tape.values())

    @property
    def current_value(self):
        """value at tape cursor location"""
        return self.tape.get(self.cursor, 0)
        
    def next_step(self):
        """applies rules based on current state and updates accordingly"""
        rule = self.rules[self.state][self.current_value]
        self.change_value(rule[0])
        self.move_cursor(rule[1])
        self.change_state(rule[2])

    def change_value(self, x):
        """change current value of tape in cursor position"""
        self.tape[self.cursor] = x

    def move_cursor(self, x):
        """move cursor either left or right"""
        self.cursor += x

    def change_state(self, x):
        """change state for next step"""
        self.state = x



    def solve_part2(self):
        """part 2"""
        pass
                 
        
if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    puzzle = Puzzle(test_flag)
    part1 = puzzle.solve_part1()
    print("part1:", part1)
    part2 = puzzle.solve_part2()
    print("part2:", part2)
    

    if test_flag:
        print("testing complete successfully")
        

    
    