class BinarySearch:

    def __init__(self, arr):
        self.arr = arr

    def binary_search(self, item):

        low = 0
        high = len(self.arr) - 1  
        step = 0       # Low and High keeps track of with part of the list to search in

        while low <= high:
            
            mid = int((low + high) / 2) # Convert to int because division returns a float

            guess = self.arr[mid]

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
binarySearch = BinarySearch(sorted_list)

print(binarySearch.binary_search(3))

