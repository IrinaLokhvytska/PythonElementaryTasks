class Buffer:
    def __init__(self):
        self.queue = list()

    def add(self, *a):
        for v in a:
            self.queue.append(v)
            if len(self.queue) == 5:
                firstFiveElement = self.queue[:5]
                self.queue = self.queue[5:]
                total = 0
                for v in firstFiveElement:
                    total += v
                print(total)

    def get_current_part(self):
        return self.queue

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())
buf.add(4, 5, 6)
print(buf.get_current_part())
buf.add(7, 8, 9, 10)
print(buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 8, 9))
print(buf.get_current_part() )