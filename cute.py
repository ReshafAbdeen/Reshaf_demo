import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = LRUCache(capacity=2)
cache.put(1, 100)
cache.put(2, 200)
print("Get 1:", cache.get(1))  # Returns 100 (1 is now most recently used)
cache.put(3, 300)              # Evicts key 2
print("Get 2:", cache.get(2))  # Returns -1 (evicted)
cache.put(4, 400)              # Evicts key 1
print("Get 1:", cache.get(1))  # Returns -1 (evicted)
print("Get 3:", cache.get(3))  # Returns 300