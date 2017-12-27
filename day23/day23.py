 # day23
import sys
import operator
from collections import defaultdict

class Puzzle():
    
    def __init__(self, test_flag=False):
        if test_flag:
            self.duet = self.load_into_memory("test.txt")
        else:
            self.duet = self.load_into_memory("input.txt")
        
    def load_into_memory(self, filename):
        """load input into memory"""
        lst = []
        with open(filename) as f:
            for line in f:
                cmd = line.strip('\n').split()
                try:
                    cmd[-1] = int(cmd[-1])
                    cmd[-2] = int(cmd[-2])
                except ValueError:
                    pass
                lst.append(tuple(cmd))
        return lst
                    
    def solve_part1(self):
        """part 1"""
        program = Program()
        i = 0
        while not program.stop:
            try:
                cmd = self.duet[i]
                i = program.run_command(cmd, i)
            except IndexError:
                break
        return program.count_mul

    def solve_part2(self):
        """part 2 - replicate assembly code"""
        print("Please wait...")
        a,b,c,d,e,f,g,h = 1,0,0,0,0,0,0,0
        b = 84
        c = b
        b *= 100
        b -= -100000
        c = b
        c -= -17000
        while True:  # jnz 1 -23
            f = 1
            d = 2
            while g != 0:
                if b % d == 0:
                    f = 0
                g = 0
                d += 1
                g = d - b
            if f == 0:
                h += 1
            g = b - c 
            if g == 0:
                return h + 1
            b += 17

                









        
class Program():
    ops = {'add': operator.add,
           'mul': operator.mul,
           'mod': operator.mod,
           'sub': operator.sub}
    
    def __init__(self, p=0, part=1):
        self.registers = defaultdict(int)
        self.previous_f = 0
        self.inbox = []
        self.outbox = []
        self.stop = False
        self.waiting = False
        self.count = 0
        self.count_mul = 0
        if part == 1:
            self.rcv = self.rcv1
            self.snd = self.snd1
        elif part == 2:
            self.rcv = self.rcv2
            self.snd = self.snd2
    
    def send(self):
        """sends outbox"""
        try:
            out = self.outbox.pop(0)
        except:
            out = None
        return out

    def receive(self, rec):
        """receives data into inbox"""
        if rec != None:
            self.inbox.append(rec)
        return

    def run_command(self, cmd, i):
        """runs command at a time and returns next i"""
        i = i
        op, x = cmd[:2]
        try:
            y = cmd[2]
        except IndexError:
            y = None
        if op == 'set':
            self._set(x, y)
        elif op in ('add', 'mul', 'mod', 'sub'):
            if op =='mul':
                self.count_mul += 1
            self.calculation(op, x, y)
        elif op =='snd':
            self.snd(x)
        elif op == 'rcv':
            self.stop = self.rcv(x)
            if self.waiting:
                return i
        elif op == 'jgz':
            i += self.jgz(x, y)
            return i
        elif op == 'jnz':
            i += self.jnz(x, y)
            return i
        else:
            print("unknown command:", op)
            input("Coninue?")
        i += 1
        return i
               
    def resolve(self, x):
        """returns value of register, or value"""
        if type(x) == int:
            return x
        else:
            return self.registers[x]
        
    def snd1(self, x):
        """updates previous_f with frequency"""
        self.previous_f = self.resolve(x)
        return

    def _set(self, x, y):
        """updates dictionary with new register value"""
        self.registers[x] = self.resolve(y)
        return

    def calculation(self, op, x, y):
        """performs adding, mulitplying and modulus"""
        self.registers[x] = self.ops[op](self.resolve(x), self.resolve(y))
        return

    def jgz(self, x, y):
        """jumps index by y if x > 0"""
        if self.resolve(x) > 0:
            return self.resolve(y)
        return 1

    def jnz(self, x, y):
        """jumps index by y if x != 0"""
        if self.resolve(x) != 0:
            return self.resolve(y)
        return 1

    def rcv1(self, x):
        """if x != 0 then update list"""
        if self.resolve(x) != 0:
            return True
        return False

    def rcv2(self, x):
        """waits to receive from other program"""
        try:
            self.registers[x] = self.inbox.pop(0)
            self.waiting = False
        except IndexError:
            self.waiting = True
        return self.waiting

    def snd2(self, x):
        """sends x to other program inbox"""
        self.outbox.append(self.resolve(x))
        self.count += 1
        return



             
    
        
        
if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    puzzle = Puzzle(test_flag)
    part1 = puzzle.solve_part1()
    print("part1:", part1)
    part2 = puzzle.solve_part2()
    print("part2:", part2)
    

    if test_flag:
        assert part1 == 4
        print("testing complete successfully")
        

    
    