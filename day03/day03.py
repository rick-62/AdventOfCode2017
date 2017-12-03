# day03 

import sys
import math
import itertools

class Puzzle():
    
    def __init__(self, number):
        self.number = number
        self.part1 = self.solve_part1()
        self.part2 = self.solve_part2()
        
    def side_length(self, number):
        """returns side length of outer square"""
        squ_root = int(number ** 0.5) + 1
        if squ_root % 2 == 0:
            return squ_root + 1
        else:
            return squ_root
            
    def outer_index(self, side_len, number):
        """returns index around outer square"""
        inner_side_len = side_len - 2
        start_number = (inner_side_len ** 2) + 1
        outer_index = number - start_number + 1
        return outer_index
        
    def side_index(self, index, side_len):
        """returns which side the number is on (ENWS) and index"""
        next_side = itertools.cycle([side_len - 2, side_len])
        for side in ['E', 'N', 'W', 'S']:
            nxt = next(next_side)
            if (index - nxt) <= 0:
                return (side, index)
            index -= nxt

    def directions(self, side_index, side_len):
        """returns directions to one (ENWS)"""
        ENWS, index = side_index
        dist_thru_squs = (side_len - 1) / 2
        EW_centre = (side_len - 1) / 2
        NS_centre = (side_len + 1) / 2
        if ENWS == 'E':
            y = EW_centre - index
            x = -dist_thru_squs
        elif ENWS == 'N':
            x = index - NS_centre
            y = -dist_thru_squs
        elif ENWS == 'W':
            y = index - EW_centre
            x = dist_thru_squs
        elif ENWS == 'S':
            x = NS_centre - index
            y = dist_thru_squs
        else:
            return False
        
        return (x, y)
        
    def solve_part1(self):
        """returns solution to part 1"""
        side_len = self.side_length(self.number)
        outer_index = self.outer_index(side_len, self.number)
        side_index = self.side_index(outer_index, side_len)
        directions = self.directions(side_index, side_len)
        return sum([abs(d) for d in directions])
        
    def adjacent_coords(self, coord):
        """returns all possible adjacent coords"""
        x, y = coord
        X = [x, x + 1, x - 1]
        Y = [y, y + 1, y - 1]
        return itertools.product(X, Y)
        
    def next_coord(self):
        """yield next coord"""
        u,l,d,r = 0, 0, 0, 1  # instructions
        coord = [0, 0]
        while True:
            for i in range(u):
                coord[1] += 1
                yield coord
            for i in range(l):
                coord[0] -= 1
                yield coord
            for i in range(d):
                coord[1] -= 1
                yield coord
            for i in range(r):
                coord[0] += 1
                yield coord
            u,l,d,r = r, l + 2, d + 2, r + 2
    
    def solve_part2(self):
        """returns solution to part 2"""
        model_dict = {(0,0): 1}
        for coord in self.next_coord():
            sum_adjacent = sum(model_dict.get(adj_coord, 0) 
                           for adj_coord 
                           in self.adjacent_coords(coord))
            if sum_adjacent > self.number:
                return sum_adjacent
            model_dict[tuple(coord)] = sum_adjacent
        

if __name__ == '__main__':
    number = int(sys.argv[1])
    puzzle = Puzzle(number)
    print("part1:", puzzle.part1)
    print("part2:", puzzle.part2)
    