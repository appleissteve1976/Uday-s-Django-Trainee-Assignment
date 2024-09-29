class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._attributes = [('length', self.length), ('width', self.width)]
        self._index = 0

    # iterate
    def __iter__(self):
        return self

    # action in each iteraction
    def __next__(self):
        if self._index < len(self._attributes):
            attr = self._attributes[self._index]
            self._index += 1
            return {attr[0]: attr[1]}
        else:
            self._index = 0  # Reset the index for future iterations
            raise StopIteration
