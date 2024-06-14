# chaining using list 

class hashmap:
    def __init__(self) -> None:
        self.MAX = 100
        self.array = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        for i in range(len(self.array[h])):
            if self.array[h][i][0]  == key: 
                self.array[h].pop(i)
                break
               
        self.array[h].append((key, value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for i in self.array[h]:
            if i[0] == key: return i[1]
        return 'not fount'

ha = hashmap()
ha['name'] = 'rahul'
ha['eman'] = 'abhijith'
print(ha.array)
print(ha['name'])
print(ha.array)
