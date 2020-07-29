class Heap:
    def __init__(self, data):
        self._data = [None]
        self._data.extend(data)

    def node_parent(self, index):
        return self._data(index >> 1)

    def node_left(self, index):
        index = index << 1
        if index >= len(self._data):
            return self._data(index)
        else:
            return None

    def node_right(self, index):
        index = (index << 1) + 1
        if index >= len(self._data):
            return self._data(index)
        else:
            return None
