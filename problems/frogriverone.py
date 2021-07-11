# def solution(X, A):
    
    

#     leafpaths = {}
    

#     for K in range(len(A)):
        
#         leafpaths[A[K]] = True

#         if len(leafpaths) == X:
    
#             return K

#     return -1

def solution(X, A):
    # write your code in Python 3.6
    if not A:
        return -1
        
    if len(A) == 1 and A[0] != 1:
        return -1

    leafpaths = [False]*(X+1)
    K = 0
    jump = 1

    for K in range(len(A)):

        leafpaths[A[K]] = True
        
        while leafpaths[jump] == True:

            if jump == X:

                return K
            
            jump += 1

    return -1

# [1,3,1,4,2,3,5,4]
arr = [1,3,1,4,2,3,5,4]
X = 5

ans = solution(X, arr)
print(ans)