"""
Merge function for 2048 game.
"""

def merge(line):

    """
    Function that merges a single row or column in 2048.
    """
    #Initialize temporary variables
    if(len(line) == 0):
        return []
    idx1 = 0
    idx2 = 0
    merged = 0
    out1 = [0] * len(line)
    # A simple loop to loop through the list
    while ((idx1 < len(line)) and (idx2 < len(line))):
        while ((idx2 < len(line)) and (line[idx2] == 0)):
            idx2 = idx2 + 1
        if(idx2 < len(line)):
            out1[idx1] = line[idx2]
        if ((idx1 >= 1) and (out1[idx1] == out1[idx1-1]) and (merged == 0)):
            out1[idx1-1] = out1[idx1-1] + out1[idx1]
            out1[idx1] = 0
            idx1 = idx1 - 1
            merged = 1
        else:
            merged = 0
        idx1 = idx1 + 1
        idx2 = idx2 + 1
    return out1
	
	
line = [8, 16, 16, 8]
a = merge(line)
print line
print a
