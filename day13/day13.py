 # day13
import sys
import itertools

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
                dct.update(self.convert_to_dct(line, ': '))
        return dct
        
    def convert_to_dct(self, line, delim):
        """converts string to dictionary, with ints"""
        return {int(a):int(b) for a,b in [line.strip('\n').split(delim)]}
        
    def solve_part1(self):
        """part 1"""
        firewall = self.initiate_firewall()
        total = 0
        for i in range(max(self.raw_dct.keys()) + 1):
            try:
                if firewall[i][0] != 0:
                    total += i * self.raw_dct[i]
            except KeyError:
                pass
            firewall = self.increment_firewall(firewall, self.increment_list)
        return total
                    
    def initiate_firewall(self):
        """create dictionary of lists to replicate firewall"""
        return {a:[1]+[0]*(b-1) for a,b in self.raw_dct.items()}

    def increment_firewall(self, firewall, f):
        """increments each index in the firewall"""
        return {k: f(v) for k, v in firewall.items()}
            
    def increment_list(self, lst):
        """increment list within firewall"""
        if 1 in lst:
            i = lst.index(1)
            lst[i] = 0
            try:
                lst[i+1] = 1
            except IndexError:
                lst[i-1] = -1
        elif -1 in lst:
            i = lst.index(-1)
            lst[i] = 0
            if i == 0:
                lst[i+1] = 1
            else:
                lst[i-1] = -1
        return lst

    # brute force method - see below part2b for better/cleaner method
    def solve_part2(self):
        """part 2"""
        reset_firewall = self.initiate_firewall
        caught = True
        delay = 0
        mx = 0
        while caught == True:
            caught = False
            delay += 1
            firewall = self.delay_firewall(reset_firewall(), delay)
            for i in range(max(self.raw_dct.keys()) + 1):
                if i > mx:
                    mx = i
                    print(delay, i)
                try:
                    if firewall[i][0] != 0 and i > 0:
                        caught = True
                        break
                except KeyError:
                    pass
                firewall = self.increment_firewall(firewall, self.increment_list)
        return delay

    def delay_firewall(self, firewall, delay):
        """increments firewall with delay"""
        firewall = firewall.copy()
        for _ in range(delay):
            firewall = self.increment_firewall(firewall, self.increment_list)
        return firewall

    # better/cleaner implementation (runs in few seconds)
    def solve_part2b(self):
        """more efficient - less brute force"""
        valid_dct = self.initiate_validity_dict()
        delay = 0
        while not self.check_validity(valid_dct, delay):
            delay += 1
        return delay
            
    def initiate_validity_dict(self):
        """create dict for validating pass"""
        return {k: v * 2 - 2 for k, v in self.raw_dct.items()}

    def check_validity(self, valid_dct, delay):
        """check whether proposed delay is valid"""
        for k, v in valid_dct.items():
            inc = k + delay
            if inc % v == 0:
                return False
        return True
            
        
if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    puzzle = Puzzle(test_flag)
    print("part1:", puzzle.solve_part1())
    print("part2:", puzzle.solve_part2b())
    
    """testing"""
    def test_list(lst=[1,0,0,0], f=puzzle.increment_list):
        for i in range(20):
            lst = f(lst)
        return lst

    if test_flag:
        assert test_list(lst=[1,0,0,0]) == [0,0,1,0]

    
    