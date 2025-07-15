# [a,b,c,d,e,f,g,h] [2,4,6,8]


class zig:
    def __init__(self, l1, l2):
        self.q = [l1, l2]

    def next(self):
        v = self.q.pop(0)
        r = v.pop(0)
        if v:
            self.q.append(v)
        return r
    
    def has_next(self):
        if self.q:
            return True
        return False

z = zig(["a", "b", "c", "d", "e", "f", "g", "h"], [2, 4, 6, 8, 1])

while z.has_next():
    print(z.next(), end=" ")
