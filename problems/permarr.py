# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    sortedA = sorted(A)

    if not A:

        return 0
    
    nextnumber = min(sortedA)

    for x in sortedA:

        if x != nextnumber:
            
            return 0

        if x == nextnumber:

            nextnumber += 1

    return 1