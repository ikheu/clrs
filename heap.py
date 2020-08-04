class Heap:
    def __init__(self, data):
        # self._data = [None]
        self._data = data
        self.build()

    def parent(self, i):
        return ((i+1) >> 1) - 1

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i):
        return self._data[i]

    def __setitem__(self, i, v):
        self._data[i] = v

    def max_heapify(self, i, size):
        l, r = self.left(i), self.right(i)
        if l < size and self[l] > self[i]:
            lagest = l
        else:
            lagest = i
        if r < size and self[r] > self[lagest]:
            lagest = r
        if lagest != i:
            self[lagest], self[i] = self[i], self[lagest]
            self.max_heapify(lagest, size)

    def build(self):
        for i in range(len(self) >> 1, -1, -1):
            self.max_heapify(i, len(self))

    def sort(self):
        size = len(self)
        for i in range(len(self) - 1, 0, -1):
            self[0], self[i] = self[i], self[0]
            size -= 1
            self.max_heapify(0, size)

    def __repr__(self):
        return "heap(%s)" % self._data

if __name__ == '__main__':
    arr = [8, 7, 9, 16, 4, 10, 3, 2, 1, 14]
    h = Heap(arr)
    print(h)
    h.sort()
    print(h)

# i l r p
# 1 2 3 0
# 2 4 5 1
# 3 6 7 1

# 0 1 3 -1  (i+1) * 2 - 1 = 2*i+1, 2*i+2, (i+1)//2-1
# 1 3 4 0
# 2 5 6 0