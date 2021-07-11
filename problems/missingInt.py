def solution(A):

    A = list(filter(lambda x: x > 0, A))

    if not A:
        return 1

    arrlen = len(A)

    if arrlen == 1:
        return A[0]+1
    # remove duplicates
    non_duplicate_numbers = list(set(A))

    # sort numbers
    non_duplicate_numbers.sort()

    

    missingnumber = None

    if arrlen > 1:

        if non_duplicate_numbers[0] < 0 and non_duplicate_numbers[-1] < 0:
            
            return 1
        # sum of array including missing number
    numbersrange = list(range(non_duplicate_numbers[0], non_duplicate_numbers[-1]+1))
    sum_of_array_with_missing_number = sum(numbersrange)
    # sum of array without missing number
    arrsum = sum(non_duplicate_numbers)

    

    missingnumber = sum_of_array_with_missing_number - arrsum

    print(arrsum, sum_of_array_with_missing_number)

    if missingnumber == 0:
        return non_duplicate_numbers[-1]+1
    return missingnumber

ans = solution([-1000, 1000])
print(ans)

