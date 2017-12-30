 # day22
import sys

class Puzzle():
    
    def __init__(self, test_flag=False):
        if test_flag:
            self.nodes = self.load_into_memory("test.txt")
        else:
            self.nodes = self.load_into_memory("input.txt")
        self.infect_count = 0
        self.direction = 'N'
        self.current_node = self.start_coord()
        
    def load_into_memory(self, filename):
        """load input into memory"""
        dct = {}
        with open(filename) as f:
            all_lines = f.readlines()
            for y, line in enumerate(all_lines[::-1]):
                for x, node in enumerate(line.strip('\n')):
                    dct[(x, y)] = node
        return dct
                    
    def solve_part1(self, n=10000):
        """part 1"""
        for _ in range(n):
            self.next_direction()
            self.update_current_node()
            self.move_carrier()
        return self.infect_count

    def start_coord(self):
        """return start coordinate"""
        centre = int((len(self.nodes.keys()) ** 0.5) // 2)
        return (centre, centre)

    @property
    def node_status(self):
        """retrieve value from self.nodes else clean"""
        return self.nodes.get(self.current_node, '.')

    def next_direction(self):
        """based on current position which direction next"""
        compass = ['N', 'E', 'S', 'W']
        i_compass = compass.index(self.direction)
        if self.node_status == '.':  # turn left
            new_direction = compass[i_compass - 1]
        elif self.node_status == '#':  # turn right
            new_direction = compass[(i_compass + 1) % 4]
        elif self.node_status == 'W':  # no turn
            new_direction = self.direction
        elif self.node_status == 'F':  # reverse
            new_direction = compass[(i_compass + 2) % 4]
        else:
            print("error: check current node")
        self.direction = new_direction

    def update_current_node(self):
        """change current node infection"""
        if self.node_status == '.':
            new_status = '#'
            self.infect_count += 1
        else:
            new_status = '.'
        self.nodes[self.current_node] = new_status

    def move_carrier(self):
        """virus carrier moves forwards one node"""
        compass = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        zipped = zip(compass[self.direction], self.current_node)
        self.current_node = tuple([sum(x) for x in zipped])

    def solve_part2(self, n=10000000):
        """part 2"""
        for _ in range(n):
            self.next_direction()
            self.update_current_node_2()
            self.move_carrier()
        return self.infect_count

    def update_current_node_2(self):
        """change current node infection - part 2"""
        if self.node_status == '.':
            new_status = 'W'
        elif self.node_status == 'W':
            new_status = '#'
            self.infect_count += 1
        elif self.node_status == '#':
            new_status = 'F'
        elif self.node_status == 'F':
            new_status = '.'
        else:
            print("error: current node not identified")
        self.nodes[self.current_node] = new_status

if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    puzzle = Puzzle(test_flag)
    part1 = puzzle.solve_part1()
    print("part1:", part1)
    puzzle_2 = Puzzle(test_flag)
    part2 = puzzle_2.solve_part2()
    print("part2:", part2)
    

    if test_flag:
        print("testing complete successfully")
        

    
    