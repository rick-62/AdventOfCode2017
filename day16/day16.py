 # day16
import sys

class Puzzle():

    def __init__(self, test_flag=False):
        if test_flag:
            self.dance = self.load_into_memory("test.txt")
        else:
            self.dance = self.load_into_memory("input.txt")
        self.position = None

    def load_into_memory(self, filename):
        """load input into memory"""
        with open(filename) as f:
            dance = f.read().split(',')
        return self.convert_dance_to_lst(dance)
        
    def convert_dance_to_lst(self, dance):
        """part2: pre-parse input to reduce repeated overhead"""
        for i, move in enumerate(dance):
            move_type = move[0]
            if move_type == 's':
                dance[i] = (move_type, int(move[1:]))
            elif move_type == 'x':
                dance[i] = tuple([move_type] + [int(i) for i in move[1:].split('/')])
            elif move_type == 'p':
                dance[i] = tuple([move_type] + move[1:].split('/'))
            else:
                print("Something went wrong with moves: ", move, "at index ", i)
        return dance
                
        
    def solve_part1(self, start):
        """part 1"""
        self.position = start
        self.perform_dance()
        return ''.join(self.position)
        
    def perform_dance(self):
        """executes dance in order of input list"""
        for move in self.dance:
            move_type = move[0]
            if move_type == 's':
                self.spin(move)
            elif move_type == 'x':
                self.swap_index(move)
            elif move_type == 'p':
                self.swap_programs(move)
            else:
                continue
                
    def spin(self, move):
        """makes programs move from end to front"""
        for spin in range(move[1]):
            end = self.position.pop()
            self.position.insert(0, end)
        return
            
    def swap_index(self, move):
        """swap programs at given indices"""
        self.swap(*move[1:])
        return
                
    def swap_programs(self, move):
        """swaps programs"""
        p1, p2 = move[1:]
        i1 = self.position.index(p1)
        i2 = self.position.index(p2)
        self.swap(i1, i2)
        return
        
    def swap(self, i1, i2):
        """swap programs based on index"""
        self.position[i1], self.position[i2] = self.position[i2], self.position[i1]
        return
             
    def solve_part2(self, start, iterations):
        """part 2"""
        self.position = start
        positions = []
        position = ''.join(self.position)
        repeat_len = 0
        while position not in positions:  # identify repeating dance pattern
            positions.append(position)
            self.perform_dance()
            position = ''.join(self.position)
            repeat_len += 1
        return positions[iterations%repeat_len]
        
        
if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    if test_flag:
        input_order = list('abcde')
    else:
        input_order = list('abcdefghijklmnop')
    puzzle = Puzzle(test_flag)
    part1 = puzzle.solve_part1(input_order.copy())
    part2 = puzzle.solve_part2(input_order.copy(), 1000000000)
    print("part1:", part1)
    print("part2:", part2)
    

    if test_flag:
        assert part1 == 'baedc'
        assert part2 == 'abcde'
        print("testing complete successfully")
        

    
    