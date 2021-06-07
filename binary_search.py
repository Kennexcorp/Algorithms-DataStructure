                                # Binary search works when the list is in sorted order
                                # Logarithmic time = O(log n)

def binary_search(arr, item):

    
    low = 0
    high = len(arr) - 1  
    step = 0       # Low and High keeps track of with part of the list to search in

    while low <= high:
        
        mid = int((low + high) / 2) # Convert to int because division returns a float

        guess = arr[mid]

        if guess == item:
            return 'Position: ' + str(mid) + ' ' +  'Number of steps: ' + str(step)

        
        if guess > item:        # Guess is too high
            high = mid - 1
            step += 1
        else:                   # Guess is too low
            low = mid + 1
            step += 1
    
    return None                 # Item does not exist


                                # Run Tests

sorted_list = [ x for x in range(128)]   # Create a sorted list of 100 items

print(binary_search(sorted_list, 127))

print(binary_search(sorted_list, 2))
