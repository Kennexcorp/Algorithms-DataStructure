class MergeSort:

    def __init__(self, arr):
        self.array = arr

        self.mid = len(self.array)//2
        self.left = self.array[:self.mid]
        self.right = self.array[self.mid:]

        # self.merge_sort(self.left)
        # self.merge_sort(self.right)


    def merge_sort(self):
    

        i = j = k = 0

        while i < len(self.left) and j < len(self.right):

            if self.left[i] < self.right[j]:
                self.array[k] = self.left[i]
                i += 1
            else:
                self.array[k] = self.array[j]
                j += 1
            k += 1
        
        if i < len(self.left):
            self.array += self.left

        if j < len(self.right):
            self.array += self.right

        return self.array

arr = [12, 11, 13, 5, 6, 7]
mergeSort = MergeSort(arr)
ans = mergeSort.merge_sort(mergeSort.left)
print(ans)
