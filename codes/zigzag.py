"""
[1,3,5,7,9,] [2,4,6,8] => [1,2,3,4,5,6,7,8,9]
"""


class Zigzag:
    def __init__(self, l1, l2):
        self.queue = [l1, l2]

    def next(self):
        v = self.queue.pop(0)
        r = v.pop(0)
        if v:
            self.queue.append(v)
        return r

    def has_next(self):
        if self.queue:
            return True
        return False



z  = Zigzag([1,3,5,7,9,], [2,4,6,8] )

while z.has_next():
    print(z.next(), end=" ")