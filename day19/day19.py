 # day19
import sys

class Puzzle():
    directions = {'d':1, 'u':-1, 'r':1, 'l':-1}

    def __init__(self, test_flag=False):
        if test_flag:
            self.map = self.load_into_memory("test.txt")
        else:
            self.map = self.load_into_memory("input.txt")
        self.solution = []
        self.steps = 0

    def load_into_memory(self, filename):
        """load input into memory"""
        with open(filename) as f:
            return f.readlines()  
        
    def solve_part1(self):
        """part 1"""
        i, j = self.find_start()
        direction = 'd'
        end = False
        while not end:
            self.steps += 1
            i, j = self.next_coord(i, j, direction)
            char = self.map[i][j]
            if i < 0 or j < 0 or char == ' ':
                end = True
                continue
            dir_change_flag = self.assess_char(char)
            if dir_change_flag:
                direction = self.next_direction(i, j, direction)
        return ''.join(self.solution)

    def next_direction(self, i, j, current):
        """returns new direction"""
        for direction in ['l', 'r'] if current in ['u', 'd'] else ['u', 'd']:
            ii, jj = self.next_coord(i, j, direction)
            try:
                char = self.map[ii][jj]
            except IndexError:
                char = ' ' 
            if ii == i and char not in ['|', ' ']:
                return direction
            elif jj == j and char not in ['-', ' ']:
                return direction
        return

    def find_start(self):
        """finds beginning from first line"""
        j = self.map[0].index('|')
        return 0, j

    def next_coord(self, i, j, direction):
        """returns next coordinate"""
        if direction in ['d', 'u']:
            i += self.directions[direction]
        elif direction in ['r', 'l']:
            j += self.directions[direction]
        return i, j

    def assess_char(self, char):
        """continue, add char to lst or return direction"""
        if char == '+':
            return True
        elif char not in ['+', '|', '-']:
            self.solution.append(char)
        return False

    def solve_part2(self):
        """part 2"""
        return self.steps

    def __repr__(self):
        """print Puzzle object"""
        return ''.join(self.map)
        
if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    puzzle = Puzzle(test_flag)
    part1 = puzzle.solve_part1()
    print("part1:", part1)
    part2 = puzzle.solve_part2()
    print("part2:", part2)
    
    if test_flag:
        print(puzzle)
        print("testing complete successfully")
        

    
    