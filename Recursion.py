class Recursion:

    def __init__(self):
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

recursion = Recursion()
# print(recursion.countdown(9))
print(recursion.factorial(3))