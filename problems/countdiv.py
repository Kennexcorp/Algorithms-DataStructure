def solution(A, B, K):
    
    if A == B == 0:
        return 0

    listrange = list(range(A, B+1))
    divisible = filter(lambda x: x%K == 0, listrange)
    divisiblelist = list(divisible)

    return len(divisiblelist)

print(solution(0,1,11))