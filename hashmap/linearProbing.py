class hashmap:
    def __init__(self) -> None:
        self.MAX = 100
        self.array = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        while self.array[h] is not None:
            h = (h + 1) % self.MAX
        self.array[h] = key, value
    


    def __getitem__(self, key):
        h = self.get_hash(key)
        while self.array[h] is not None:
            if self.array[h][0] == key:
                return self.array[h][1]
            h = (h + 1) % self.MAX
        return 'not found'



h = hashmap()
h['name'] = 'rahul'
h['age'] = 20
print(h['name'])