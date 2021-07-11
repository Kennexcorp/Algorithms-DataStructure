# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.

    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]

    twinnumbers = {}

    for x in A:

        try:
            del twinnumbers[x]
        except:
            twinnumbers[x] = True
    
    if len(twinnumbers) == 1:
        return list(twinnumbers.keys())[0]

    

print(solution([9, 3, 9, 3, 9, 7, 9]))

# if len(A) == 1:
#         return A[0]

#     twinnumbers = {}

#     for x in range(len(A)):

#         for y in range(x+1, len(A)):

#             if A[x] == A[y]:

#                 twinnumbers[A[x]] = True

#                 break

#         try:
#             not twinnumbers[A[x]]
#         except:
#             return A[x]
    