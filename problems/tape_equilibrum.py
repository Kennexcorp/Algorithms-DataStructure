# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    # sums = []
    minvalue = None
    
    mid = len(A)//2 if len(A)%2 == 0 else (len(A)//2) + 1

    left = 0
    right = sum(A)

    for P in range(mid):
        left += A[P]
        right -= A[P]

        difference = abs(left - right)

        if minvalue is None or difference < minvalue:
            minvalue = difference
        # sums.append(abs(value))
    return minvalue

ans = solution([10, ])
print(ans)
