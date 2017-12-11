 # day10
import operator
import functools

class Puzzle():
    
    def __init__(self, test_flag=False):
        self.lst = []
        if test_flag:
            self.raw = self.load_into_memory("test.txt")
            self.size = 5
        else:
            self.raw = self.load_into_memory("input.txt")
            self.size = 256

    def load_into_memory(self, filename):
        """load input into memory string"""
        with open(filename) as f:
            string = f.read()
            return string

    def reverse_subset(self, n, i, l):
        """returns list with subset reversed"""
        circular = True if i + n > l else False
        if not circular:
            end_1 = i + n
            subset_2 = []
            subset_1 = self.lst[i:end_1]
        else:
            end_1 = l
            subset_1 = self.lst[i:end_1]
            end_2 = (i + n) % l
            subset_2 = self.lst[:end_2]
        rev = (subset_1 + subset_2)[::-1]  # reverse subset
        self.lst[i:end_1] = rev[:len(subset_1)]
        if circular: self.lst[:end_2] = rev[-len(subset_2):]
        return
        
    def split_input(self):
        """split input lengths into list"""
        return [int(n) for n in self.raw.split(',')]
    
    def loop_through_lengths(self, lng, i, s, l):
        """loops through one round of lengths"""
        for n in lng:
            self.reverse_subset(n, i%l, l)
            i += (n + s)
            s += 1
        return i, s

    def solve_part1(self):
        """returns multiplication of first two numbers"""
        self.lst = list(range(self.size))
        i, s = 0, 0
        l = len(self.lst)
        lng = self.split_input()
        self.loop_through_lengths(lng, i, s, l)
        return self.lst[0] * self.lst[1]
            
    def convert_to_ascii(self):
        """convert input lengths to ascii"""
        asci = []
        for c in self.raw:
            asci.append(ord(c))
        return asci

    def append_input(self, asci):
        """appends numbers to ascii list"""
        return asci + [17,31,73,47,23] 
        
    def mult_rounds_of_lengths(self, rounds, lng, i, s, l):
        """loops through loops of lengths"""
        for r in range(rounds):
            i, s = self.loop_through_lengths(lng, i, s, l)

    def convert_to_dense_hash(self, sparse_hash):
        """convert sparse to dense hash"""
        dense_hash = []
        for i in range(0, 256, 16):
            block = sparse_hash[i:i+16]
            reduced = functools.reduce(operator.xor, block)
            dense_hash.append(reduced)
        return dense_hash
    
    def convert_to_hex_string(self, d_hash):
        """converts hash to hex and combines into 1 string"""
        hex = ''
        for n in d_hash:
            hex += '{0:02x}'.format(n)
        return hex

    def solve_part2(self):
        """part2"""
        self.lst = list(range(self.size))
        asci = self.convert_to_ascii()  # convert raw input
        lng = self.append_input(asci)
        l = len(self.lst)
        self.mult_rounds_of_lengths(rounds=64, lng=lng, i=0, s=0, l=l)
        sparse_hash = self.lst
        dense_hash = self.convert_to_dense_hash(sparse_hash)
        return self.convert_to_hex_string(dense_hash)
        
if __name__ == '__main__':
    puzzle = Puzzle(test_flag=False)
    print("part1:", puzzle.solve_part1())
    print("part2:", puzzle.solve_part2())
    