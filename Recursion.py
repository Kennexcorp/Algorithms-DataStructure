class Recursion:

    def __init__(self):
        self.sums = 0
        pass

    def countdown(self, i):
        print(i)
        if i < 0:
            return
        else:
            return self.countdown(i - 1)

    def factorial(self, i):
        if i == 1:
            return i
        else:
            return i * self.factorial(i - 1);


    def sumNumbers(self, arr: list):
        a = len(arr)
        if len(arr) == 1:
            return self.sums 
        else:
            
            return arr[a-1] + self.sumNumbers(arr[:a-1])
        

recursion = Recursion()
# print(recursion.countdown(9))
print(recursion.factorial(1000))
# print(recursion.sumNumbers([4,5,7]))