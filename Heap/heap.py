class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = self.parent(index)
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    
    def delete(self, value):
        try:
            index = self.heap.index(value)
        except ValueError:
            return
        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]

        self.heap.pop()

        if index < len(self.heap):
            self._heapify_up(index)
            self._heapify_down(index)

# Example usage:
heap = MinHeap()
heap.insert(10)
heap.insert(1)
heap.insert(30)
heap.insert(20)

print(heap.extract_min())  # Output: 1
print(heap.extract_min())  # Output: 10
print(heap.extract_min())  # Output: 20
print(heap.extract_min())  # Output: 30
