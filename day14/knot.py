 # day14_knot
import operator
import functools

class Knot():
    size = 256
    
    def __init__(self, hash_input):
        self.lst = []
        self.hash_input = hash_input
        self.solution = self.solve()

    def solve(self):
        """solve the knot"""
        self.lst = list(range(self.size))
        asci = self.convert_to_ascii(self.hash_input)
        lng = self.append_input(asci)
        l = len(self.lst)
        self.mult_rounds_of_lengths(rounds=64, lng=lng, i=0, s=0, l=l)
        sparse_hash = self.lst
        dense_hash = self.convert_to_dense_hash(sparse_hash)
        return self.convert_to_hex_string(dense_hash)

    def convert_to_ascii(self, hash_input):
        """convert input lengths to ascii"""
        asci = []
        for c in hash_input:
            asci.append(ord(c))
        return asci

    def append_input(self, asci):
        """appends numbers to ascii list"""
        return asci + [17,31,73,47,23] 

    def mult_rounds_of_lengths(self, rounds, lng, i, s, l):
        """loops through loops of lengths"""
        for r in range(rounds):
            i, s = self.loop_through_lengths(lng, i, s, l)

    def loop_through_lengths(self, lng, i, s, l):
        """loops through one round of lengths"""
        for n in lng:
            self.reverse_subset(n, i%l, l)
            i += (n + s)
            s += 1
        return i, s

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

        
if __name__ == '__main__':    
    # testing
    test1 = '183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88'
    test2 = '3,4,1,5'
    knot1 = Knot(test1)
    assert knot1.solve() == '90adb097dd55dea8305c900372258ac6'
    knot2 = Knot(test2)
    assert knot2.solve() == '4a19451b02fb05416d73aea0ec8c00c0'
    print("Testing Passed")





    
    