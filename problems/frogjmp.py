# X = frogs current position
# Y = destination 
# D = fixed jump distance

# def frogjmp(x, y, d):

#     totalDistance = x
#     steps = 0
#     while totalDistance <= y:
#         totalDistance  += d
#         steps += 1
#     return totalDistance, steps

def frogjmp(X, Y, D):
    
    Q= Y-X
    R = Q//D
    return R if Q%D == 0 else R+1
            


print(frogjmp(2,85,30))