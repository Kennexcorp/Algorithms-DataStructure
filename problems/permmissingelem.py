def permmissingelem(A):
    # A.sort()
    if not A:
        return 1

    if len(A) <= 1:
        return A[0]+1

    maxnum = max(A)
    nums = range(1, maxnum+1)

    missingnum = sum(list(nums)) - sum(A)

    if missingnum == 0:
        return A[-1]+1

    return missingnum


hello = permmissingelem([1,2,3,5])
print(hello)