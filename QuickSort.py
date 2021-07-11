class QuickSort:

    def __init__(self):
        pass

    def quicksort(self, arr):

        if len(arr) < 2:
            return arr

        else:

            pivot = arr[0]
            
            less = [i for i in arr[1:] if i <= pivot]

            greater = [i for i in arr[1:] if i > pivot]

            return self.quicksort(less) + [pivot] + self.quicksort(greater)

quickSort = QuickSort()

print(quickSort.quicksort([1, 5, 2, 3, 4]))