# Day One

input = open("day01_input.txt")

# part 1
for line in input:
    line = line.splitlines()[0]
    line_match = line[-1] + line[:-1]
    
    total = 0
    for i, char in enumerate(line):
        if char == line_match[i]:
            total += int(char)
    
    print("Part 1:", total)
    
# part 2
    line = line.splitlines()[0]
    line_half_len = int(len(line) / 2)
    line_match = line[-line_half_len:] + line[:-line_half_len]
    
    total = 0
    for i, char in enumerate(line):
        if char == line_match[i]:
            total += int(char)
    
    print("Part 2:", total)

input.close()
            
        