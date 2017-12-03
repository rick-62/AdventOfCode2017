# day02

import itertools

def difference():
    """part 1: yield each row diff"""
    for row in input:
        num_lst = [int(c) for c in row.split("\t")]
        mx = max(num_lst)
        mn = min(num_lst)
        yield mx - mn
        
def even_divide():
    """part 2: yield each row even division"""
    for row in input:
        num_lst = [int(c) for c in row.split("\t")]
        for i, j in itertools.permutations(num_lst, 2):
            if i % j == 0:
                yield i / j
        
with open("day02_input.txt") as input:
    
    #checksum = sum(difference()) # part 1
    checksum = sum(even_divide()) # part 2
    
    print(checksum)
    


    
        
        
            
                
            
    
    
    
            
    
        