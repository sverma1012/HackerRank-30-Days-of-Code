# Goal: Scope

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0 # create this public integer that can be used in any instance of the class

    def computeDifference(self):
        maximum = max(self.__elements)
        minimum = min(self.__elements)

        self.maximumDifference = maximum - minimum
        return self.maximumDifference

    # Add your code here


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)