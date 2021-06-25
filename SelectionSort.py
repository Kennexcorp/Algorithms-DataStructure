class SelectionSort:

    def __init__(self, arr: list):
        self.array = arr
        
    def findSmallest(self, data: list):
        smallest = data[0]
        smallestIndex = 0
        for i in range(1, len(data)):
            if smallest > data[i]:
                smallestIndex = i
                smallest = data[i]
        return smallestIndex

    def sortArray(self):
        newArray = []
        for i in range(len(self.array)):
            smallest = self.findSmallest(self.array)
            newArray.append(self.array.pop(smallest))
        return newArray

# Run selection sort
selectionSort = SelectionSort([2, 4, 1, 3, 9, 5, 6])
print(selectionSort.sortArray())