class ProductOfNumbers(object):

    def __init__(self):
        self.array = [1]

    def add(self, num):
        if num == 0:
            self.array = [1]
        else:
            self.array.append(self.array[-1]*num)

    def getProduct(self, k):
        if k > len(self.array)-1:
            return 0
        return int(self.array[-1] / self.array[-k-1])
