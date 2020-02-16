class LRUCache:

    def __init__(self, capacity: int):
        self.new_map = {}
        self.queue = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.new_map:
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
            return self.new_map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.new_map[key] = value
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)
        if len(self.new_map) > self.capacity:
            min_key = self.queue.pop(0)
            self.new_map.pop(min_key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
