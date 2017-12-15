 # day14
import sys
import knot
import itertools

class Puzzle():

    def __init__(self, test_flag=False):
        if test_flag:
            self.input_hash = self.load_into_memory("test.txt")
        else:
            self.input_hash = self.load_into_memory("input.txt")
        self.square = {}

    def load_into_memory(self, filename):
        """load input into memory"""
        with open(filename) as f:
            return f.read()
          
    def solve_part1(self):
        """part 1"""
        square = self.create_square_as_dict()
        total_used = 0
        for row in square.values():
            total_used += sum(row)
        return total_used

    def create_square_as_dict(self, rows=128):
        """dictionary labeled for each row"""
        square = {}
        for i in range(rows):
            knot_input = self.create_row_input(i)
            hexi = knot.Knot(knot_input).solution
            row = self.convert_hex_to_bin(hexi)
            square[i] = row
        return square

    def create_row_input(self, i):
        """create each row's hash input"""
        key = self.input_hash
        return key + "-" + str(i)

    def convert_hex_to_bin(self, hexi):
        """convert hex output hash to 128 bit equivilent"""
        bin_lst = []
        for c in hexi:
            bin_lst.append(bin(int(c, 16))[2:].zfill(4))
        return [int(b) for b in ''.join(bin_lst)]
            
    def solve_part2(self):
        """part2"""
        square = self.create_square_as_dict()
        coords = self.get_list_of_coordinates(square)
        links = self.assign_adjacent_coordinates(coords)
        return self.number_of_groups(links)

    def get_list_of_coordinates(self, square):
        """get i,j for each used block in square"""
        coords = []
        for i, j in itertools.product(range(128), range(128)):
            block = square[i][j]
            if block == 1:
                coords.append((i, j))
        return coords

    def get_adjacent_coords(self, coord):
        """return all adjacent coordinates to given coord"""
        i, j = coord
        return [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]

    def search_coords(self, c, coords):
        """returns list of adjacent coordinate indicies"""
        lst = []
        for adjacent in self.get_adjacent_coords(c):
            try:
                lst.append(coords.index(adjacent))
            except ValueError:
                continue
        return lst

    def assign_adjacent_coordinates(self, coords):
        """covert coords list into dict of direct links"""
        dct_links = {}
        for i, c in enumerate(coords):
            dct_links[i] = self.search_coords(c, coords)
        return dct_links

    def get_links(self, start, links):
        """return list of links associated with the start number"""
        lst = links[start]
        record = []
        while len(lst) != len(record):
            record = lst.copy()
            for i in record:
                lst += links[i]
            lst = list(set(lst))  # remove duplicates
        return lst
       
    def number_of_groups(self, links):
        """return number of separate groups"""
        lst_all = []
        group_count = 0
        for i in links.keys():
            if i in lst_all:
                continue
            else:
                group_count += 1
                lst = self.get_links(i, links)
                lst_all += lst
        return group_count   
            

        
if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    puzzle = Puzzle(test_flag)
    print("part1:", puzzle.solve_part1())
    print("part2:", puzzle.solve_part2())
    
    """testing"""
    if test_flag:
        assert puzzle.convert_hex_to_bin('f401e') == [1,1,1,1,
                                                      0,1,0,0,
                                                      0,0,0,0,
                                                      0,0,0,1,
                                                      1,1,1,0]
        print("Testing Passed")

    
    