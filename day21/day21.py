 # day21
import sys
import numpy as np

class Puzzle():
    
    def __init__(self, test_flag=False):
        if test_flag:
            self.rules = self.load_into_memory("test.txt")
        else:
            self.rules = self.load_into_memory("input.txt")
        
    def load_into_memory(self, filename):
        """load input into memory"""
        dct = {}
        with open(filename) as f:
            for line in f:
                k, v = line.strip('\n').split(' => ')
                key = tuple([tuple(row) for row in k.split('/')])
                val = np.array([list(row) for row in v.split('/')])
                dct[key] = val
                # key is tuple-tuple array; value is numpy array
        return dct
                    
    def solve_part1(self, n=5):
        """part 1"""
        new_square = np.array([['.','#','.'],['.','.','#'],['#','#','#']])
        for i in range(n):
            new_arrays = []
            for square in self.split_square(new_square):
                arrays = self.get_variations(square)
                new_arrays.append(self.check_rules(arrays))
            new_square = self.stitch_arrays(new_arrays)
        return np.count_nonzero(new_square == '#')
        

    def split_square(self, arr):
        """split square into 2x2 or 3x3 chunks"""
        arr_len = len(arr)
        if arr_len % 2 == 0:
            new_squares = self.blockshaped(arr, 2, 2)
        elif arr_len % 3 == 0:
            new_squares = self.blockshaped(arr, 3, 3)
        else:
            print("error occured:", arr)
        return new_squares

    @staticmethod
    def blockshaped(arr, nrows, ncols):
        """
        Return an array of shape (n, nrows, ncols) where
        n * nrows * ncols = arr.size

        If arr is a 2D array, the returned array should look like n subblocks with
        each subblock preserving the "physical" layout of arr.
        """
        h, w = arr.shape
        return (arr.reshape(h//nrows, nrows, -1, ncols)
                .swapaxes(1,2)
                .reshape(-1, nrows, ncols))

    def get_variations(self, square):
        """all variations of 2x2 or 3x3 pattern"""
        np_square = np.array(square)
        variations = [np_square]
        size = len(np_square)
        if size >= 2:
            for i in range(1,4):
                rot = np.rot90(np_square, i)
                variations.append(rot)
        if size >= 3:
            for v in variations.copy():
                flip = np.flipud(v)
                variations.append(flip)
        return [self.array_to_tuple(arr) for arr in variations]
    
    @staticmethod
    def array_to_tuple(arr):
        """convert np array to tuple before dict matching"""
        return tuple(tuple(row) for row in arr.tolist())

    def check_rules(self, arrays):
        """checks variations for rule match"""
        for arr in arrays:
            if arr in self.rules.keys():
                return self.rules[arr]
        else:
            return np.array(arrays[0])

    def stitch_arrays(self, arrays):
        """stich np arrays into new square"""
        side_len = int(len(arrays) ** 0.5)
        temp = [arrays[ x * side_len : (x + 1) * side_len ] 
                for x 
                in range(side_len)]
        return np.block(temp)

    def solve_part2(self):
        """part 2"""
        # part 1 with 18 iterations
        pass
        
                 
        
if __name__ == '__main__':
    test_flag = True if 'test' in sys.argv else False
    puzzle = Puzzle(test_flag)
    n = 2 if test_flag else 5
    part1 = puzzle.solve_part1(n)
    print("part1:", part1)
    part2 = puzzle.solve_part1(n=18)
    print("part2:", part2)
    

    if test_flag:
        assert list(puzzle.get_variations(
            np.array([[2,3],[3,4]]))[1]) == [(3, 4), (2, 3)]
        assert len(puzzle.get_variations(
            np.array([[2,3,4],[4,5,6],[5,4,3]]))) == 8

        print("testing complete successfully")
        

    
    