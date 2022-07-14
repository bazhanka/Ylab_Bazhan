class CyclicIterator:
    def __init__(self, iterable):
        self.current = -1
        self.stop = iterable[-1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            self.current+=1
            return self.current
        else:
            self.current = 0
            return self.current

cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
