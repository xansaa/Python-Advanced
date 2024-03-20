class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterator = -1

    def __iter__(self):
        return self

    def __next__(self):

        if self.iterator == self.count - 1:
            raise StopIteration

        self.iterator += 1
        return self.iterator * self.step


