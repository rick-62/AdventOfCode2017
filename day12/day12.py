 # day12

class Puzzle():

    def __init__(self, test_flag=False):
        if test_flag:
            self.raw_dct = self.load_into_memory("test.txt")
        else:
            self.raw_dct = self.load_into_memory("input.txt")

    def load_into_memory(self, filename):
        """load input into memory string"""
        dct = {}
        with open(filename) as f:
            for line in f:
                dct.update(self.convert_to_dct(line, ' <-> '))
        return dct

    def convert_to_dct(self, line, delim):
        """converts string to dictionary, with ints"""
        return {int(a):[int(b2) for b2 in b.split(',')] 
                for a,b 
                in [line.strip('\n').split(delim)]}
      
    def get_links(self, start):
        """return list of links associated with the start number"""
        lst = self.raw_dct[start]
        record = []
        while len(lst) != len(record):
            record = lst.copy()
            for i in record:
                lst += self.raw_dct[i]
            lst = list(set(lst))  # remove duplicates
        return lst

    def solve_part1(self):
        """return number of links to '0'"""
        links = self.get_links(0)
        return len(links)

    def solve_part2(self):
        """return number of separate groups"""
        lst_all = []
        group_count = 0
        for i in self.raw_dct.keys():
            if i in lst_all:
                continue
            else:
                group_count += 1
                lst = self.get_links(i)
                lst_all += lst
        return group_count

        
if __name__ == '__main__':
    puzzle = Puzzle(test_flag=False)
    print("part1:", puzzle.solve_part1())
    print("part2:", puzzle.solve_part2())
    