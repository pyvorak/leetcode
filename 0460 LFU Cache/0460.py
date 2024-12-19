class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq = {}
        self.LRU = defaultdict(OrderedDict)
        self.min_freq = 0

    def inc(self, key):
        f = self.freq[key]
        self.LRU[f].pop(key)
        if len(self.LRU[f]) == 0:
            del self.LRU[f]
        
        f += 1
        self.LRU[f][key] = 1
        self.freq[key] = f
        
        if self.min_freq not in self.LRU:
            self.min_freq = f

    def add(self, key, value):
        self.freq[key] = 1
        self.cache[key] = value
        self.LRU[1][key] = 1
    
    def delete(self):
        k, _ = self.LRU[self.min_freq].popitem(last=False)
        del self.cache[k]
        del self.freq[k]

    def get(self, key: int) -> int:
        if key in self.cache:
            self.inc(key)
            return self.cache[key] 
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.inc(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                self.delete()
            self.add(key, value)
            self.min_freq = 1
