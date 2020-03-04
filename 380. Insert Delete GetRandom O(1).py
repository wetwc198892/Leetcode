from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.setdata = {}
        self.listdata = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.setdata:
            return False
        self.listdata.append(val)
        self.setdata[val] = len(self.listdata)-1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.setdata:
            return False
        i = self.setdata.get(val)
        temp = self.listdata[-1]
        self.setdata[temp] = i
        self.listdata[i] = temp
        self.setdata.pop(val)
        self.listdata.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.listdata)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()